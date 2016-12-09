from commands import getVoice
from commands import mcpradio
from snowboy import snowboydecoder
import speech_recognition as sr
import pyttsx
import requests
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
sys.path.append('/home/pi/BrYOUno/web')
import web

def listen_loop():
    detector = snowboydecoder.HotwordDetector("/home/pi/BrYOUno/Hey Bruno.pmdl", sensitivity=0.5)
    print("Waiting for 'Hey Bruno!'")
    detector.start(detected_callback=lambda: onBruno(detector),
               sleep_time=0.03)

def onBruno(detector):
    detector.terminate()
    voice=""
    try:
        voice = getVoice.getVoice()
    except sr.UnknownValueError:
        talker.say("I did not understand that, sorry")
    except sr.RequestError as e:
        talker.say("Could not decode speech. You probably used up your API credits, idiot")


    print voice
    if "lights" in voice:
        talker.say("Toggling lights")
        r = requests.get("http://0.0.0.0/lights")
    elif "radio" in voice:
        if "stop" in voice:
            talker.say("Stopping music")
            r = requests.get("http://0.0.0.0/music/stop")
        else:
            talker.say("Starting MCParks radio")
            r = requests.get("http://0.0.0.0/music/start")
    elif voice == "how are you doing":
        talker.say("I am doing well.")
        talker.say("Thank you for asking!")
    else:
        talker.say("No command found.")
    listen_loop()

if __name__ == "__main__":
    listen_loop()
