from pydantic import BaseModel

class RequestWordsModel  (BaseModel):
    """description of class"""
    userId:int = None
    fromLanguage:str = None
    toLanguage:str = None
    subject:str = None
