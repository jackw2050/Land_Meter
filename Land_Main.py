import file_ops as file_op
import BBB_ADC as BBB_ADC
import heater as heater
import Adafruit_BBIO.GPIO as GPIO
import time
import Levels
import MAX1300 as MAX1300

system9VoltEnable = "P8_10"
systemPowerEnable = "P8_22"



dutyCycle								= 0.50



Meter                               	= "Land"       
Hardware_revision                   	= 1.0        
Software_revision                   	= 1.5        
Calibration_version                 	= "calibrated" 
Customer                            	= "Orangelamp" 

pwm_freq                            	= 125        
sense_freq                          	= 10000      
adc_offset                          	= 0.0  
zh_offset                           	= 0.0        
lid_thermistor_offset               	= 0.0        
p12v_offset                         	= 0.0        
p5v_offset                          	= 0.0        
p3p3v_offset                        	= 0.0        
battery_thermistor_offset           	= 0.0        
batt_v_offset                       	= 0.0        

beam_offset                         	= 0.0        
m5v_offset                          	= 0.0        
zp_offset                           	= 0.0        
gearbox_thermistor_offset           	= 0.0        
conning_tower_thermistor_offset     	= 0.0        
arrestment_thermistor_offset        	= 0.0        
meter_thermistor_1_offset           	= 0.0        
meter_thermistor_2_offset           	= 0.0        

adc_divider                         	= 0.0
zh_divider                          	= 0.0        
lid_thermistor_divider              	= 0.0        
p12v_divider                        	= 0.0        
p5v_divider                         	= 0.0        
p3p3v_divider                       	= 0.0        
battery_thermistor_divider          	= 0.0        
batt_v_divider                      	= 0.0        

beam_divider                        	= 0.0        
m5v_divider                         	= 0.0        
zp_divider                          	= 0.0        
gearbox_thermistor_divider          	= 0.0        
conning_tower_thermistor_divider    	= 0.0        
arrestment_thermistor_divider       	= 0.0        
meter_thermistor_1_divider          	= 0.0        
meter_thermistor_2_divider          	= 0.0 
beam10									= 0.0
beam50									= 2.5
beam90									= 5.0

p5vTarget								= 5.0           
p5vError								= 0.2 
n5vTarget								= 5.0           
n5vError								= 0.2 
p3p3vTarget								= 3.3           
p3p3vError								= 0.2            
p12vTarget								= 12.0          
p12vError								= 0.5             
batteryTarget							= 12.0          
batteryError							= 2.0          
zh_Target								= 36.0       
zh_Error								= 0.1       
zpTarget								= 24.0           
zpError									= 0.01     




# Setup GPIO for system power
GPIO.setup(systemPowerEnable, GPIO.OUT)	# Enable pin for DC-DC converter
GPIO.setup(system9VoltEnable, GPIO.OUT)	# Enable pin for DC-DC converter





