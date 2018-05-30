import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P9_15", GPIO.OUT)
# GPIO.setup("P8_10", GPIO.OUT)


# GPIO.output("P8_10", GPIO.HIGH) 
for x in range(360):
	# TODO: write code...
    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(1e-3)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(1e-3)

# GPIO.output("P8_10", GPIO.LOW)
for x in range(360):
	# TODO: write code...
    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(1e-3)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(1e-3)
