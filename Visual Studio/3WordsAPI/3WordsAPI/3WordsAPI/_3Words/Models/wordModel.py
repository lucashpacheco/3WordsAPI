from pydantic import BaseModel


class wordModel(BaseModel):
    """description of class"""
    id:int = None
    fromLanguage:str = None
    toLanguage:str = None
    word:str = None
    translatedWord:str = None
    file:bytes = None
