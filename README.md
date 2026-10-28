# 🎬 ML Model Deployment & MLOps Pipeline (Movie API)

Ce dépôt contient le code et la configuration nécessaires pour déployer une API d'inférence de modèle d'apprentissage automatique sur **Microsoft Azure** à l'aide d'une démarche MLOps rigoureuse (Tests unitaires, Barrière de qualité, Conteneurisation Docker, CI/CD via GitHub Actions et Déploiement sur Azure Container Apps).

---

## 🛠️ Structure du Projet

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD GitHub Actions
├── model/
│   ├── model.pkl              # Modèle IA entraîné
│   └── threshold.json         # Seuil minimal exigé (Quality Gate)
├── notebooks/
│   └── model_training.ipynb   # Notebook d'expérimentation et d'entraînement
├── app.py                     # API FastAPI (/health, /predict, /hello)
├── quality_gate.py            # Script d'évaluation de la barrière de qualité
├── test_app.py                # Tests unitaires Pytest
├── requirements.txt           # Liste des dépendances Python
├── Dockerfile                 # Instructions de construction de l'image Docker
└── .dockerignore              # Fichiers exclus lors du build Docker

📋 Prérequis
Python 3.10+

Docker Desktop (pour l'exécution des conteneurs en local)

Git

Un compte Microsoft Azure avec :

Un groupe de ressources (ex: hachahbouneRG)

Un registre d'images Azure Container Registry (ex: hamidRegistre)

Un environnement Azure Container Apps (ex: movie-container)

🚀 Installation & Lancement en Local
1. Cloner le projet et préparer l'environnement
# Cloner le dépôt GitHub
git clone [https://github.com/achahbounehamid/Creation_Optimisation_mise_en_production_model_IA.git](https://github.com/achahbounehamid/Creation_Optimisation_mise_en_production_model_IA.git)
cd Creation_Optimisation_mise_en_production_model_IA

# Créer un environnement virtuel Python
python -m venv venv

# Installer les dépendances du projet
pip install -r requirements.txt

2. Exécuter les tests et la barrière de qualité
Avant de lancer l'application, vous pouvez valider le bon fonctionnement de l'API et vérifier si le modèle respecte le seuil de performance requis :
# Exécuter les tests unitaires
pytest test_app.py

# Exécuter la vérification du seuil de qualité 
python quality_gate.py

3. Lancer l'API FastAPI en local
uvicorn app:app --reload --host 0.0.0.0 --port 8000

L'API sera accessible sur http://localhost:8000. Vous pouvez consulter la documentation interactive Swagger sur http://localhost:8000/docs.

Endpoints principaux :
GET /health : Vérifie la disponibilité de l'API et retourne la version active du modèle.

POST /predict : Transmet les caractéristiques en entrée et retourne la prédiction du modèle.

GET /hello : Route de test de déploiement et de mise à jour.

4. Tester l'image Docker en local

# Construire l'image Docker locale
docker build -t movie-api:local .

# Démarrer le conteneur Docker sur le port 8000
docker run -d -p 8000:8000 --name movie-app movie-api:local

# Vérifier la réponse de l'API conteneurisée
curl http://localhost:8000/health

🔄 Pipeline CI/CD (GitHub Actions)
Le fichier .github/workflows/ci-cd.yml définit l'automatisation à chaque git push sur la branche main :

Job test :

Exécute les tests unitaires (pytest).

Exécute quality_gate.py pour vérifier que le score du modèle dépasse la valeur configurée dans model/threshold.json.

Si le modèle ne franchit pas le seuil, la chaîne s'arrête immédiatement (Test Chaîne Rouge).

Job image :

Construit l'image Docker de l'application.

Job publier :

Authentifie GitHub auprès d'Azure Container Registry (ACR).

Pousse l'image sous le tag correspondant au commit SHA (ex: ee5d920...).

☁️ Déploiement & Rollback sur Azure
Déploiement d'une nouvelle révision :
Une fois le pipeline CI/CD validé (chaîne verte), l'image est hébergée sur ACR : hamidregistre.azurecr.io/movie-api:<COMMIT_SHA>.

Sur le portail Azure, accédez à Azure Container Apps (movie-container).

Sous Application > Conteneurs, mettez à jour la Balise d'image avec le tag du commit souhaité.

Cliquez sur Enregistrer en tant que nouvelle révision.

Procédure de Rollback (Retour arrière) :
En cas d'anomalie ou pour restaurer une version précédente stable :

Accédez à la section Conteneurs de l'application Azure Container Apps.

Saisissez la balise correspondant au commit stable précédent (ex: ee5d920...).

Validez la création de la révision. L'application rebascule instantanément sur l'ancienne version.

🧹 Nettoyage des Ressources Cloud
Pour supprimer l'ensemble des ressources créées sur Microsoft Azure et éviter toute facturation :
# Suppression du groupe de ressources complet
az group delete --name hachahbouneRG --yes --no-wait

