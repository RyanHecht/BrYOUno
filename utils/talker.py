import pyttsx

# Given String input "text", will say it, slightly slower than the default pyttsx rate
def say(text):
    engine = pyttsx.init()
    engine.setProperty('rate', engine.getProperty('rate')-20)
    engine.say(text)
    engine.runAndWait()
