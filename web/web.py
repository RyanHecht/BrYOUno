from flask import Flask
from gevent.wsgi import WSGIServer
import time
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/BrYOUno/commands')
import mcpradio
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
@app.route("/lights")
def lights():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	return "done"

@app.route("/music/start")
def start_music():
	mcpradio.start()
	return "started"

@app.route("/music/stop")
def stop_music():
	mcpradio.stop()
	return "stopped"

if __name__ == "__main__":
	http_server = WSGIServer(('', 80), app)
	http_server.serve_forever()
