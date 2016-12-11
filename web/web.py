from flask import Flask, current_app
from gevent.wsgi import WSGIServer
import time
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/BrYOUno/commands')
import mcpradio
import google_music
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
@app.route("/lights")
def lights():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	return "done"

@app.route("/switch")
def get_lightswitch():
	return current_app.send_static_file('lightswitch.html')


@app.route("/mcp/start")
def start_mcpr():
	mcpradio.start()
	return "started"

@app.route("/mcp/stop")
def stop_mcpr():
	mcpradio.stop()
	return "stopped"

@app.route("/music/start")
def start_music():
	google_music.play()
	return "started"

@app.route("/music/stop")
def stop_music():
	google_music.stop()
	return "stopped"

@app.route("/version")
def get_version():
	return "0.1"

if __name__ == "__main__":
	print "Starting webserver"
	http_server = WSGIServer(('', 80), app)
	http_server.serve_forever()
