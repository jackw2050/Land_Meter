import file_ops as file_op
import ADC as ADC
from MAX1300 import *

Meter                                  = "Land"       
Hardware_revision                      = 1.0        
Software_revision                      = 1.5        
Calibration_version                    = "calibrated" 
Customer                               = "Orangelamp" 

pwm_freq                               = 125        
sense_freq                             = 10000      
adc_offset                             = 0.0  
zh_offset                              = 0.0        
lid_thermistor_offset                  = 0.0        
p12v_offset                            = 0.0        
p5v_offset                             = 0.0        
p3p3v_offset                           = 0.0        
battery_thermistor_offset              = 0.0        
batt_v_offset                          = 0.0        

beam_offset                            = 0.0        
m5v_offset                             = 0.0        
zp_offset                              = 0.0        
gearbox_thermistor_offset              = 0.0        
conning_tower_thermistor_offset        = 0.0        
arrestment_thermistor_offset           = 0.0        
meter_thermistor_1_offset              = 0.0        
meter_thermistor_2_offset              = 0.0        

adc_divider                            = 0.0
zh_divider                             = 0.0        
lid_thermistor_divider                 = 0.0        
p12v_divider                           = 0.0        
p5v_divider                            = 0.0        
p3p3v_divider                          = 0.0        
battery_thermistor_divider             = 0.0        
batt_v_divider                         = 0.0        

beam_divider                           = 0.0        
m5v_divider                            = 0.0        
zp_divider                             = 0.0        
gearbox_thermistor_divider             = 0.0        
conning_tower_thermistor_divider       = 0.0        
arrestment_thermistor_divider          = 0.0        
meter_thermistor_1_divider             = 0.0        
meter_thermistor_2_divider             = 0.0 






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
	ADC.adc_init()
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
	print ""
	
def commHandler():
	# this interrupt is for serial communications
	# Need to see if there is a bluetooth equivilant
	print""
	




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
	        
	        



def initGlobalVars():
	global Meter                               
	global Hardware_revision                   
	global Software_revision                   
	global Calibration_version                 
	global Customer                            
	global pwm_freq                            
	global sense_freq                          
	global adc_offset                          
	global zh_offset                           
	global lid_thermistor_offset               
	global p12v_offset                         
	global p5v_offset                          
	global p3p3v_offset                        
	global battery_thermistor_offset           
	global batt_v_offset                       
	global beam_offset                         
	global m5v_offset                          
	global zp_offset                           
	global gearbox_thermistor_offset           
	global conning_tower_thermistor_offset     
	global arrestment_thermistor_offset        
	global meter_thermistor_1_offset           
	global meter_thermistor_2_offset           
	global adc_divider                         
	global zh_divider                          
	global lid_thermistor_divider              
	global p12v_divider                        
	global p5v_divider                         
	global p3p3v_divider                       
	global battery_thermistor_divider          
	global batt_v_divider                      
	global beam_divider                        
	global m5v_divider                         
	global zp_divider                          
	global gearbox_thermistor_divider          
	global conning_tower_thermistor_divider    
	global arrestment_thermistor_divider       
	global meter_thermistor_1_divider          
	global meter_thermistor_2_divider          
	
	
	
		        
	data = file_op.read_cal_file()
	
	for row in data:
		
		if (row[0] == "Meter"):  	
			Meter = row[1]
		elif (row[0] == "Hardware_revision"): 
			Hardware_revision = row[1]
		elif (row[0] == "Software_revision"):    
			Software_revision = row[1]
		elif (row[0] == "Calibration_version"):   
			Calibration_version = row[1]
		elif (row[0] == "Customer"):  
			Customer = row[1]
		elif (row[0] == "pwm_freq"):  
			pwm_freq = row[1]
		elif (row[0] == "sense_freq"): 
			sense_freqv = row[1]
		elif (row[0] == "adc_offset"):   
			adc_offset = row[1]
		elif (row[0] == "zh_offset"):   
			zh_offset = row[1]
		elif (row[0] == "lid_thermistor_offset"): 
			lid_thermistor_offset = row[1]
		elif (row[0] == "p12v_offset"):
			p12v_offset = row[1]
		elif (row[0] == "p5v_offset"):  
			p5v_offset = row[1]
		elif (row[0] == "p3p3v_offset"):
			p3p3v_offset = row[1]
		elif (row[0] == "battery_thermistor_offset"):
			battery_thermistor_offset
		elif (row[0] == "batt_v_offset"): 
			batt_v_offset = row[1]
		elif (row[0] == "beam_offset"):
			beam_offset = row[1]
		elif (row[0] == "m5v_offset"):  
			m5v_offset = row[1]
		elif (row[0] == "zp_offset"):  
			zp_offset = row[1]
		elif (row[0] == "gearbox_thermistor_offset"):  
			gearbox_thermistor_offset = row[1]
		elif (row[0] == "conning_tower_thermistor_offset"):  
			conning_tower_thermistor_offset = row[1]
		elif (row[0] == "arrestment_thermistor_offset"):    
			arrestment_thermistor_offset = row[1]
		elif (row[0] == "meter_thermistor_1_offset"):  
			meter_thermistor_1_offset = row[1]
		elif (row[0] == "meter_thermistor_2_offset"):   
			meter_thermistor_2_offset = row[1]
		elif (row[0] == "adc_divider"):    
			adc_divider = row[1]
		elif (row[0] == "zh_divider"):  
			zh_divider = row[1]
		elif (row[0] == "lid_thermistor_divider"):
			lid_thermistor_divider = row[1]
		elif (row[0] == "p12v_divider"):  
			p12v_divider = row[1]
		elif (row[0] == "p5v_divider"):     
			p5v_divider = row[1]
		elif (row[0] == "p3p3v_divider"):      
			p3p3v_divider = row[1]
		elif (row[0] == "battery_thermistor_divider"):  
			battery_thermistor_divider = row[1]
		elif (row[0] == "batt_v_divider"):     
			batt_v_divider = row[1]
		elif (row[0] == "beam_divider"):  
			beam_divider = row[1]
		elif (row[0] == "m5v_divider"): 
			m5v_divider = row[1]
		elif (row[0] == "zp_divider"):   
			zp_divider = row[1]
		elif (row[0] == "gearbox_thermistor_divider"):   
			gearbox_thermistor_divider = row[1]
		elif (row[0] == "conning_tower_thermistor_divider"): 
			conning_tower_thermistor_divider = row[1]
		elif (row[0] == "arrestment_thermistor_divider"):    
			arrestment_thermistor_divider = row[1]
		elif (row[0] == "meter_thermistor_1_divider"):      
			meter_thermistor_1_divider = row[1]
		elif (row[0] == "meter_thermistor_2_divider"): 
			meter_thermistor_2_divider = row[1]
		elif (row[0] == "field"):
			print "reading data file"
		else:
			print "Error reading data file.\nCould not find variable named ",row[0]
			
def main():
#	initialize_land()			
	initGlobalVars()			
main()