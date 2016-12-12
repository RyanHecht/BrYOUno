import speech_recognition as sr
import sys
import wave
import time
import pyaudio
sys.path.append('/home/pi/BrYOUno/utils')
import talker
import db


# The main method of getting user input via voice
# Option argument prompt will prompt the user with "How can I help you?", other wise will ding when listening
# returns lowercase representation of what Google thinks was said, using SpeechRecognition's interface
def getVoice(prompt=True):
    print "getting voice..."
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print "in microphone"
        r.adjust_for_ambient_noise(source, duration = 1)
        if prompt:
            talker.say("How can I help you")
        else:
            ding_wav = wave.open("/home/pi/BrYOUno/utils/ding.wav", 'rb')
            ding_data = ding_wav.readframes(ding_wav.getnframes())
            audio = pyaudio.PyAudio()
            stream_out = audio.open(
            format=audio.get_format_from_width(ding_wav.getsampwidth()),
            channels=ding_wav.getnchannels(),
            rate=ding_wav.getframerate(), input=False, output=True)
            stream_out.start_stream()
            stream_out.write(ding_data)
            time.sleep(0.2)
            stream_out.stop_stream()
            stream_out.close()
        print "listening"
        audio = r.listen(source)
    print "out of microphone"
    speech = r.recognize_google(audio)
    db.log_action("voice", speech.lower())
    return speech.lower()


# Allows the user to select between a predefined list of choices, given in list form in "choices" argument
# Optional "selector" argument allows to change what talker calls the options (by default, option)
def select(choices, selector="Option"):
    talker.say("Select a " + selector)
    index = 0
    for choice in choices:
        talker.say(str(index))
        talker.say(choice)
        index = index + 1
    voice = getVoice(prompt=False)
    if "repeat" in voice:
        return select(choices, selector)
    else:
        try:
            res_index = int(voice)
        except ValueError:
            nums = {'zero':0,'one':1,'two':2,'to':2,'too':2,'three':3,'four':4,'for':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
            res_index = nums[voice]
        db.log_action("voice", choices[res_index])
        return choices[res_index]
