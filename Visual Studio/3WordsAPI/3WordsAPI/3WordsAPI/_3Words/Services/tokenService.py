from random import randint
from _3Words.Data import tokenRepository

def generateNewToken():
    token = randint(10000 , 99999) 
    return token

def insertNewToken(userId:int , token:int):
    token = generateNewToken()
    tokenRepository.insertNewToken(token)

def validateToken(userId:int , token:int):
    actualToken = tokenRepository.getTokenByUserId(userId)
    if token == actualToken:
        return True
    return False