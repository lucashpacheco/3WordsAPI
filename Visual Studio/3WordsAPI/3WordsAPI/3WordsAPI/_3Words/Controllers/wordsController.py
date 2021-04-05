from fastapi import APIRouter
from _3Words.Services import wordsService
from _3Words.Models.responseModel import ResponseModel

router = APIRouter()

@router.get("/words")
async def defaultWords():
    try:
        words = wordsService.wordsPackMaker()
        words = words
        return ResponseModel(200 , "teste" , words)
    except :
        return ResponseModel(600 , "teste" , words)
    

