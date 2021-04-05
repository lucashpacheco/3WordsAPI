from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from _3Words.Models.UserModel import UserModel
from _3Words.Services import usersService
from _3Words.Services import tokenService
from _3Words.Models.responseModel import ResponseModel
from _3Words.Models.tokenModel import TokenModel
from _3Words.Models.loginModel import LoginModel
from fastapi.encoders import jsonable_encoder


router = APIRouter()

#region Login e Logout
#region Login e Logout

@router.get("/authenticate")
async def login(loginPack:LoginModel) -> ResponseModel:
    try:
        if usersService.login(loginPack):
            return  ResponseModel(200 , "teste" , None)
        return  ResponseModel(301 , "teste" , None)
    except :
        return  ResponseModel(302 , "teste" , None)

@router.get("/logout")
async def logout() -> ResponseModel:
    try:
        if usersService.logout():
            return  ResponseModel(200 , "teste" , None)
        return  ResponseModel(301 , "teste" , None)
    except :
        return  ResponseModel(302 , "teste" , None)
    
    
#endregion

#region Register
#region Register

@router.post("/step1")
async def saveUserEmailAndCellphone(user:UserModel) -> ResponseModel:
    try:
        # user = UserModel(email="teste@teste.com" , cellphone="+5511990205678")
        user =  jsonable_encoder(user)
        usersService.insertUserEmailAndCellphone(user.dict())
        return  ResponseModel(200 , "teste" , None)
    except :
        return  ResponseModel(500 , "teste" , None)
    
    
@router.post("/step2")
async def validateAuthToken(token:TokenModel) -> ResponseModel:
    try:
        token =  jsonable_encoder(token)
        if tokenService.validateToken(token.userId , token.token):
            return  ResponseModel(200 , "teste" , None)
        return  ResponseModel(505 , "teste" , None)
    except :
        return  ResponseModel(501 , "teste" , None)

@router.post("/step3")
async def saveUserInfo(user:UserModel) -> ResponseModel:
    try:
        # user = UserModel.UserModel(name = "Lucas Pacheco" , surname= "Pacheco" , birthdate= "1995-06-29" , gender= "0" , postalCode= "01106010" )
        user =  jsonable_encoder(user)
        usersService.insertUserInfo(user.dict())
        return  ResponseModel(200 , "teste" , None)
    except :
        return  ResponseModel(502 , "teste" , None)
    
@router.post("/step4")
async def saveNewPassword(user:UserModel) -> ResponseModel:
    try:
        # user = UserModel.UserModel(password = "123" , userId = 1 )
        user =  jsonable_encoder(user)
        usersService.insertNewUserPassword(user.dict())
        return  ResponseModel(200 , "teste" , None)
    except :
        return  ResponseModel(502 , "teste" , None)
    
@router.post("/resendtoken")
async def sendAuthToken(token:TokenModel) -> ResponseModel:
    try:
        token =  jsonable_encoder(token)
        tokenService.sendNewToken(token.userId , token.token)
        return  ResponseModel(200 , "teste" , None)
    except :
        return  ResponseModel(503 , "teste" , None)
    
#endregion
