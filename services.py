import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
# Hugging Face
def get_Hugg():
    API_URL = os.getenv("API_URL_env")
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN_env']}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    })
    return output
print("===== Hugging Face =====")
print(get_Hugg())

# Gemini key
def get_gemini_key():
    GEMINI_API_KEY = os.getenv("Gemini_Key_env")
    client = genai.Client(api_key=GEMINI_API_KEY)
    global response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="How does AI work?"
    )
print("===== Gemini Key =====")
print(response.text)
