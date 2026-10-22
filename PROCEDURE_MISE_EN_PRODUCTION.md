# PROCEDURE_MISE_EN_PRODUCTION.md

## 1. Cycle de mise en production

* **Déclencheur** : Validation de la Pull Request sur la branche `main` avec succès des jobs CI (tests automatiques et barrière qualité).
* **Vérifications préalables** :
  * Exécution locale ou par le robot des tests `pytest`.
  * Vérification du respect des seuils de performance du modèle Deep Learning optimisé (provenant de la phase d'entraînement du notebook) dans `metrics.json` via le script de barrière qualité.
* **Déploiement** :
  * Construction et envoi de l'image Docker sur l'Azure Container Registry (ACR) étiquetée avec l'identifiant unique du commit (`git rev-parse HEAD`).
  * Mise à jour manuelle de l'Azure Container App (ACA) pointant vers la nouvelle image tagguée.
* **Contrôle post-déploiement** :
  * Test des endpoints `/health` (vérification de la version du commit) et `/predict` sur l'adresse publique.
* **Conditions et mode de retour arrière (Rollback)** :
  * *Condition* : Échec des tests de santé ou comportement inattendu en production.
  * *Mode* : Redéploiement immédiat de l'ancienne image étiquetée avec l'identifiant du commit précédent via la commande Azure Container Apps.
* **Rôles** :
  * *Qui décide* : Le Data/DevOps Engineer.
  * *Qui exécute* : Le Data/DevOps Engineer.

---

## 2. Journal des versions

| Date | Identifiant du Commit | Description du Changement | Résultat / Statut |
| :--- | :--- | :--- | :--- |
| 22/10/2026 | `d138fe0` | feat: fin de la phase notebook et ajout du gitignore propre. | Déployé / Stable |
| 22/10/2026 | `e1a1139` | Initial commit : structure du projet, documentation et intégration du pipeline de synthèse/notebook. | Déployé / Stable |







