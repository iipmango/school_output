import RPi.GPIO as GPIO
import time
from src import *

switch = 23

GPIO.sermode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)

try:
    while True:
        if GPIO.input(switch) == True:
            tts()
            send
except KeyboardInterrupt:
    GPIO.cleanup()
