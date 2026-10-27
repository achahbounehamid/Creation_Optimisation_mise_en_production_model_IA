import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import joblib
import numpy as np

app = FastAPI(title="Movie Classification API", version="1.0")

# 1. Chargement unique des artefacts au démarrage de l'API
MODEL_DIR = "model"

try:
    model = tf.keras.models.load_model(os.path.join(MODEL_DIR, "model.keras"))
    vectorizer = joblib.load(os.path.join(MODEL_DIR, "vectoriseur.joblib"))
    with open(os.path.join(MODEL_DIR, "metrics.json"), "r", encoding="utf-8") as f:
        metrics_data = json.load(f)
        model_version = metrics_data.get("model_version", "1.0")
except Exception as e:
    print(f"Erreur lors du chargement des artefacts : {e}")

# Définition du format de la requête entrante
class MovieRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    """Route de santé : renvoie 'ok' et la version du modèle."""
    return {
        "status": "ok",
        "model_version": model_version
    }

@app.post("/predict")
def predict_movie(request: MovieRequest):
    """Route de prédiction : reçoit un texte, renvoie la classe, la probabilité et la version."""
    text = request.text
    
    # Validation du texte : gestion des cas vides ou espaces
    if not text or not text.strip():
        raise HTTPException(
            status_code=400, 
            detail="Erreur : Le texte fourni est vide ou invalide."
        )
    
    # Cas limite : texte trop court (moins de 5 caractères)
    if len(text.strip()) < 5:
        raise HTTPException(
            status_code=400, 
            detail="Erreur : Le texte est trop court pour être analysé (minimum 5 caractères requis)."
        )
    
    try:
        # Transformation du texte avec le vectoriseur TF-IDF
        text_tfidf = vectorizer.transform([text])
        text_dense = text_tfidf.toarray()
        
        # Prédiction avec le modèle Keras
        prediction_prob = float(model.predict(text_dense)[0][0])
        
        # Seuil à 0.5 (0 = Comédie / 1 = Horreur)
        predicted_class = 1 if prediction_prob >= 0.5 else 0
        class_label = "Horreur" if predicted_class == 1 else "Comédie"
        
        return {
            "prediction_class": class_label,
            "probability": round(prediction_prob, 4),
            "model_version": model_version
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Erreur interne lors de la prédiction : {str(e)}"
        )