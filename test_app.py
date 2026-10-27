import json
import os
from fastapi.testclient import TestClient
from app import app

# Création d'un client de test pour notre application FastAPI
client = TestClient(app)

def test_health_check():
    """Vérifie que la route /health répond correctement et renvoie le statut ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model_version" in data

def test_predict_valid():
    """Vérifie qu'un texte valide renvoie bien une prédiction et une probabilité."""
    response = client.post("/predict", json={"text": "A terrifying ghost haunts a family in an isolated house."})
    assert response.status_code == 200
    data = response.json()
    assert "prediction_class" in data
    assert "probability" in data
    assert data["prediction_class"] in ["Horreur", "Comédie"]

def test_predict_invalid_empty():
    """Vérifie qu'un texte vide est bien refusé (Erreur 400)."""
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400

def test_predict_invalid_too_short():
    """Vérifie qu'un texte trop court (< 5 caractères) est refusé (Erreur 400)."""
    response = client.post("/predict", json={"text": "Hi"})
    assert response.status_code == 400

def test_metrics_minimum_score():
    """Vérifie que le modèle enregistré respecte un score F1 minimum acceptable."""
    metrics_path = os.path.join("model", "metrics.json")
    assert os.path.exists(metrics_path), "Le fichier metrics.json est introuvable."
    
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    
    # Récupération du score F1 (adaptez la clé selon votre fichier metrics.json)
    f1_score = metrics.get("test_f1_score", 0.0)
    
    # On impose un seuil minimal de validation (par exemple 0.60)
    assert f1_score >= 0.60, f"Le score F1 ({f1_score}) est inférieur au seuil minimal requis de 0.60."