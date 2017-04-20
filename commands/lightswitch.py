import RPi.GPIO as GPIO
import time

# Sends IR signal to Arduino controller to  toggle lights
# it's new!!
def toggle():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    #print("on")
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.099)
    #print("off")
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.75)
    #print("on")
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    #print("off")
    GPIO.output(12, GPIO.LOW)

if __name__ == "__main__":
    toggle()
