from fastapi import APIRouter
from _3Words.Models.UserModel import UserModel
from _3Words.Services import usersService
from _3Words.Services import tokenService
from _3Words.Models.responseModel import responseModel
router = APIRouter()

#region Login

@router.get("/authenticate")
async def login():
    return  responseModel(200 , "teste" , None)
    
#endregion

#region Register

@router.post("/step1")
async def saveUserEmailAndCellphone():
    user = UserModel(email="teste@teste.com" , cellphone="+5511990205678")
    usersService.insertUserEmailAndCellphone(user)
    return  responseModel(200 , "teste" , None)
    
@router.post("/step2")
async def sendAuthToken():
    tokenService.insertNewToken()
    return  responseModel(200 , "teste" , None)
    
@router.get("/step3")
async def validateAuthToken(userId:int , token:int):
    tokenService.validateToken(userId , token)
    return  responseModel(200 , "teste" , None)
    
@router.post("/step4")
async def saveUserInfo():
    user = UserModel.UserModel(name = "Lucas Pacheco" , surname= "Pacheco" , birthdate= "1995-06-29" , gender= "0" , postalCode= "01106010" )
    usersService.insertNewUserPassword(user)
    return  responseModel(200 , "teste" , None)
    
#endregion
