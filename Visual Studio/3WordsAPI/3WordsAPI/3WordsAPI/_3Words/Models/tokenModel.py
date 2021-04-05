from pydantic import BaseModel
from datetime import datetime


class TokenModel(BaseModel):
    """description of class"""
    userId:int = None
    token:int = None
    dt_emailTokenExprirated:datetime = None

    def __init__(self, **kwargs):
        for key , value in kwargs.items():
            for attr in self.__dir__():
                if not attr.startswith("__"):
                    if key == attr:
                        setattr(self , key , value)


