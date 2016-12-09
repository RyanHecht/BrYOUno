import websocket
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
#import speech_recognition as sr
import getVoice
from snowboy import snowboydecoder


stop_listening = False
play="nothing"
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("closed!")

def on_open(ws):
    ws.send("name:RyanPi")
    engine.say("Web Socket opened.")
    engine.say("Please say the name of a song")
    engine.runAndWait()
    play="nothing"
    detector = snowboydecoder.HotwordDetector("/home/pi/BrYOUno/Hey Bruno.pmdl", sensitivity=0.5)
    detector.start(detected_callback=lambda: on_word(detector),
                interrupt_check=interrupt,
               sleep_time=0.03)
    play = getVoice.getVoice()
    print "back in wd"
    if ("main" in play) and ("street" in play):
        play="mainstreet"
    engine.say("Playing " + play)
    print(play)
    engine.runAndWait()

def on_word(detector):
    detector.terminate()
    stop_listening = True

def interrupt():
    return stop_listening

def start():
    websocket.enableTrace(True)


    ws = websocket.WebSocketApp("ws://main.mcparks.us:8887/",
                    on_message = on_message,
                    on_error = on_error,
                    on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    start()
