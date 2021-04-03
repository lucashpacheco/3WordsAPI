import os
import six
import re
from google_trans_new import google_translator

def translateText(text, target):
    trans = google_translator()
    result1 = trans.translate(text , lang_tgt=target)
    if type(result1) != list:
        result = re.sub('[^A-Za-z ]+', '', result1.lower())
    else:
        result = re.sub('[^A-Za-z ]+', '', result1[0])
        #res2 = re.sub('[^A-Za-z]+', '', result1[1])
        #result = res1 + '/' + res2
    return result

def detectLanguage(text):
    trans = google_translator()
    result = trans.detect(text)
    return result[0]
    