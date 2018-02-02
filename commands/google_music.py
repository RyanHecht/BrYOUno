# Interface between BrYOUno and GMusicProxy
import getVoice
import sys
sys.path.append('/home/pi/BrYOUno/utils')
import db
import talker
import subprocess
import urllib
import requests



# Initialize player as empty string. A check for this will tell whether music is currently Playing
player = ""

# Talker will ask user to select between song, artist, station, and playlist, and call the proper function
def play():
    global player
    if player == "":
        try:
            print "playing"
            option = getVoice.select(["song", "artist", "station", "playlist"])
            if option == "song" or option == "artist":
                search(option)
            elif option == "station":
                station()
            elif option == "playlist":
                playlist()
        except Exception as e:
            print("error encountered")
            talker.say("Encountered error.")
            db.log_error(type(e).__name__, str(e), __file__)
# If there is a player playing, stop it
def stop():
    global player
    if player != "":
        player.terminate()
        player = ""
        talker.say("Music stopped")

# If the user wants to play a song or artist, we use the get_by_search API call, the specifics for which are determined here
def search(option):
    global player
    url = "http://0.0.0.0:9999/get_by_search?type=" + option
    talker.say("Speak search query:")
    query = getVoice.getVoice(prompt=False)
    if option == "song":
        url += "&title=" + urllib.quote(query)
        db.log_action("gplaymusic", "played song " + query)
        player = setPlayer(["mplayer", url + "&num_tracks=1"])

    elif option == "artist":
        url += "&artist=" + urllib.quote(query)
        db.log_action("gplaymusic", "played artist " + query)
        player = setPlayer(["mplayer", "-playlist", url])

# In the case of a station, this API call must be made
def station():
    # NOT YET IMPLEMENTED
    url = ""


# In the case of a playlist, the user says a keyword to identify the playlist by, and the system selects the first one that comes up
def playlist():
    global player
    talker.say("Say playlist keyword:")
    query = getVoice.getVoice(prompt=False)
    playlists_text = requests.get("URL_HERE:9999/get_all_playlists?format=text").text[:-1]
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
        talker.say("Would you like it shuffled?")
        shuffle = getVoice.getVoice(prompt=False)
        if shuffle == "yes":
            player = setPlayer(["mplayer", "-shuffle", "-playlist", playlist_url])
        else:
            player = setPlayer(["mplayer", "-playlist", playlist_url])
        db.log_action("gplaymusic", "played playlist " + query)


# Will start an mplayer subprocess with the arguments given, opening the URL to get the playlist/song
def setPlayer(args):
    if player == "":
        #return subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return subprocess.Popen(args)
