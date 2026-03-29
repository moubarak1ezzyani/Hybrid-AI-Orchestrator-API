from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session 
from sqlalchemy.ext.declarative import declarative_base
# from schema import UserAuth
from fastapi import FastAPI, Depends,HTTPException

load_dotenv()
# --- Declarations Variables
DB_USER = os.getenv("DB_USER_env")
DB_PASSWORD = os.getenv("DB_PASSWORD_env")
DB_ADDR = os.getenv("DB_ADDR_env")
DB_PORT = os.getenv("DB_PORT_env")
DB_NAME = os.getenv("DB_NAME_env")
DB_URL = os.getenv("DB_URL_env")

# --- DB SETUP
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
MyBase = declarative_base()

# --- Table : User
class UserDB(MyBase):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, unique=True, index=True)
    password =Column(String)

MyBase.metadata.create_all(bind=engine)

# --- Fonction db
def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()
 
 
""" def create_user(user : UserAuth):
    username =user.username
    password =user.password 
    return {"message" : "donnees prises"} """

def get_user(username : str, db : Session ):
    user_by_username = db.query(UserDB).filter(UserDB.username == username).first()
    return user_by_username

    # --- Add a user created to DB
def add_to_db(username : str, hashed_password : str, db : Session ):
    new_user_obj = UserDB(username=username, password =hashed_password )
    db.add(new_user_obj)
    db.commit()     # Sauvegarder
    return new_user_obj
