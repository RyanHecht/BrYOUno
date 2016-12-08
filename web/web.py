from flask import Flask
from gevent.wsgi import WSGIServer
import time
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
@app.route("/lights")
def lights():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	return "done"

if __name__ == "__main__":
	http_server = WSGIServer(('', 80), app)
	http_server.serve_forever()