from random_word import RandomWords
from _3Words.Data import wordsRepository
from _3Words.Services import translationService
import re

def generate():
    r = RandomWords()
    words = r.get_random_words(hasDictionaryDef="true",minDictionaryCount=1,limit=3)
    refined_words = []

    for word in words:
        word = re.sub('[^A-Za-z]+', '', word.lower())
        refined_words.append(word)
    return refined_words

def getAllNonRefinedWords():
    allWords = wordsRepository.getAllNonRefinedWords()
    return allWords

def getNonRefinedWord():
    word = wordsRepository.getNonRefinedWord()
    return word

def translateWord(target:str):
    wordx = wordsRepository.getNonRefinedWord()
    word = re.sub('[^A-Za-z]+', '', wordx[0].lower().replace('\n', ''))
    translatedWord = translationService.translateText(word , target)
    while translationService.detectLanguage(translatedWord) != target:
        wordx = wordsRepository.getNonRefinedWord()
        word = re.sub('[^A-Za-z]+', '', wordx[0].lower().replace('\n', ''))
        translatedWord = translationService.translateText(word, target)
    return { word : translatedWord } 

def wordsPackMaker():
    words = []
    while len(words) < 3:
        word = translateWord('es')
        words.append(word)
    return words


