# FIN_DE_VIE.md - Plan de Décommissionnement

## Stratégie de fin de vie des composants

| Composant | Fin de vie Partielle | Fin de vie Totale (Suppression) | Ordre de suppression | Ce qu'on conserve | Coût estimé si laissé en place |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Application (Azure Container App)** | Arrêt temporaire du trafic (Scale to 0) | Suppression complète de l'instance ACA | 1 | Code source sur GitHub | Facturation à l'utilisation / ressources inactives |
| **Registre de conteneurs (ACR)** | Désactivation temporaire | Suppression du registre ACR (Basic) | 2 | Code Dockerfile et sources | Facturation journalière forfaitaire (coût fixe non négligeable) |
| **Images Docker** | Suppression des tags obsolètes sur ACR | Suppression définitive de l'image du registre | 3 | Historique Git | Stockage cloud |
| **Secrets & Identifiants** | Révocation des tokens d'accès | Suppression des secrets GitHub & Azure | 4 | Aucun | Risque de sécurité si compromis |
| **Dépôt GitHub** | Archivage en mode lecture seule | Suppression totale du dépôt distant | 5 | Sauvegarde locale éventuelle | Gratuit (Public/Private) |
| **Données & Modèles locaux** | Nettoyage du cache venv / build | Suppression locale du dossier `model/` et des données brutes | 6 | Code versionné | Gratuit (stockage local) |

---
*Note : Conformément aux consignes, la suppression totale des ressources Cloud (ACA et ACR) sera exécutée et prouvée (captures d'écran à l'appui) à la fin du projet pour éviter toute facturation inutile.*