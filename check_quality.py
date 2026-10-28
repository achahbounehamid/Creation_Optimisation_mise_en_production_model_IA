import json
import os
import yaml

def validate_model_quality():
    # 1. Charger la configuration
    config_path = "config.yaml"
    if not os.path.exists(config_path):
        raise FileNotFoundError("Le fichier de configuration config.yaml est introuvable.")
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    min_f1 = config.get("min_f1_score", 0.60)
    min_size = config.get("min_test_size", 50)
    
    # 2. Charger les métriques du modèle
    metrics_path = os.path.join("model", "metrics.json")
    if not os.path.exists(metrics_path):
        raise FileNotFoundError("Le fichier metrics.json est introuvable dans le dossier model/.")
    
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    
    actual_f1 = metrics.get("test_f1_score", 0.0)

    actual_size = metrics.get("test_size", 0)
    
    print(f"--- Évaluation de la Barrière Qualité ---")
    print(f"Score F1 requis : {min_f1} | Score F1 actuel : {actual_f1}")
    print(f"Taille de test requise : {min_size} | Taille actuelle : {actual_size}")
    
    # 3. Vérification des seuils
    if actual_f1 < min_f1:
        raise ValueError(f" ÉCHEC : Le score F1 ({actual_f1}) est inférieur au seuil minimal requis ({min_f1}).")
    
    if actual_size < min_size:
        raise ValueError(f" ÉCHEC : La taille de test ({actual_size}) est inférieure au minimum requis ({min_size}).")
        
    print(" SUCCÈS : Le modèle respecte tous les critères de la barrière qualité !")

if __name__ == "__main__":
    validate_model_quality()