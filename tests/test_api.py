from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data

def test_predict_valid():
    # Résumé valide de plus de 10 caractères
    response = client.post("/predict", json={"text": "Un groupe d'amis se retrouve dans une cabane isolée au milieu de la forêt."})
    assert response.status_code == 200
    data = response.json()
    assert "classe" in data
    assert "probabilite" in data
    assert data["classe"] in ["horreur", "comedie"]

def test_predict_too_short():
    # Résumé trop court (moins de 10 caractères)
    response = client.post("/predict", json={"text": "Court"})
    assert response.status_code in [400, 422]

def test_predict_empty():
    # Résumé vide
    response = client.post("/predict", json={"text": ""})
    assert response.status_code in [400, 422]