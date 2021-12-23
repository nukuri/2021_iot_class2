import RPi.GPIO as GPIO
import time


TRIGGER_PIN = 4
ECHO_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO.TRIGGER_PIN,GPIO.OUT)