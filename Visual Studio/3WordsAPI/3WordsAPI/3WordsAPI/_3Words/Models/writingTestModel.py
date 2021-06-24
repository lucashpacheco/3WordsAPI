from pydantic import BaseModel

class writingTestModel(BaseModel):
    """description of class"""
    id:int = None
    word:str = None
    typedWord:str = None
    #match:bool = false

