from gtts import gTTS
import os
import dbcon
# from .dbcon import dbGet
import datetime

def tts():
    today = datetime.datetime.today().weekday()
    
    Date = []
    Lunch = []
    Date, Lunch = dbcon.dbGet()
    menu = Lunch[today].split("\n")
    if Lunch[today + 7].split("\n"):
        menu += Lunch[today + 7].split("\n")
    text = ""
    print(menu)
    size = len(menu)
    for i in range(0, size):
        if menu[i] == '':
            continue
        else:
            text += menu[i]
    tts = gTTS(text = text, lang = 'ko')
    tts.save("helloKR.mp3")
    
    os.system("mpg321 helloKR.mp3")