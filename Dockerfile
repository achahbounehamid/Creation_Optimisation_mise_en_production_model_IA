# Utiliser une image officielle Python légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source de l'API, la config et le dossier des artefacts
COPY app.py config.yaml ./
COPY model/ ./model/

# Exposer le port sur lequel l'API va tourner
EXPOSE 8000

# Commande pour lancer l'application au démarrage du conteneur
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]