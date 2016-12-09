import getVoice
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
import subprocess
player = ""
def play():
    global player
    print "playing"
    talker.say("Playing Music")
    player = subprocess.Popen(["mplayer", "-shuffle", "-playlist", "http://172.18.165.129:9999/get_playlist?id=ef7d7336-e2bf-42b5-978c-c631d444a699"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
def stop():
    global player
    player.stdin.write("q")
    talker.say("Music stopped")
