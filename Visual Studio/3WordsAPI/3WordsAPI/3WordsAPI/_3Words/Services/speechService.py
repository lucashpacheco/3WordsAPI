import speech_recognition as sr
from _3Words.Models.speechToTextModel import speechToTextModel as SpeechToText
from gtts import gTTS


def speechToText(file) -> str:
    with sr.AudioFile(fileX) as source:
        audio_en = r.record(source)  # read the entire audio file
    try:
        text = r.recognize_google(audio_en)
    except sr.UnknownValueError:
        raise("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        raise("Could not request results from Google Cloud Speech service; {0}".format(e))
    return text

def processAnswer(answer:SpeechToText) -> bool:
    answerWord = speechToText(answer.file)
    if(answer.word == answerWord):
        return true
    return false

def textToSpeech(text:str):
    tts = gTTS(text)
    #tts.save('{}.mp3'.format(text))
    return tts.write_to_fp(text+"MP3")