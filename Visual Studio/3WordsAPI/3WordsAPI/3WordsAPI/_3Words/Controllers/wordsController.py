from fastapi import APIRouter
from _3Words.Services import wordsService
from _3Words.Models.responseModel import responseModel


router = APIRouter()

@router.get("/words")
async def defaultWords():
    words = wordsService.wordsPackMaker()
    words = words
    return responseModel(200 , "teste" , words)

