# from database import UserDB
from pydantic import BaseModel
# from sqlalchemy import String, Integer

class UserAuth(BaseModel):
        username : str
        password : str

class AnalyzeText(BaseModel):
    text_input : str

class Token(BaseModel):
      access_token : str
      token_type : str

