import Adafruit_BBIO.GPIO as GPIO
import time
 
 
 

mgal = 1
steps = 70 * mgal
step_size = 100000
turns = step_size * 1
speed = 10

# Main shaft setup
GPIO.setup("P8_12", GPIO.OUT)       #Shaft PWM
GPIO.setup("P8_11", GPIO.OUT)       #Shaft Direction
GPIO.setup("P8_27", GPIO.IN)        #Shaft Fault 

# Arrestment setup
GPIO.setup("P8_17", GPIO.IN)         #Arrestment Direction
GPIO.setup("P8_18", GPIO.IN)         #Arrestment PWM
GPIO.setup("P8_25", GPIO.IN)         #Shaft Fault 


# drv8801
# Cross & Long setup

GPIO.setup("P8_9", GPIO.IN)         #Long Fault 
GPIO.setup("P9_23", GPIO.OUT)       #Long PWM
GPIO.setup("P9_25", GPIO.OUT)       #Long Direction


GPIO.setup("P8_34", GPIO.OUT)       #Cross PWM
GPIO.setup("P8_35", GPIO.OUT)       #Cross Direction
GPIO.setup("P8_10", GPIO.IN)        #Cross Fault










GPIO.output("P8_11", GPIO.LOW) 
for x in range(turns):
	# TODO: write code...
    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(.5 * speed * 0.1e-3)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(0.5 * speed * 0.1e-3)


# time.sleep(.25)
# GPIO.output("P8_11", GPIO.LOW)
# for x in range(steps):
# 	# TODO: write code...
#     GPIO.output("P8_12", GPIO.HIGH)
#     time.sleep(1e-3)
#     GPIO.output("P8_12", GPIO.LOW)
#     time.sleep(1e-3)
