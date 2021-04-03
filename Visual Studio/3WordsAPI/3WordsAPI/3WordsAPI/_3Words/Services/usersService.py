from _3Words.Models.UserModel import UserModel
from _3Words.Data import usersRepository
from _3Words.Services import tokenService
from random import randint


def insertUserEmailAndCellphone(user:UserModel):
    usersRepository.insertUserEmailAndCellphone(user)
    idUser:int = usersRepository.getUserIdbyEmail(user.email)
    tokenService.insertNewToken(idUser)

def insertUserInfo(user:UserModel):
    usersRepository.updateUserInfo(user)
    return None

def insertNewUserPassword(idUser:int , password:str):
    usersRepository.insertNewUserPassword(idUser , password)

def createToken():
    token = randint(10000 , 99999) 
    return token