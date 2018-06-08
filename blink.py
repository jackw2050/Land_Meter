import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P8_11", GPIO.OUT)
mgal = 1
steps = 70 * mgal
step_size = 50
turns = step_size * 10
speed = 1


GPIO.output("P8_11", GPIO.HIGH) 
for x in range(turns):
	# TODO: write code...
    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(.5 * speed * 1e-3)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(0.5 * speed * 1e-3)


# time.sleep(.25)
# GPIO.output("P8_11", GPIO.LOW)
# for x in range(steps):
# 	# TODO: write code...
#     GPIO.output("P8_12", GPIO.HIGH)
#     time.sleep(1e-3)
#     GPIO.output("P8_12", GPIO.LOW)
#     time.sleep(1e-3)
