# Plan de projet — Classification de films par IA

## Tableau de planification

| ID | Tâche | Dépend de | Charge estimée | Charge réelle | Ressources | Date prévue | Statut |
|---|---|---|---:|---|---|---|---|
| T01 | Planifier le projet et créer le dépôt | Aucune | 1 h | À renseigner | VS Code, Git, GitHub | 22/10/2026 | En cours |
| T02 | Auditer et nettoyer les données | T01 | 2 h | À renseigner | Python, Pandas, notebook | 23/10/2026 | À faire |
| T03 | Séparer les données en trois parties | T02 | 1 h | À renseigner | Scikit-learn | 23/10/2026 | À faire |
| T04 | Transformer les textes avec TF-IDF | T03 | 1 h | À renseigner | TfidfVectorizer | 26/10/2026 | À faire |
| T05 | Entraîner les modèles de départ | T04 | 4 h | À renseigner | Scikit-learn, TensorFlow/Keras | 27/10/2026 | À faire |
| T06 | Rechercher les réglages avec KerasTuner | T05 | 3 h | À renseigner | KerasTuner | 28/10/2026 | À faire |
| T07 | Rechercher les réglages avec Optuna | T05 | 3 h | À renseigner | Optuna | 29/10/2026 | À faire |
| T08 | Évaluer et comparer les modèles | T06, T07 | 2 h | À renseigner | F1-score, Python | 30/10/2026 | À faire |
| T09 | Sauvegarder le modèle et les métriques | T08 | 1 h | À renseigner | Keras, joblib, JSON | 02/11/2026 | À faire |
| T10 | Développer l'API FastAPI | T09 | 3 h | À renseigner | FastAPI, Pydantic | 03/11/2026 | À faire |
| T11 | Écrire les tests automatiques | T10 | 2 h | À renseigner | Pytest | 04/11/2026 | À faire |
| T12 | Créer la barrière qualité | T09, T11 | 2 h | À renseigner | Python, config.yaml | 05/11/2026 | À faire |
| T13 | Construire l'image Docker | T12 | 3 h | À renseigner | Dockerfile, Docker | 06/11/2026 | À faire |
| T14 | Configurer GitHub Actions | T13 | 3 h | À renseigner | GitHub, YAML | 09/11/2026 | À faire |
| T15 | Créer le registre Azure | T14 | 1 h | À renseigner | Azure Container Registry | 10/11/2026 | À faire |
| T16 | Publier l'image dans le registre | T15 | 2 h | À renseigner | GitHub Actions, Azure | 10/11/2026 | À faire |
| T17 | Déployer l'API sur Azure | T16 | 3 h | À renseigner | Azure Container Apps | 11/11/2026 | À faire |
| T18 | Tester l'API publique | T17 | 2 h | À renseigner | Navigateur, API | 12/11/2026 | À faire |
| T19 | Tester une nouvelle version et le retour arrière | T18 | 2 h | À renseigner | Git, Azure CLI | 13/11/2026 | À faire |
| T20 | Vérifier les coûts et supprimer les ressources | T19 | 1 h | À renseigner | Portail Azure | 16/11/2026 | À faire |
| T21 | Finaliser le README et les preuves | T20 | 2 h | À renseigner | GitHub, captures d'écran | 17/11/2026 | À faire |

## Ressources humaines

- Moi-même : développement, tests, documentation et déploiement.
- Formateur : accompagnement si nécessaire.

## Ressources matérielles et techniques

- Ordinateur et connexion Internet.
- Python, VS Code, Jupyter Notebook, Git et GitHub.
- Scikit-learn, TensorFlow/Keras, KerasTuner, Optuna, FastAPI et Pytest.
- Docker, GitHub Actions, Azure CLI et Azure Container Apps.

## Ressources financières

- Compte Azure de formation, selon les quotas disponibles.
- Vérification des coûts avant et après le déploiement.
- Suppression des ressources créées pour le projet à la fin.

## Suivi du projet

- Mettre à jour le statut après chaque tâche.
- Renseigner la charge réelle après chaque session de travail.
- Conserver les preuves des tests et des déploiements.
- Respecter les dépendances entre les tâches.
