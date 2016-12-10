import pyttsx


def say(text):
    engine = pyttsx.init()
    engine.setProperty('rate', engine.getProperty('rate')-20)
    engine.say(text)
    engine.runAndWait()
