import speech_recognition as sr
import sys
import wave
import time
import pyaudio
sys.path.append('/home/pi/BrYOUno/utils')
import talker

def getVoice(prompt=true):
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
    return speech
