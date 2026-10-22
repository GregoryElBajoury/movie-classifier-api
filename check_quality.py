import json
import yaml
import sys
import os

def check_quality():
    config_path = "config.yaml"
    metrics_path = "model/metrics.json"

    if not os.path.exists(config_path) or not os.path.exists(metrics_path):
        print(" Erreur : Fichier config.yaml ou model/metrics.json introuvable.")
        sys.exit(1)

    # Chargement de la configuration
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Chargement des métriques du modèle
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    min_f1 = config.get("min_f1", 0.0)
    min_test_size = config.get("min_test_size", 0)

    # Utilisation des clés exactes du metrics.json : f1_test et taille_test
    model_f1 = metrics.get("f1_test", 0.0)
    test_size = metrics.get("taille_test", 0)

    print(f" Analyse de la qualité du modèle :")
    print(f"   - F1-score mesuré : {model_f1:.4f} (Seuil requis : >= {min_f1})")
    print(f"   - Taille de test : {test_size} (Seuil requis : >= {min_test_size})")

    # Barrière qualité
    if model_f1 < min_f1 or test_size < min_test_size:
        print(" ÉCHEC DE LA BARRIÈRE QUALITÉ : Le modèle ne respecte pas les critères exigés.")
        sys.exit(1)
    else:
        print(" SUCCÈS : Le modèle valide tous les critères de qualité !")
        sys.exit(0)

if __name__ == "__main__":
    check_quality()