def verifySysVoltages():
	loop_count = 10

	# Need target values for each
	# Need error range for acceptable, warning and error/ stop program
	# First warning for any item must be recorded to file  Need flag for this.
	# Add these to the config/ cal file
	# Add write to log file for start up status and values
	
	print "\nSystem\t\tLow\tValue\tHigh\tStatus"
	print "Voltage\t\tLimit\t\tLimit"
	print "-----------------------------------------------"


	# BBB_ADC.adc_init()
	sysPowerStatus = "Pass"
	
	sys5v = BBB_ADC.read_adc("p5vSys", loop_count, p5v_divider, p5v_offset)
	sys5vOk = "Pass"
	if((sys5v < (p5vTarget - p5vError)) or (sys5v > p5vTarget + p5vError)):
		sys5vOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "+5V system voltage" + "\t" + "target: " + str(p5vTarget) + "\tError:  +/-" + str(p5vError) + "\tMeasured: " + str(round(sys5v,2)) + "\t" + sys5vOk
		file_op.create_log_entry(issue)
	print "+5V\t\t",5 * .95, "\t", round(sys5v,2), "\t",  5 * 1.05, "\t", sys5vOk
	time.sleep(1)



	sys12v = BBB_ADC.read_adc("p12vSys", loop_count, p12v_divider, p12v_offset)
	sys12vOk = "Pass"
	if((sys12v < p12vTarget - p12vError) or (sys12v > p12vTarget + p12vError)):
		sys12vOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "+12V system voltage" + "\t" + "target: " + str(p12vTarget) + "\tError:  +/-" + str(p12vError) + "\tMeasured: " + str(round(sys12v,2)) + "\t" + sys12vOk
		file_op.create_log_entry(issue)
	print "+12V\t\t",12.0 * .95, "\t", round(sys12v,2), "\t", 12.0 * 1.05, "\t", sys12vOk
	time.sleep(1)
	
	sys3p3v = BBB_ADC.read_adc("p3p3vSys", loop_count, p3p3v_divider, p3p3v_offset)
	sys3p3vOk = "Pass"
	if((sys3p3v < p3p3vTarget - p3p3vError) or (sys3p3v > p3p3vTarget + p3p3vError)):
		sys3p3vOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "+3.3V system voltage" + "\t" + "target: " + str(p3p3vTarget) + "\tError:  +/-" + str(p3p3vError) + "\tMeasured: " + str(round(sys3p3v,2)) + "\t" + sys3p3vOk
		file_op.create_log_entry(issue)		
	print "+3.3V\t\t",3.3 * .95, "\t", round(sys3p3v,2), "\t", 3.3 * 1.05, "\t", sys3p3vOk
	time.sleep(1)
	
	battVolt = BBB_ADC.read_adc("battVolt", loop_count, batt_v_divider, batt_v_offset)
	battVoltOk = "Pass"
	if((sys5v < batteryTarget - batteryError) or (battVolt > batteryTarget + batteryError)):
		battVoltOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "Battery  voltage" + "\t" + "target: " + str(batteryTarget) + "\tError:  +/-" + str(batteryError) + "\tMeasured: " + str(round(battVolt,2)) + "\t" + battVoltOk
		file_op.create_log_entry(issue)		
	print "Battery\t\t",9.0, "\t", round(battVolt,2), "\t", 18.0, "\t", battVoltOk
	time.sleep(1)	

	zhVolt = BBB_ADC.read_adc("zhSys", loop_count, zh_divider, zh_offset)
	zhVoltOk = "Pass"
	if((zhVolt < zh_Target - zh_Error) or (zhVolt > zh_Target + zh_Error)):
		zhVoltOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "ZH system voltage" + "\t" + "target: " + str(zh_Target) + "\tError:  +/-" + str(zh_Error) + "\tMeasured: " + str(round(zhVolt,2)) + "\t" + zhVoltOk
		file_op.create_log_entry(issue)		
	print "ZH\t\t",5 * .95, "\t", round(zhVolt,2), "\t", 5 * 1.05, "\t", zhVoltOk
	time.sleep(1)




	sysn5v = MAX1300.ReadADC_average(1 , 10, .01,  1, 0)
	# sysn5v = MAX1300.ReadADC(1)
	sysn5vOk = "Pass"
	if((sysn5v > -1 * n5vTarget - p5vError) or (sysn5v < -1 * n5vTarget - n5vError)):
		sysn5vOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "-5V system voltage" + "\t" + "target: " + str(-1 * n5vTarget) + "\tError:  +/-" + str(p5vError) + "\tMeasured: " + str(round(sysn5v,2)) + "\t" + sysn5vOk
		file_op.create_log_entry(issue)		
	print "-5V\t\t",-5.0 * .95, "\t", round(sysn5v,2), "\t", -5.0 * 1.05, "\t", sysn5vOk
	time.sleep(1)

	zpVolt = MAX1300.ReadADC(2)
	zhVoltOk = "Pass"
	if((zpVolt < zpTarget - zpError) or (zpVolt > zpTarget + zpError)):
		zhVoltOk = "Fail"
		sysPowerStatus = "Fail"
		issue = "ZP system voltage" + "\t" + "target: " + str(zpTarget) + "\tError:  +/-" + str(zpError) + "\tMeasured: " + str(round(zpVolt,2)) + "\t" + zhVoltOk
		file_op.create_log_entry(issue)		
	print "ZP\t\t",24.0 * .999, "\t", round(zpVolt,2), "\t", 24.0 * 1.001, "\t", zhVoltOk
	time.sleep(1)

	print "\nSystem power\t\t\t\t",sysPowerStatus
	print "-----------------------------------------------"



	
	#MAX1300.
	# MAX1300.read_adc(adc_chan, loop_count)
	# MAX1300.read_adc(adc_chan, loop_count)

