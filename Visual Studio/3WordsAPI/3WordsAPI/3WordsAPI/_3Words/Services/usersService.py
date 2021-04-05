from _3Words.Models.UserModel import UserModel
from _3Words.Data import usersRepository
from _3Words.Services import tokenService
from random import randint
from _3Words.Models.loginModel import LoginModel

#region Login e Logout

def validateUser(loginPack:LoginModel) -> bool:
    userId:int = usersRepository.getUserIdbyEmail(loginPack.email)
    password:str = usersRepository.getUserPassword(userId)
    if password == loginPack.password:
        return True
    return False

def login(loginPack:LoginModel) -> bool:
    if validateUser(loginPack):
        #todo: atualiza data de login e flag isLogged
        return True

def logout(userId:int) -> bool:
    #todo: atualiza flag isLogged
    return True

#endregion

#region Register

def insertUserEmailAndCellphone(user:UserModel):
    usersRepository.insertUserEmailAndCellphone(user)
    idUser:int = usersRepository.getUserIdbyEmail(user.email)
    tokenService.sendNewToken(idUser)

def insertUserInfo(user:UserModel):
    usersRepository.updateUserInfo(user)


def insertNewUserPassword(idUser:int , password:str):
    usersRepository.insertNewUserPassword(idUser , password)

#endregion
