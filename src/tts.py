from gtts import gTTS
import os
import dbcon

def tts():
    
    #Date = []
    #Lunch = []
    #Date, Lunch = dbcon.dbGet()
    
    text = "heLLO"
    tts = gTTS(text = text, lang = 'en')
    tts.save("helloKR.mp3")
    
    os.system("mpg321 helloKR.mp3")


tts()
