# 🧠 Hybrid AI Orchestrator API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![Coverage](https://img.shields.io/badge/Tests-Pytest%20%26%20Mocks-green)

> **Intelligent orchestration API chaining Zero-Shot Classification and Contextual Synthesis.**

## 🔗 Frontend Interface Link

This backend is the intelligence engine that powers the user dashboard:
👉 **[Access the Hybrid-Analysis-Dashboard](https://github.com/moubarak1ezzyani/Hybrid-Analysis-Dashboard.git)**

## 📖 Project Context

As part of the modernization of a **media monitoring** agency, this project aims to automate the analysis of news article feeds.

The **Hybrid AI Orchestrator API** is an AI orchestration platform that replaces costly manual processing with an automated pipeline. This backend acts as an intelligent orchestrator capable of:
1.  **Classifying** text without prior training (Zero-Shot Classification via Hugging Face).
2.  **Synthesizing** and analyzing the tone of the content by using the classification as context (via Google Gemini).

## 🏗 Architecture & Workflow

The backend exposes a secure RESTful API that manages the chaining of AI calls.

### 📂 Project Structure

```text
OrchestrationIA Fullstack-backend/
├── app/                  # Application Core (Business logic, Security, DB)
├── docs/                 # Technical documentation and resources
├── script/               # Utility scripts for the project
├── venv/                 # Python virtual environment (local)
├── .env                  # Environment variables (Sensitive - ignored by Git)
├── .gitignore            # Git exclusion configuration
├── docker-compose.yml    # Container orchestration (App + DB)
├── dockerfile            # Docker image configuration for the backend
├── main.py               # Main entry point for the FastAPI application
├── notes_backend.md      # Development logs and notes
├── README.md             # General repository documentation
└── requirements.txt      # List of Python libraries and dependencies
```

## 🛠️ Technical Stack

* **API Framework:** FastAPI (Python) for its native async support and high performance.
* **Database:** PostgreSQL via SQLAlchemy (ORM).
* **Authentication:** Full JWT (JSON Web Tokens) implementation with Bcrypt hashing (`passlib`).
* **AI Services:**
    * **Classification:** Hugging Face Inference API (`facebook/bart-large-mnli` model).
    * **Generation:** Google Generative AI (Gemini Flash).
* **Quality & Testing:** Pytest with a Mocking strategy to isolate external API calls.
* **DevOps:** Docker & Docker Compose.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10+
* PostgreSQL
* Docker (optional)

### 1. Clone the project

```bash
git clone [https://github.com/votre-user/Hybrid-Analyzer-Backend.git](https://github.com/votre-user/Hybrid-Analyzer-Backend.git)
cd Hybrid-Analyzer-Backend
```

### 2. Environment Variables (.env)

Create a `.env` file at the root. **Essential for security and API calls.**

```ini
# --- Database ---
DB_USER_env=postgres
DB_PASSWORD_env=admin
DB_ADDR_env=localhost
DB_PORT_env=5432
DB_NAME_env=orchestrator_db
DB_URL_env=postgresql://postgres:admin@localhost/orchestrator_db

# --- Security (JWT) ---
SECRET_KEY_env=your_super_secret_openssl_key
ALGO_env=HS256

# --- AI API Keys ---
# Hugging Face (Write Token)
HF_TOKEN_env=hf_xxxxxxxxxxxxxxxxxxxx
API_URL_env=[https://api-inference.huggingface.co/models/facebook/bart-large-mnli](https://api-inference.huggingface.co/models/facebook/bart-large-mnli)

# Google Gemini
Gemini_Key_env=AIzaSyxxxxxxxxxxxxxxxxxxxx
```

### 3. Install dependencies

```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:MyApp --reload
```

The API will be available at `http://localhost:8000`.
Swagger Documentation: `http://localhost:8000/docs`.

## 🐳 Running with Docker

To launch both the backend and the PostgreSQL database simultaneously:

```bash
docker-compose up --build
```

## 🔌 API Documentation

### Authentication

* **POST** `/Register`
    * Account creation. Automatic password hashing.
    * *Body:* `{"username": "admin", "password": "secure123"}`
* **POST** `/Login`
    * Retrieve Access Token.
    * *Body:* `{"username": "admin", "password": "secure123"}`
    * *Response:* `{"access token": "eyJhbGci...", "type": "bearer"}`

### AI Orchestration (Protected)

* **POST** `/AnalyzeText`
    * *Header:* `Authorization: Bearer <token>`
    * *Body:* `{"text_input": "The stock market crashed following..."}`
    * *Process:*
      1.  Sent to **Hugging Face** for categorization.
      2.  Injection of the received category into the **Gemini** prompt.
      3.  Generation of the summary and sentiment analysis.
    * *Response Example:*
      ```json
      {
        "original text": "...",
        "result_hugg": { "labels": ["Finance"], "scores": [0.98] },
        "result gemini": "Summary: Following the announcement... \nTone: Negative"
      }
      ```

## 🧪 Unit Tests

The project includes unit tests validating the processing chain and mocking external APIs (so no AI credits are consumed during testing).

```bash
# Run tests
pytest tests/
```
