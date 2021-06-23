from random import randint
from _3Words.Data import tokenRepository
from _3Words.Data import usersRepository
from _3Words.Services import emailService
from _3Words.Models.tokenModel import TokenModel

def generateNewToken():
    token = randint(10000 , 99999) 
    return token

def sendNewToken(userId:int):
    tokenObj = TokenModel()
    tokenObj.token = generateNewToken()
    tokenObj.userId = userId
    #todo: montar obj TokenModel
    
    tokenRepository.insertNewToken(tokenObj)
    emailTo:str = usersRepository.getUserById(userId).email
    emailService.sendEmail(emailTo , "Ur code is "+str(token))

def validateToken(tokenModel:TokenModel):
    actualToken = tokenRepository.getTokenByUserId(userId)
    if token == actualToken:
        return True
    return False