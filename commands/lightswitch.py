import RPi.GPIO as GPIO
import time

def toggle():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(12, GPIO.LOW)

if __name__ == "__main__":
    toggle()
