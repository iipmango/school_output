from gtts import gTTS
import os
<<<<<<< HEAD
from .dbcon import dbGet
=======
from dbcon import dbGet
>>>>>>> a93772c88b752ddf4dd64e10d8c63c58b550ec59
import datetime

def tts():
    today = datetime.datetime.today().weekday()
    
    Date = []
    Lunch = []
    Date, Lunch = dbGet()
    menu = Lunch[today].split("\n")
    text = ""
    for i in range(4,):
	if menu[i] == None:
		break
        text += menu[i]
    
    tts = gTTS(text = text, lang = 'ko')
    tts.save("helloKR.mp3")
    
    os.system("mpg321 helloKR.mp3")
