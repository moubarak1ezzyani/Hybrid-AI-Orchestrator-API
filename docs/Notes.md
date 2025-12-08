| Action        | Analogie                       | Explication technique                  |
| ------------- | ------------------------------ | -------------------------------------- |
| **Encodage**  | Le cinéma crée un ticket signé | header + payload → Base64 + signature  |
| **Décodage**  | L’agent vérifie le ticket      | serveur vérifie signature + expiration |
| **Signature** | Cachet officiel                | HMAC-SHA256 avec secret                |
| **Payload**   | Infos du ticket                | données utilisateur                    |


---
| ✅ PARFAIT POUR... | ❌ À ÉVITER SI... | | :--- | :--- | | Projets React, Vue, Next.js | Traitement vidéo lourd | | Portfolios & E-commerce | Websockets (Chat temps réel long) | | Startups (MVP) | Bases de données complexes intégrées |