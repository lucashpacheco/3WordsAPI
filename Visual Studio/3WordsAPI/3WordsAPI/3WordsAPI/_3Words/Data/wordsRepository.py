from _3Words.Data import dataUtils as db
from datetime import datetime

def getAllNonRefinedWords():
    rows = db.select("SELECT word FROM tbNonRefinedWord").fetchall()
    return rows

def getNonRefinedWord():
    rows = db.select("SELECT TOP 1 word FROM tbNonRefinedWord ORDER BY NEWID()").fetchone()
    return rows

def insertNewWord(word):
    rows = getAllNonRefinedWords()
    if word not in rows:
        db.insert("Insert into tbNonRefinedWord( word, dt_insertDate) VALUES (?, ?)", ( word ,  datetime.now()))