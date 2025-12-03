import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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

class User(MyBase):
    __tablename__ = "users"
    id=Column(String, primary_key=True, index=True)
    username=Column(String, unique=True, index=True)
    hashedpassword = Column(String)

MyBase.metadata.create_all(bind=engine)

def get_db(MyBase):
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()

