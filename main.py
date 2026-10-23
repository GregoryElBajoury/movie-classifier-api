import json
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import joblib
from tensorflow.keras.models import load_model

app = FastAPI(
    title="Classifieur de résumés de films",
    description="API de classification de films (Horreur ou Comédie)",
    version="1.0.0",
)

# Chargement unique des artéfacts au démarrage du serveur
try:
    with open("model/metrics.json", "r", encoding="utf-8") as f:
        metrics = json.load(f)
    # On récupère "version_modele" (qui vaut "1.0.0" d'après ton fichier)
    model_version = metrics.get("version_modele", metrics.get("version", "0.1.0"))
except Exception:
    model_version = "0.1.0"

# Chargement du modèle et du vectoriseur TF-IDF
model = load_model("model/model.keras")
vectorizer = joblib.load("model/vectoriseur.joblib")

class MovieInput(BaseModel):
    text: str = Field(..., min_length=10, description="Résumé du film (minimum 10 caractères)")

@app.get("/hello")
def hello():
    return {"message": "hello depuis la version déployée sur Azure"}

@app.get("/health")
def health_check():
    return {"status": "ok", "version": model_version}

@app.post("/predict")
def predict_movie(input_data: MovieInput):
    text = input_data.text.strip()
    
    if not text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le texte du résumé ne peut pas être vide."
        )
    
    if len(text) < 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le résumé est trop court (minimum 10 caractères requis)."
        )


    
    # Transformation TF-IDF et prédiction
    X_vec = vectorizer.transform([text])
    prediction = model.predict(X_vec.toarray())
    probability = float(prediction[0][0])
    
    if probability >= 0.5:
        predicted_class = "horreur"
        confidence = probability
    else:
        predicted_class = "comedie"
        confidence = 1.0 - probability

    return {
        "classe": predicted_class,
        "probabilite": round(confidence, 4),
        "version": model_version
    }