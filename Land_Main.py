import file_opsfile_op as file_op
import pwm as pwm
from bbio import *


#	Notes
# Add mux to one chanel of MAX1300 for system voltage measurements. (12V, +/- 5V, 3.3V, 36V, Beam volt, 9V and precision volatage reference)




def initialize_land():
	# Sysyewm check.
	# 0)	Call init for all devices. (ssi, i2c etc.)
	# 1)	Check status of all system voltages (Use precistion voltage source on one channel for ADC cal)
	# 2)	Connect to database
	# 3)	Get cal factors etc.
	# 4)	Check status of levels
	# 5)	Start PWM
	# 6)	Check status of beam(measure @ 10% duty cycle and 90% duty cycle then zero via feedback)
	# 7)	Setup interrupts
	adc_init()
	gpio_init()
	pwm.init()
	MAX1300.init()
	uart.init()
	display_init()
	
	

def comms():
	"""
	Gets serial data and parses command and data
	Returns list with command a data
	n_bytes
	z_command
	z_data
	checksum
	"""
	error = "no error"
	return error



def heartBeatHandler():
	# need to define handler
	# send data to pda if flag is set
	
def commHandler():
	# this interrupt is for serial communications
	# Need to see if there is a bluetooth equivilant
	




def beam_check():

	MAX1300.init() #initialize beam measurement

	duty_cycle = 10
	while True:
		pwm.set_force_duty_cycle(duty_cycle)
		ADC_value = MAX1300.readADC()
		
	    	print(duty_cycle, " , ", ADC_value)
	    
		count += 1
		if count >= 90:
	    		break
	        
	        
def main():
	initialize_land()
	while True:
		if record_data == True:
			# Measure beam and levels
	#	else 
			# Measure levels	
	        