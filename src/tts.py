from gtts import gTTS
import os
from dbcon import dbGet
import datetime

def tts():
    today = datetime.datetime.today().weekday()
    
    Date = []
    Lunch = []
    Date, Lunch = dbGet()
    menu = Lunch[today].split("\n")
    text = ""
    for i in range(4,10):
        text += menu[i]
    
    tts = gTTS(text = text, lang = 'ko')
    tts.save("helloKR.mp3")
    
    os.system("mpg321 helloKR.mp3")
