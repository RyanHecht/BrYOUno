# Where all the magic happens. Contains the main input loop, and command parsing/firing
from commands import getVoice
from commands import mcpradio
from snowboy import snowboydecoder
import speech_recognition as sr
import pyttsx
import requests
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
import db
sys.path.append('/home/pi/BrYOUno/web')
import web

# The main input loop. While active, uses snowboy and a personally trained model file to listen for "Hey Bruno" every 0.03 seconds
def listen_loop():
    detector = snowboydecoder.HotwordDetector("/home/pi/BrYOUno/Hey Bruno.pmdl", sensitivity=0.5)
    print("Waiting for 'Hey Bruno!'")
    detector.start(detected_callback=lambda: onBruno(detector),
               sleep_time=0.03)

# When the keyword is detected, this function is fired
def onBruno(detector):
    # The detector is stopped so we can get more input
    detector.terminate()
    voice=""
    try:
        # Asks the user what they want, with exception handling
        voice = getVoice.getVoice()
    except sr.UnknownValueError:
        talker.say("I did not understand that, sorry")
    except sr.RequestError as e:
        talker.say("Could not decode speech. You probably used up your API credits, idiot")

    # Parses and runs given command via API call, or has a speech interaction with the user.
    # In a try block so to catch any errors and make the user aware of them/log them
    try:
        print voice
        voice = voice.lower()
        if "lights" in voice:
            talker.say("Toggling lights")
            r = requests.get("http://0.0.0.0/lights")
        elif "radio" in voice:
            if "stop" in voice:
                talker.say("Stopping music")
                r = requests.get("http://0.0.0.0/mcp/stop")
            else:
                talker.say("Starting MCParks radio")
                r = requests.get("http://0.0.0.0/mcp/start")
        elif "google" in voice:
            if "music" in voice:
                if "stop" in voice:
                    talker.say("Stopping Google Play Music")
                    r = requests.get("http://0.0.0.0/music/stop")
                else:
                    talker.say("Playing Google Play Music")
                    r = requests.get("http://0.0.0.0/music/start")
        elif "tasks" in voice:
            talker.say("Opening Toodoo ist")
            r = requests.get("http://0.0.0.0/todoist")
        elif voice == "how are you doing":
            talker.say("I am doing well.")
            talker.say("Thank you for asking!")
        elif "help" in voice:
            talker.say("Help menu coming soon.")
        elif voice == "what can you do":
            talker.say("I can perform a variety of functions")
            talker.say("First, say 'Hey Bruno' to activate me")
            talker.say("Then, ask me to turn off the lights,")
            talker.say("play Christmas Music,")
            talker.say("Or to open MCParks radio")
            talker.say("Or, ask me how I'm doing!")
        else:
            talker.say("No command found.")
    except Exception as e:
        db.log_error(type(e).__name__, str(e), __file__)
        print "Encountered an error in command handling"
        talker.say("Encountered an error.")
        talker.say("Sorry.")
    finally:
        listen_loop()

if __name__ == "__main__":
    listen_loop()
