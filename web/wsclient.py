import websocket
import thread
import time
import requests

def on_message(ws, message):
    if message == 'lights':
		r = requests.get("http://0.0.0.0/lights")

def on_error(ws, error):
    print "error:: " + error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
	def run(*args):
		
		for i in range(3):
			time.sleep(1)

		time.sleep(1)
		print "thread terminating..."
	thread.start_new_thread(run, ())

def on_openn(ws):
	print "open!"


if __name__ == "__main__":
	print "waiting..."
	time.sleep(10)
	print "starting..."
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://ryanhecht.net:8080",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
