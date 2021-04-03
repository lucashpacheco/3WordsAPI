from fastapi import APIRouter
from _3Words.Models.UserModel import UserModel
from _3Words.Services import usersService
from _3Words.Services import tokenService
from _3Words.Models.responseModel import responseModel

router = APIRouter()

#region Login

@router.get("/authenticate")
async def login():
    try:
        #todo: mecanismo de login
        return  responseModel(200 , "teste" , None)
    except :
        return  responseModel(300 , "teste" , None)

    
#endregion

#region Register

@router.post("/step1")
async def saveUserEmailAndCellphone():
    try:
        user = UserModel(email="teste@teste.com" , cellphone="+5511990205678")
        usersService.insertUserEmailAndCellphone(user)
        return  responseModel(200 , "teste" , None)
    except :
        return  responseModel(500 , "teste" , None)
    
    
@router.get("/step2")
async def validateAuthToken(userId:int , token:int):
    try:
        if tokenService.validateToken(userId , token):
            return  responseModel(200 , "teste" , None)
        return  responseModel(505 , "teste" , None)
    except :
        return  responseModel(501 , "teste" , None)

@router.post("/step3")
async def saveUserInfo():
    try:
        user = UserModel.UserModel(name = "Lucas Pacheco" , surname= "Pacheco" , birthdate= "1995-06-29" , gender= "0" , postalCode= "01106010" )
        usersService.insertNewUserPassword(user)
        return  responseModel(200 , "teste" , None)
    except :
        return  responseModel(502 , "teste" , None)
    
    

@router.post("/resendtoken")
async def sendAuthToken():
    try:
        tokenService.sendNewToken()
        return  responseModel(200 , "teste" , None)
    except :
        return  responseModel(503 , "teste" , None)
    
#endregion
