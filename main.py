import os
from services import get_Hugg, get_gemini_key
from database import UserDB, get_user, add_to_db, get_db
from schema import UserAuth, AnalyzeText
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import sessionmaker, Session 
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from security import get_hash_password, verify_password, create_access_token

# --- ENDPOINTS
MyApp = FastAPI()

@MyApp.get('/home')
def get_home():
    return {"Message" : "Hello World"}

@MyApp.post('/Register')
def sign_up(user : UserAuth, db : Session = Depends(get_db)):
    existing_user =  get_user(user.username, db)
    # SELECT * FROM user where username == username LIMIT 1
    if existing_user:
        raise HTTPException(status_code=409, detail="utilsateeur deja pris")
    
    hash_pwd = get_hash_password(user.password)
    
    if not verify_password(user.password, hash_pwd):
        raise ValueError("Mot de passe est incorrect")
    
    add_to_db(username=user.username, hashed_password=hash_pwd, db=db)
    return {"message" : "Utilsateur cree avec succes", "username" : user.username}

@MyApp.post('/Login')
def sign_in(user : UserAuth, db : Session = Depends(get_db)):
    db_user = get_user(user.username, db)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Utilisateur Inconnu'
        )
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Mot de passe incorrect"
        )
    access_token=create_access_token(data={"sub" : db_user.username})
    return {"acces token" : access_token, "type": "bearer"}
    

@MyApp.post('/AnalyzeText')
def AnalyzeText_Gemini(text_req: AnalyzeText):
    
    text_to_analyze = text_req.text_input
    try:
        # Import model Hugg Face
        hf_output=get_Hugg(text_to_analyze)
        if "error" in hf_output:
            raise HTTPException(status_code=503, detail=f"Erreur dans HF : {hf_output}")
        
        # --- Import model Gemini key
        text_gemini=str(hf_output)
        output_gemini=get_gemini_key(text_gemini)

        # --- OUPUT
        return {
            "original text" : text_to_analyze,
            "result_hugg" : hf_output,
            "result gemini" : output_gemini
        } 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
