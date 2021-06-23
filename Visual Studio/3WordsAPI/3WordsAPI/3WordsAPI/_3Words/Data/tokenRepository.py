import typing
import datetime
from _3Words.Data import dataUtils as db
from _3Words.Models.tokenModel import TokenModel

def getTokenByUserId(userId:int) -> int:
    token:int = db.select("SELECT emailToken FROM tbToken WHERE fk_IdUser = ? AND dt_emailTokenExprirated > GETDATE()" , userId).fetchone()[0] 
    return token


def insertNewToken(token:TokenModel):
    user = db.insert("INSERT INTO tbToken (fk_IdUser ,emailToken) VALUES (? ,?)", token)
    
