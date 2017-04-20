from websocket import create_connection
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
import subprocess
player = ""

# Connects to the MCParks Audio Websocket server, asks to be played Grand Floridan piano music
def start():
    global player
    if player == "":
        print "Connecting to MCParks Audio Server..."
        ws = create_connection("ws://main.mcparks.us:8887")
        print "Sending opening message..."
        ws.send("name:BrYOUno")
        print "Sent."
        ws.send("playplay:gfpiano")
        res = ws.recv()
        ws.close()
        talker.say("Playing music.")
        if res.startswith("loop-"):
            splt = res.split("-")
            pos = int(splt[1]) / 1000
            toplay = splt[2]
            player = subprocess.Popen(["mplayer", "http://mcparks.us/audio_files/gfpiano.mp3", "-ss", str(pos)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Terminates musc playing
def stop():
    global player
    player.terminate()
    player = ""
    talker.say("Music stopped.")
if __name__ == "__main__":
    start()

def choose_song():
    talker.say("Choose a song:")
    talker.say("1: Main Street, USA")
    talker.say("2: Epcot Entrance")
    talker.say("3: Grand Floridian Piano")
    talker.say("4: Space Mountain 1")
