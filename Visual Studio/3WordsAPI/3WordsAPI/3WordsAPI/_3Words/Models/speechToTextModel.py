from pydantic import BaseModel

class speechToTextModel(BaseModel):
    """description of class"""
    id:int = None
    file:bytes = None
    word:str = None



