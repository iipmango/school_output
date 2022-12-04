from gtts import gTTS
import os
import dbcon

def tts():
    
    # Date = []
    # Lunch = []
    # Date, Lunch = dbcon.dbGet()
    
    text = "안녕하세요"
    tts = gTTS(text = text, lang = 'ko')
    tts.save("helloKR.mp3")
    
    os.system("mpg321 helloKR.mp3")


tts()