from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    """User Model contains user properties"""

    id:int = None
    name:str = None
    surname:str = None
    birthdate:datetime = None
    email:str = None
    cellphone:int = None
    gender:int = None
    postalCode:int = None
    isActive:bool = None

    def __init__(self, **kwargs):
        for key , value in kwargs.items():
            for attr in self.__dir__():
                if not attr.startswith("__"):
                    if key == attr:
                        setattr(self , key , value)
