from fastapi import APIRouter
from _3Words.Services import wordsService
from _3Words.Services import speechService
from _3Words.Models.responseModel import ResponseModel
from _3Words.Models.wordModel import wordModel as WordModel
from _3Words.Models.requestWordsModel import RequestWordsModel
from _3Words.Models.speechToTextModel import speechToTextModel as SpeechToText
from _3Words.Models.writingTestModel import writingTestModel  as WritingTest

router = APIRouter()
#region Words

@router.post("/words")
async def defaultWords(request:RequestWordsModel) -> ResponseModel:
    try:
        words = wordsService.wordsPackMaker(request.fromLanguage,request.toLanguage)
        return ResponseModel(200 , "The words are..." , words)
    except :
        return ResponseModel(600 , "teste")

#endregion

#region Challenge
    
@router.post("/wordChallenge")
async def wordChallenge(word:str) -> ResponseModel:
    try:
        response = WordModel()
        response.word = word
        response.file = speechService.textToSpeech(word)
        return ResponseModel(200 , None , response)
    except :
        return ResponseModel(600 , "teste")

@router.post("/wordChallenge/speakingTest")
async def speakingTest(speech:WordModel) -> ResponseModel:
    try:
        response = speechService.processAnswer(speech)
        return ResponseModel(200 , None , response)
    except :
        return ResponseModel(600 , "teste")

@router.post("/wordChallenge/writingTest")
async def writingTest(writingTest:WritingTest) -> ResponseModel:
    try:
        if writingTest.word == writingTest.typedWord:
            return ResponseModel(200 , None , true)
        return ResponseModel(200 , None , false)
    except :
        return ResponseModel(600 , "teste")

#endregion

