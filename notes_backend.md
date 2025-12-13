### Explications rapides des dépendances :

  * **`fastapi` & `uvicorn`** : Pour créer l'API et lancer le serveur.
  * **`sqlalchemy` & `psycopg2-binary`** : Pour gérer la base de données PostgreSQL.
  * **`python-dotenv`** : Pour lire votre fichier `.env`.
  * **`requests`** : Pour appeler l'API Hugging Face.
  * **`python-jose[cryptography]`** : Pour générer et décoder les tokens JWT (sécurité).
  * **`passlib[bcrypt]`** : Pour hacher les mots de passe (sécurité).
  * **`google-genai`** : C'est la bibliothèque officielle requise pour la ligne de code `client = genai.Client(...)` (attention, ne pas confondre avec l'ancienne `google-generativeai`).
  * **`python-multipart`** : Souvent requis par FastAPI pour gérer l'authentification et les formulaires.