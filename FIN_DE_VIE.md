# Plan de fin de vie des composants

## 1. Distinction Fin de Vie Partielle vs Totale
- **Fin de vie partielle :** Arrêt temporaire ou suppression de certains services en cours d'itération (ex: arrêt d'un conteneur local, suppression d'une image de test obsolète sur le registre).
- **Fin de vie totale :** Clôture définitive du projet, suppression de toutes les ressources Cloud payantes ou consommatrices de stockage, et archivage du code.

## 2. Analyse par composant
Pour chaque composant, voici les modalités de suppression, l'ordre à respecter, et ce qui est conservé :

| Composant | Quand le retirer ? | Comment et dans quel ordre ? | Ce qu'on garde | Coût de l'inaction (si laissé en place) |
| :--- | :--- | :--- | :--- | :--- |
| **Application (Azure Container Apps)** | Fin de la démonstration / projet | 1er : Supprimer en premier via le portail Azure ou CLI pour stopper la facturation du calcul[cite: 2]. | Rien (le code reste dans le dépôt) | Consommation continue de ressources CPU/RAM et frais d'hébergement. |
| **Registre de conteneurs (Azure ACR)** | Fin du projet | 2e : Supprimer le registre une fois l'application supprimée (attention à ne pas supprimer le groupe de ressources partagé)[cite: 2]. | Les fichiers sources Dockerfile en local/GitHub | Facturation journalière du stockage de l'image (offre Basic)[cite: 2]. |
| **Secrets GitHub** | Fin du projet | 3e : Supprimer les identifiants ACR des paramètres du dépôt GitHub. | Aucun | Risque de sécurité résiduel si le dépôt devenait public. |
| **Image Docker locale** | Nettoyage régulier | Via commande `docker rmi` sur le poste de travail. | Le `Dockerfile` et les scripts sources[cite: 2]. | Occupation inutile de l'espace disque local. |
| **Modèle et artefacts (`model/`)** | Archivage long terme | Conservés sur le dépôt Git, supprimés du disque de travail si besoin. | `model.keras`, `metrics.json`, `vectoriseur.joblib`[cite: 2]. | Aucun coût direct (stockage Git gratuit). |
| **Données (CSV bruts / test)** | Fin du projet | Supprimées des environnements de travail non sécurisés. | Les scripts de traitement[cite: 2]. | Risque de non-conformité RGPD / confidentialité des données si sensibles. |
| **Dépôt GitHub** | Clôture définitive | Archivage du dépôt (mode Read-Only) ou suppression totale. | L'historique des commits et la documentation (README)[cite: 2]. | Aucun coût (dépôt public/privé gratuit). |

## 3. Preuve de la suppression
- Joindre une capture d'écran montrant le groupe de ressources Azure nettoyé ou l'absence de services actifs pour prouver l'application de la fin de vie totale[cite: 1, 2].