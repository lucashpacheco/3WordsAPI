from _3Words.Data import dataUtils as db
from _3Words.Models.UserModel import UserModel
from _3Words.Models.loginModel import LoginModel

import typing
import datetime

def getUserIdbyEmail(email:str) -> int:
    userid:int = db.select("SELECT pk_IdUser FROM tbUser WHERE userEmail = ? " , (email)) #todo: pega user pelo id
    return userid


def getUserById(id:int) -> UserModel:
    user = db.select("SELECT * FROM tbUser WHERE pk_IdUser = ? " , (id)) #todo: pega user pelo id
    return user

def getUserPassword(id:int) -> str:
    password:str = db.select("SELECT userPassword FROM tbLogin WHERE fk_IdUser = ? " , (id)) #todo: pega senha pelo id
    return password

def insertUserEmailAndCellphone(user:UserModel):
    db.insert("INSERT INTO tbUser (userEmail, userCellphone, isActive) VALUES  (? , ? , 0)" , (user.email , user.cellphone)) #todo: insere o email para o novo usuario

def updateUserInfo(user:UserModel):# , userName:str , userSurname:str , userBirthDate:datetime , userGender:int , userPostalCode:int , idUser:int):
    db.update("UPDATE tbUser SET userName = ? , userSurname = ? , dt_userBithdate = ?  , userGender = ? , userPostalCode = ?  WHERE pk_IdUser = ?" , (user.name , user.surname , user.birthdate , user.gender , user.postalCode , user.id)) #todo: atualiza as informações referentes ao usuario(nome , dt nasc , postal code ...)

def insertNewUserPassword(login:LoginModel):
    db.insert("INSERT INTO tbLogin (fk_IdUser ,userPassword , isActive) VALUES  (? ,? , 1 )" , login.userId , login.password) #todo: insere senha para novo usuario no cadastro

