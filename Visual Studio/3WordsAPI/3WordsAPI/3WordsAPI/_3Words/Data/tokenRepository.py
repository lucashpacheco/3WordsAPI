import typing
import datetime

def getTokenByUserId(userId:int) -> int:
    token:int = db.select("SELECT emailToken FROM tbToken WHERE fk_IdUser = ? AND dt_emailTokenExprirated > GETDATE()" , userId) 
    return token


def insertNewToken(id:int , token:int):
    user = db.insert("INSERT INTO tbToken (fk_IdUser ,emailToken) VALUES (? ,?)" , id , token)
    
