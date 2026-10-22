# Procédure de mise en production

## 1. Déclencheur (Trigger)
- Modification du code source ou du modèle et validation locale.
- Envoi (*push*) des modifications sur la branche principale du dépôt GitHub.

## 2. Vérifications et Pipeline CI/CD (Tests & Barrière qualité)
- Lancement automatique du workflow GitHub Actions (`test` et `image`).
- Vérification du respect des seuils de performance (barrière qualité via `metrics.json`)[cite: 2].
- Construction et validation de l'image conteneurisée[cite: 2].

## 3. Rôles et Responsabilités
- **Qui décide :** L'ingénieur (validation des tests verts et de la conformité du modèle).
- **Qui exécute :** Le déploiement est réalisé manuellement par l'ingénieur sur Azure Container Apps en raison des restrictions des droits Contributeur (utilisation des identifiants administrateur du registre ACR)[cite: 2].

## 4. Déploiement et Contrôle
- Récupération de l'identifiant unique du commit (`git rev-parse HEAD`).
- Mise à jour de l'application sur Azure Container Apps pointant vers l'image étiquetée avec cet identifiant.
- Contrôle de bon fonctionnement via la route `/health` (vérification de la version du commit) et test de la route `/predict`[cite: 2].

## 5. Procédure de Retour Arrière (Rollback)
- **Condition :** En cas d'anomalie détectée en production sur la nouvelle version.
- **Mode opératoire :** Redéploiement manuel de l'image correspondant à l'identifiant du commit précédent stable sur Azure Container Apps.

---

## Journal des versions

| Date | Identifiant du commit | Changement / Évolution | Résultat |
| :--- | :--- | :--- | :--- |
| JJ/MM/AAAA | `abcdef0` | Version initiale de l'API de classification (Horreur / Comédie) | Déploiement réussi, `/health` ok[cite: 2] |
| JJ/MM/AAAA | `1234567` | Ajout de la route `/hello`[cite: 2] | Déploiement réussi, route accessible |
| JJ/MM/AAAA | `abcdef0` | *Rollback* vers la version précédente suite au test de retour arrière[cite: 2] | Restauration de l'ancienne version, route `/hello` supprimée |