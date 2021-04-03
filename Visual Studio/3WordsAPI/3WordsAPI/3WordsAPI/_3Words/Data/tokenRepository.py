import typing
import datetime

def getTokenByUserId(userId:int) -> int:
    token:int = db.select("") #todo: pega token do user pelo id do user
    return token


def insertNewToken(id:int , token:int):
    user = db.insert("") #todo: salva o novo token
    
