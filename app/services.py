import os
import requests
from dotenv import load_dotenv
from google import genai

SECRET_KEY = os.getenv("SECRET_KEY_env")
load_dotenv()
# --- Hugging Face
def get_Hugg(text_input : str):
    API_URL = os.getenv("API_URL_env")
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN_env']}",
    }
    # text_input = "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!"
    # text_input="Briefly, how AI works"
    payload = {
        "inputs": text_input,
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    }

    # def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()   
    # text_input=query()
    # return text_input

print("===== Hugging Face =====")
# print(get_Hugg())

# --- Gemini key
client = genai.Client(api_key=os.getenv("Gemini_Key_env"))

print("===Liste des modèles disponibles :===")
for model in client.models.list():
    # On affiche seulement les modèles "generateContent" (pour le texte)
    if "generateContent" in model.supported_actions:
        print(model.name)

def get_gemini_key(prompt : str):
    GEMINI_API_KEY = os.getenv("Gemini_Key_env")
    client = genai.Client(api_key=GEMINI_API_KEY)

    """full_prompt =f 
    Analyse le texte suivant : 
    {prompt}
    Donner moi un résumé concis.
"""    
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        # contents="briefly, how does AI work?"
        contents=prompt
    )
    return response.text
print("===== Gemini Key =====")
# print(response.text)
# print(get_gemini_key()) 

# --- ENPOINT : Analyze Text    
# ___ Categorize
# ___ Summarize