def startupLand():
	print("ZLS Beaglebone Black boot complete")
	time.sleep(1)
	print "System information"
	print "-----------------------------------------------"
	print "Model\t\t\t",Meter   
	print "Hardware Revision\t",Hardware_revision      
	print "Software Revision\t",Software_revision      
	print "Calibration Status\t",Calibration_version    
	print "Customer\t\t",Customer  
	print "-----------------------------------------------"
	time.sleep(1)
	print("\nEnabling GPIO 1-5 for +/- 5V and +12V")
	GPIO.output(systemPowerEnable, GPIO.LOW)
	time.sleep(1)
	print("DC-DC converters enabled")
	time.sleep(3)
	print("Enabling GPIO 2-4 for +9V")
	GPIO.output(system9VoltEnable, GPIO.LOW)
	time.sleep(1)
	print("9V LDO converter enabled")
	time.sleep(1)
	print "Initializing Land Meter Electronics"
	time.sleep(1)
	print "Verifying system voltages"
	time.sleep(1)
	verifySysVoltages()
	
	
	print "Initializing Sense clock to ", sense_freq, "Hz"
	time.sleep(1)
	print "Initializing Force clock to ", pwm_freq, "Hz\t", dutyCycle * 100,"% Duty cycle"
	time.sleep(1)
	
		
	print "-----------------------------------------------"
	print "Verifying heater subsystem"
	# getHeaterSettings()
	# getHeaterStatus
	heater.heaterInit()
		
	updatedHeat = heater.checkHeaterTemp(heater.heaterList)
	
	degree_sign = u'\N{DEGREE SIGN}'


	#for element in updatedHeat:
	for element in range (len(updatedHeat)):
		if updatedHeat[element][0] == 'Meter':
			print updatedHeat[element][0], "\t\tLow setpoint: ", updatedHeat[element][2], degree_sign, "\tHigh setpoint: ", updatedHeat[element][3], degree_sign, "\tEnabled: ", updatedHeat[element][1], "\tHeater on: ", updatedHeat[element][4], "\tTemp1: ", updatedHeat[element][5], degree_sign, "\tTemp2: ", updatedHeat[element][6], degree_sign
		else:
			print updatedHeat[element][0], "\tLow setpoint: ", updatedHeat[element][2], degree_sign, "\tHigh setpoint: ", updatedHeat[element][3], degree_sign, "\tEnabled: ", updatedHeat[element][1], "\tHeater on: ", updatedHeat[element][4], "\tTemp1: ", updatedHeat[element][5],degree_sign

			

	print "-----------------------------------------------"
	time.sleep(1)
	print "Initializing communications with Levels"
	print "-----------------------------------------------"


	time.sleep(1)
	print "Initializing Bluetooth"
	print "-----------------------------------------------"
	time.sleep(1)
	print "Initializing Wifi"
	from pythonwifi.iwlibs import Wireless
	wifi = Wireless('wlan0')
	print "Connected to:\t", wifi.getEssid()
	print "Mode:\t", wifi.getMode()
	print "-----------------------------------------------"
#	findBeamPoints()




