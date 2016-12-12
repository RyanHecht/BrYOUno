
from flask import Flask, current_app
from gevent.wsgi import WSGIServer
import time
import sys
sys.path.append('/home/pi/BrYOUno/commands')
import mcpradio
import google_music
import lightswitch
import brown_dining
import todoistcmd
sys.path.append('/home/pi/BrYOUno/utils')
import db
app = Flask(__name__)
# The webapp that routes API calls to commands


@app.route("/dashboard")
def dashboard():
	return current_app.send_static_file('dashboard.html')

# Lightswitch toggling
@app.route("/lights")
def lights():
	lightswitch.toggle()
	db.log_action("lights", "")
	return "toggled lights"

# Webpage for lightswitch toggling
@app.route("/switch")
def get_lightswitch():
	return current_app.send_static_file('lightswitch.html')


# MCParks Radio start
@app.route("/mcp/start")
def start_mcpr():
	db.log_action("mcpradio", "started")
	mcpradio.start()
	return "started"

# MCParks Radio stop
@app.route("/mcp/stop")
def stop_mcpr():
	db.log_action("mcpradio", "stopped")
	mcpradio.stop()
	return "stopped"

# Google Play Music start
@app.route("/music/start")
def start_music():
	db.log_action("gplaymusic", "started")
	google_music.play()
	return "started"

# Google Play Music stop
@app.route("/music/stop")
def stop_music():
	db.log_action("gplaymusic", "stopped")
	google_music.stop()
	return "stopped"

# todoist
@app.route("/todoist")
def todoist():
	db.log_action("todoist", "")
	todoistcmd.go()

@app.route("/food")
def food():
	db.log_action("food", "")
	brown_dining.go()


# Get BrYOUno version number, set in this file
# (maybe I should put this in a text file somewhere instead)
@app.route("/version")
def get_version():
	return "1.0"

if __name__ == "__main__":
	print "Starting webserver"
	http_server = WSGIServer(('', 80), app)
	http_server.serve_forever()
