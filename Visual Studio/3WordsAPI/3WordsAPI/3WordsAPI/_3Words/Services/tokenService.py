from random import randint
from _3Words.Data import tokenRepository
from _3Words.Data import usersRepository
from _3Words.Services import emailService

def generateNewToken():
    token = randint(10000 , 99999) 
    return token

def sendNewToken(userId:int , token:int):
    token = generateNewToken()
    tokenRepository.insertNewToken(token)
    #todo: envio do token por email
    emailTo:str = usersRepository.getUserById(userId).email
    emailService.sendEmail(emailTo , "Ur code is "+str(token))

def validateToken(userId:int , token:int):
    actualToken = tokenRepository.getTokenByUserId(userId)
    if token == actualToken:
        return True
    return False