from fastapi import APIRouter
from _3Words.Services import wordsService
from _3Words.Services import speechService
from _3Words.Models.responseModel import ResponseModel
from _3Words.Models.wordModel import wordModel as WordModel
from _3Words.Models.requestWordsModel import RequestWordsModel
from _3Words.Models.speechToTextModel import speechToTextModel as SpeechToText

router = APIRouter()

@router.get("/words")
async def defaultWords(request:RequestWordsModel) -> ResponseModel:
    try:
        words = wordsService.wordsPackMaker(request.fromLanguage,request.toLanguage)
        words = words
        return ResponseModel(200 , "The words are..." , words)
    except :
        return ResponseModel(600 , "teste")
    
@router.get("/wordChallenge")
async def wordChallenge(word:str) -> ResponseModel:
    try:
        response = WordModel()
        response.word = word
        response.file = speechService.textToSpeech(word)
        return ResponseModel(200 , None , response)
    except :
        return ResponseModel(600 , "teste")

@router.get("/wordChallenge/speakingTest")
async def speakingTest(speech:SpeechToText) -> ResponseModel:
    try:
        response = speechService.processAnswer(speech)
        return ResponseModel(200 , "The words are..." , response)
    except :
        return ResponseModel(600 , "teste")