def initialize_land():
	print "Initializing meter"
	# Sysyem check.
	# 0)	Call init for all devices. (ssi, i2c etc.)
	# 1)	Check status of all system voltages (Use precistion voltage source on one channel for ADC cal)
	# 2)	Connect to database
	# 3)	Get cal factors etc.
	# 4)	Check status of levels
	# 5)	Start PWM
	# 6)	Check status of beam(measure @ 10% duty cycle and 90% duty cycle then zero via feedback)
	# 7)	Setup interrupts
	# BBB_ADC.adc_init()
	# gpio_init()
	# pwm.init()
	MAX1300.ADCinit()
	# uart.init()
	# display_init()

	
	

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
	        
	        

def beamFeedbackLoop(target, errorOk, beam_divider, beam_offset):
	global duty_cycle
	chan = 0x80
	averages = 20
	rate = 0.1
	loopMax = 1
	duty_cycle = 50.0
	beamDone = False
	pwm.set_force_duty_cycle(duty_cycle)

	# normalize beam center to 0
	while (beamDone == False):
		ADC_value = MAX1300. ReadADC_average(chan, chan_vrange, averages, rate, loopMax)
		beam_value = ADC_value * beam_divider + beam_offset
		if(beam_value < target - errorOk):
			beamError = (beam_value - target) / target






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
	global beam10
	global beam50
	global beam90	
	global p5vTarget					       
	global p5vError		
	global n5vTarget					       
	global n5vError		
	global p3p3vTarget					       
	global p3p3vError					        
	global p12vTarget					       
	global p12vError					         
	global batteryTarget				       
	global batteryError					  
	global zh_Target					    
	global zh_Error						
	global zpTarget						    
	global zpError						  


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
			pwm_freq = float(row[1])
		elif (row[0] == "sense_freq"): 
			sense_freqv = float(row[1])
		elif (row[0] == "adc_offset"):   
			adc_offset = float(row[1])
		elif (row[0] == "zh_offset"):   
			zh_offset = float(row[1])
		elif (row[0] == "lid_thermistor_offset"): 
			lid_thermistor_offset = float(row[1])
		elif (row[0] == "p12v_offset"):
			p12v_offset = float(row[1])
		elif (row[0] == "p5v_offset"):  
			p5v_offset = float(row[1])
		elif (row[0] == "p3p3v_offset"):
			p3p3v_offset = float(row[1])
		elif (row[0] == "battery_thermistor_offset"):
			battery_thermistor_offset
		elif (row[0] == "batt_v_offset"): 
			batt_v_offset = float(row[1])
		elif (row[0] == "beam_offset"):
			beam_offset = float(row[1])
		elif (row[0] == "m5v_offset"):  
			m5v_offset = float(row[1])
		elif (row[0] == "zp_offset"):  
			zp_offset = float(row[1])
		elif (row[0] == "gearbox_thermistor_offset"):  
			gearbox_thermistor_offset = float(row[1])
		elif (row[0] == "conning_tower_thermistor_offset"):  
			conning_tower_thermistor_offset = float(row[1])
		elif (row[0] == "arrestment_thermistor_offset"):    
			arrestment_thermistor_offset = float(row[1])
		elif (row[0] == "meter_thermistor_1_offset"):  
			meter_thermistor_1_offset = float(row[1])
		elif (row[0] == "meter_thermistor_2_offset"):   
			meter_thermistor_2_offset = float(row[1])
		elif (row[0] == "adc_divider"):    
			adc_divider = float(row[1])
		elif (row[0] == "zh_divider"):  
			zh_divider = float(row[1])
		elif (row[0] == "lid_thermistor_divider"):
			lid_thermistor_divider = float(row[1])
		elif (row[0] == "p12v_divider"):  
			p12v_divider = float(row[1])
		elif (row[0] == "p5v_divider"):     
			p5v_divider = float(row[1])
		elif (row[0] == "p3p3v_divider"):      
			p3p3v_divider = float(row[1])
		elif (row[0] == "battery_thermistor_divider"):  
			battery_thermistor_divider = float(row[1])
		elif (row[0] == "batt_v_divider"):     
			batt_v_divider = float(row[1])
		elif (row[0] == "beam_divider"):  
			beam_divider = float(row[1])
		elif (row[0] == "m5v_divider"): 
			m5v_divider = float(row[1])
		elif (row[0] == "zp_divider"):   
			zp_divider =float( row[1])
		elif (row[0] == "gearbox_thermistor_divider"):   
			gearbox_thermistor_divider = float(row[1])
		elif (row[0] == "conning_tower_thermistor_divider"): 
			conning_tower_thermistor_divider = float(row[1])
		elif (row[0] == "arrestment_thermistor_divider"):    
			arrestment_thermistor_divider = float(row[1])
		elif (row[0] == "meter_thermistor_1_divider"):      
			meter_thermistor_1_divider = float(row[1])
		elif (row[0] == "meter_thermistor_2_divider"): 
			meter_thermistor_2_divider =float(row[1])

		elif (row[0] == "beam10"): 
			beam10 = float(row[1])
		elif (row[0] == "beam50"): 
			beam50 = float(row[1])
		elif (row[0] == "beam90"): 
			beam90 = float(row[1])
		elif (row[0] == "p5vTarget"): 
			p5vTarget = float(row[1])
		elif (row[0] == "p5vError"): 
			p5vError = float(row[1])
		elif (row[0] == "n5vTarget"): 
			n5vTarget = float(row[1])
		elif (row[0] == "n5vError"): 
			n5vError = float(row[1])
		elif (row[0] == "p3p3vTarget"): 
			p3p3vTarget = float(row[1])
		elif (row[0] == "p3p3vError"): 
			p3p3vError = float(row[1])
		elif (row[0] == "p12vTarget"): 
			p12vTarget = float(row[1])
		elif (row[0] == "p12vError"): 
			p12vError = float(row[1])
		elif (row[0] == "batteryTarget"): 
			batteryTarget = float(row[1])
		elif (row[0] == "batteryError"): 
			batteryError = float(row[1])
		elif (row[0] == "zh_Target"): 
			zh_Target = float(row[1])
		elif (row[0] == "zh_Error"): 
			zh_Error = float(row[1])
		elif (row[0] == "zpTarget"): 
			zpTarget = float(row[1])
		elif (row[0] == "zpError"): 
			zpError = float(row[1])


		elif (row[0] == "field"):
			print "Reading data file and initializing global variables"
		else:
			print "Error reading data file.\nCould not find variable named ",row[0]

