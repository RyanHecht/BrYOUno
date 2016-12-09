import speech_recognition as sr
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker

def getVoice():
    print "getting voice..."
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print "in microphone"
        r.adjust_for_ambient_noise(source, duration = 1)
        talker.say("How can I help you")
        print "listening"
        audio = r.listen(source)
    print "out of microphone"
    speech = r.recognize_google(audio)
    return speech
