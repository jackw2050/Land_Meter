import Adafruit_BBIO.GPIO as GPIO
import time


SSTRB = "P8_10"

if GPIO.input(SSTRB):
	print "Data ready"
	