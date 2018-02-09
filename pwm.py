import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
import datetime


#PWM.start(channel, duty, freq=2000, polarity=0)
PWM.start("P8_13", 50)
# PWM.set_frequency("P9_14", 10)
debug = True
SENSE_CLOCK = "P9_14"
FORCE_PWM = "P8_13"
HEARTBEAT = "P8_46"
SENSE_FREQUENCY = 10000
FORCE_FREQUENCY = 125
HEARTBEAT_FREQUENCY = 100
current_duty_cycle = 0x00


# add pid code here or in main or in new file


#optionally, you can set the frequency as well as the polarity from their defaults:
# PWM.start("P9_14", 50, 1000, 1)
def pwm_init():
	global debug
	if debug:
		print "Initializing sense clock to ", SENSE_FREQUENCY, "Hz.   ","Duty cycle:  50.0%"
		print "Initializing force clock to ", FORCE_FREQUENCY, "Hz.   ","Duty cycle:  50.0%"
		print "Initializing heart beat clock to 1Hz.   ","Duty cycle:  50.0%"
		
	PWM.start(SENSE_CLOCK, 50, SENSE_FREQUENCY, 0)
	PWM.start(FORCE_PWM, 50, FORCE_FREQUENCY, 0)
	PWM.start(HEARTBEAT, 50.00, HEARTBEAT_FREQUENCY, 0)




def pwm_shutdown():
	PWM.stop(FORCE_PWM)
	PWM.stop(SENSE_CLOCK)
	PWM.cleanup()


def set_force_duty_cycle(duty_cycle):
	global debug
	PWM.set_duty_cycle(FORCE_PWM, duty_cycle)
	if debug:
		print "New Force PWM duty cycle: ", duty_cycle, "%"
	
# PWM.start('P8_13', 50.00, 1, 0)

# GPIO.add_event_detect("P8_11", GPIO.RISING) # look for RISING 
# pwm_init()
# count = 0
# while True:
	
# 	#time.sleep(.001)

# 	if GPIO.event_detected("P8_11"): 
# 		count = count + 1
# 		print "ADC data 1000 count", datetime.datetime.now(), count
# 		BBB_ADC.getAdcVal()
# 		print ""
# 		if count >= 60:
# 			count = 0
# 			print "Doing one minute stuff"

