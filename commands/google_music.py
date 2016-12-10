import getVoice
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import talker
import subprocess
import urllib
import requests

player = ""
def play():
    global player
    print "playing"
    option = getVoice.select(["song", "artist", "station", "playlist"])
    if option == "song" or option == "artist":
        search(option)
    elif option == "station":
        station()
    elif option == "playlist":
        playlist()

def stop():
    global player
    if not (player == ""):
        player.terminate()
    player = ""
    talker.say("Music stopped")

def search(option):
    url = "http://0.0.0.0:9999/get_by_search?type=" + option
    talker.say("Speak search query:")
    query = getVoice.getVoice(prompt=False)
    if option == "song":
        url += "&title=" + urllib.quote(query)
        player = setPlayer(["mplayer", url + "&num_tracks=1"])
    elif option == "artist":
        url += "&artist=" + urllib.quote(query)
        player = setPlayer(["mplayer", "-playlist", url])

def station():
    url = ""


def playlist():
    talker.say("Say playlist keyword:")
    query = getVoice.getVoice(prompt=False)
    playlists_text = requests.get("http://pi.ryanhecht.net:9999/get_all_playlists?format=text").text[:-1]
    all_playlists = playlists_text.split("\n")
    index = 0
    playlist_url = ""
    for pl in all_playlists:
        if query in pl[0:pl.index("|")].lower():
            to_trim = pl.index("|") + 1
            playlist_url = pl[to_trim:]
            break
        index = index + 1
    if playlist_url == "":
        talker.say("Playlist not found. Sorry.")
    else:
        player = setPlayer(["mplayer", "-shuffle", "-playlist", playlist_url])

def setPlayer(args):
    if player == "":
        return subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
