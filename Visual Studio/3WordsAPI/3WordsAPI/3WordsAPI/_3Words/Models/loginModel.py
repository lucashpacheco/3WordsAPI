from pydantic import BaseModel

class LoginModel  (BaseModel):
    """description of class"""
    userId:int = None
    email:str = None
    password:str = None
    isActive:bool = None

    #def __init__(self, **kwargs):
    #    for key , value in kwargs.items():
    #        for attr in self.__dir__():
    #            if not attr.startswith("__"):
    #                if key == attr:
    #                    setattr(self , key , value)