def findBeamPoints():
	global beam10
	global beam50
	global beam90
	print "Starting Beam calibration"
	print "Measuring beam output range"
	# Record values of Beam output for PWM duty cycle of 10, 50 and 90%
	# Finish with 50% duty cycle
	print "Duty cycle\tBeam output voltage"
	print "----------\t-------------------"
	print "10%       \t",beam10
	print "50%       \t",beam50
	print "90%       \t",beam90


def productionLoop():
	#	initialize_land()			
	initGlobalVars()	# Reads calibration file and assignes global variables	
	initialize_land()
	startupLand()		# Enable DC-DC converters
	# meterRun = True
	# while( meterRun == True):
	# 	print "test"
		
	

def testLoop():
	testNumber = input("Enter test number to be run:\n1)    Simple turn on with time delay\n2)    Turn on with ADC verification\n3)    Turn on with system voltage calibration\n4)    Calibrate levels\n	")
	if(testNumber == 1):
	    test1()
	elif(testNumber == 2):
	    test2()
	elif(testNumber == 3):
	    test3()    
	elif(testNumber == 4):
		Levels.calibrateLevels()      
	else:
    		print("Invalid number entered.  \nTerminating....")
	#	initialize_land()
	
	initGlobalVars()
	initialize_land()
	startupLand()

	
def main():
	
	# At this point the only thing with power should be the processor
	# Load the mode file.  This tells the program if it is to run in productin mode or test / calibration mode.
	
	runMode = file_op.readFile("mode.csv")


	print "Current run mode: ", runMode[0][0]
	
	if( int(runMode[0][0]) == 0):
		productionLoop()
	elif( int(runMode[0][0])  == 1):
		testLoop()
	else:
		print "Invalid entry"
	
	

main()
