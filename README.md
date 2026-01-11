# 🧠 Hybrid AI Orchestrator API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![Coverage](https://img.shields.io/badge/Tests-Pytest%20%26%20Mocks-green)

> **API d'orchestration intelligente chaînant la Classification Zero-Shot et la Synthèse Contextuelle.**

## 🔗 Lien vers l'Interface (Frontend)
Ce backend est le moteur d'intelligence qui alimente le tableau de bord utilisateur :
👉 **[Accéder au Hybrid-Analysis-Dashboard](https://github.com/moubarak1ezzyani/Hybrid-Analysis-Dashboard.git)**

## 📖 Contexte du Projet

Dans le cadre de la modernisation d'une agence de **media monitoring**, ce projet vise à automatiser l'analyse de flux d'articles de presse.

**Hybrid AI Orchestrator API** est une plateforme d'orchestration IA qui remplace le traitement manuel coûteux par un pipeline automatisé. Ce backend agit comme un chef d'orchestre intelligent capable de :
1.  **Classifier** un texte sans entraînement préalable (Zero-Shot Classification via Hugging Face).
2.  **Synthétiser** et analyser la tonalité du contenu en utilisant la classification comme contexte (via Google Gemini).

## 🏗 Architecture & Workflow

Le backend expose une API RESTful sécurisée qui gère le chaînage des appels IA.

### 📂 Structure du Projet

```text
OrchestrationIA Fullstack-backend/
├── app/                  # Cœur de l'application (Logique métier, Sécurité, DB)
├── docs/                 # Documentation technique et ressources
├── script/               # Scripts utilitaires pour le projet
├── venv/                 # Environnement virtuel Python (local)
├── .env                  # Variables d'environnement (Sensible - non versionné)
├── .gitignore            # Configuration des exclusions Git
├── docker-compose.yml    # Orchestration des conteneurs (App + DB)
├── dockerfile            # Configuration de l'image Docker du backend
├── main.py               # Point d'entrée principal de l'API FastAPI
├── notes_backend.md      # Journal de bord et notes de développement
├── README.md             # Documentation générale du dépôt
└── requirements.txt      # Liste des bibliothèques et dépendances Python
```

## 🛠️ Stack Technique

  * **Framework API :** FastAPI (Python) pour sa gestion native de l'asynchronisme et sa rapidité.
  * **Base de Données :** PostgreSQL via SQLAlchemy (ORM).
  * **Authentification :** Implémentation complète JWT (JSON Web Tokens) avec hashage Bcrypt (`passlib`).
  * **Services IA :**
      * **Classification :** API Inference Hugging Face (Modèle `facebook/bart-large-mnli`).
      * **Génération :** Google Generative AI (Gemini Flash).
  * **Qualité & Tests :** Pytest avec stratégie de Mocking pour isoler les appels API externes.
  * **DevOps :** Docker & Docker Compose.

## ⚙️ Installation et Configuration

### Prérequis

  * Python 3.10+
  * PostgreSQL
  * Docker (optionnel)

### 1\. Cloner le projet

```bash
git clone [https://github.com/votre-user/Hybrid-Analyzer-Backend.git](https://github.com/votre-user/Hybrid-Analyzer-Backend.git)
cd Hybrid-Analyzer-Backend
```

### 2\. Variables d'Environnement (.env)

Créez un fichier `.env` à la racine. **Indispensable pour la sécurité et les appels API.**

```ini
# --- Database ---
DB_USER_env=postgres
DB_PASSWORD_env=admin
DB_ADDR_env=localhost
DB_PORT_env=5432
DB_NAME_env=orchestrator_db
DB_URL_env=postgresql://postgres:admin@localhost/orchestrator_db

# --- Sécurité (JWT) ---
SECRET_KEY_env=votre_cle_super_secrete_openssl
ALGO_env=HS256

# --- API Keys IA ---
# Hugging Face (Write Token)
HF_TOKEN_env=hf_xxxxxxxxxxxxxxxxxxxx
API_URL_env=[https://api-inference.huggingface.co/models/facebook/bart-large-mnli](https://api-inference.huggingface.co/models/facebook/bart-large-mnli)

# Google Gemini
Gemini_Key_env=AIzaSyxxxxxxxxxxxxxxxxxxxx
```

### 3\. Installation des dépendances

```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

### 4\. Lancement

```bash
uvicorn main:MyApp --reload
```

L'API est accessible sur `http://localhost:8000`.
Documentation Swagger : `http://localhost:8000/docs`.

## 🐳 Lancement via Docker

Pour lancer le backend et la base de données PostgreSQL simultanément :

```bash
docker-compose up --build
```

## 🔌 Documentation API

### Authentification

  * **POST** `/Register`
      * Création de compte. Hashage automatique du mot de passe.
      * *Body :* `{"username": "admin", "password": "secure123"}`
  * **POST** `/Login`
      * Récupération du Token d'accès.
      * *Body :* `{"username": "admin", "password": "secure123"}`
      * *Response :* `{"access token": "eyJhbGci...", "type": "bearer"}`

### Orchestration IA (Protégé)

  * **POST** `/AnalyzeText`
      * *Header :* `Authorization: Bearer <token>`
      * *Body :* `{"text_input": "Le marché boursier a chuté suite..."}`
      * *Processus :*
        1.  Envoi à **Hugging Face** pour catégorisation.
        2.  Injection de la catégorie reçue dans le prompt **Gemini**.
        3.  Génération du résumé et analyse de sentiment.
      * *Response Example :*
        ```json
        {
          "original text": "...",
          "result_hugg": { "labels": ["Finance"], "scores": [0.98] },
          "result gemini": "Résumé : Suite à l'annonce... \nTonalité : Négative"
        }
        ```

## 🧪 Tests Unitaires

Le projet inclut des tests unitaires validant la chaîne de traitement et mockant les API externes (pour ne pas consommer de crédits IA lors des tests).

```bash
# Lancer les tests
pytest tests/
```

