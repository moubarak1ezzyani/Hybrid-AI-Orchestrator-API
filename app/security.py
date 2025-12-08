from dotenv import load_dotenv
import os
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
load_dotenv()
# --- Variables
SECRET_KEY = os.getenv("SECRET_KEY_env")
ALGO = os.getenv("ALGO_env")
minutes_expire_token = 30
password_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")    # bcrypt : algo de chiffrement | context vs hashage : couteau vs action de couper

# ---  Functions
def get_hash_password(password) -> str:
    hash_pwd=password_context.hash(password)
    return hash_pwd

def verify_password(password, hash_pwd) -> bool:
    return password_context.verify(password, hash_pwd)

def create_access_token(data : dict, exp_min : int = minutes_expire_token):
    to_encode = data.copy()
    exp_min = datetime.now(timezone.utc) + timedelta(minutes = minutes_expire_token)
    to_encode.update({"exp":exp_min})
    return jwt.encode(to_encode, SECRET_KEY, ALGO)

# def authenticate_user(username : str, password : str):
#     user = get_user(username)
#     if not user or not verify_password(password, user["hash_pwd"]):
#         return None
#     return user

