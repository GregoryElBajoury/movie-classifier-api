FROM python:3.14-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Installation des dépendances système nécessaires si besoin
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie et installation des exigences depuis requirements-app.txt
COPY requirements-app.txt .
RUN pip install --no-cache-dir -r requirements-app.txt

# Copie du code source et des artéfacts du modèle
COPY main.py .
COPY model/ ./model/
COPY config.yaml .

# Exposition du port sur lequel tourne l'API FastAPI
EXPOSE 8000

# Commande pour lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]