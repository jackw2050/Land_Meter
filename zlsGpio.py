import Adafruit_BBIO.GPIO as GPIO
import time

debug = True
systemPowerEnable   = "P8_22"  #GPIO 1-5
meterHeaterFET      = "P8_5"
gearboxHeaterFET    = "P8_6"

arrestmentHeaterFET = "P8_3"
conningTowerFET     = "P8_4"
icHeaterFET         = "P8_19"
levelsReset         = "P8_28"
rtc1Hz              = "P8_29"
rtcReset            = "P8_30"
MUX_A0				= "P8_39"    #GPIO 2-12  BAD
MUX_A1				= "P8_40"    #GPIO 2-13  OK
MUX_A2				= "P8_41"    #GPIO 2-14  OK
thermistor_MUX_A0	= "P8_31"    #GPIO 0-10  BAD
thermistor_MUX_A1	= "P8_32"    #GPIO 0-11  BAD
thermistor_MUX_A2	= "P8_33"    #GPIO 0-9   OK
FB_MUX_A0			= "P8_25"    #GPIO 1-0   OK
FB_MUX_A1			= "P8_26"    #GPIO 1-29  OK





def zlsInit(debug):
	#Enable GPIO for system power DC-DC converters
	if (debug):
		print "Initializing GPIO"
	GPIO.setup(systemPowerEnable, 	GPIO.OUT)

	#Enable GPIO heater for heater FETs
	GPIO.setup(meterHeaterFET, 		GPIO.OUT)
	GPIO.setup(gearboxHeaterFET, 	GPIO.OUT)
	GPIO.setup(arrestmentHeaterFET,	GPIO.OUT)
	GPIO.setup(conningTowerFET, 	GPIO.OUT)
	GPIO.setup(icHeaterFET, 		GPIO.OUT)
	#Enable GPIO for levels
	GPIO.setup(levelsReset, 		GPIO.OUT)
	# Enable 1Hz heartbeat input
	# GPIO.setup(rtc1Hz, 				GPIO.IN)
	GPIO.setup(MUX_A0, 				GPIO.OUT)	
	GPIO.setup(MUX_A1, 				GPIO.OUT)
	GPIO.setup(MUX_A2, 				GPIO.OUT)
	GPIO.setup(thermistor_MUX_A0, 	GPIO.OUT)
	GPIO.setup(thermistor_MUX_A1, 	GPIO.OUT)
	GPIO.setup(thermistor_MUX_A2, 	GPIO.OUT)
	GPIO.setup(FB_MUX_A0, 			GPIO.OUT)	
	GPIO.setup(FB_MUX_A1, 			GPIO.OUT)	
	
	#Initialize GPIOs to low state
	GPIO.output(systemPowerEnable, 		GPIO.LOW)
	GPIO.output(meterHeaterFET, 		GPIO.LOW)
	GPIO.output(gearboxHeaterFET, 		GPIO.LOW)
	GPIO.output(arrestmentHeaterFET, 	GPIO.LOW)
	GPIO.output(conningTowerFET, 		GPIO.LOW)
	GPIO.output(icHeaterFET, 			GPIO.LOW)
	# GPIO.output(rtcReset, 				GPIO.LOW)
	GPIO.output(levelsReset, 			GPIO.LOW)	
	
	GPIO.output(MUX_A0, 				GPIO.LOW)	
	GPIO.output(MUX_A1, 				GPIO.LOW)
	GPIO.output(MUX_A2, 				GPIO.LOW)
	GPIO.output(thermistor_MUX_A0, 		GPIO.LOW)
	GPIO.output(thermistor_MUX_A1, 		GPIO.LOW)
	GPIO.output(thermistor_MUX_A2, 		GPIO.LOW)
	GPIO.output(FB_MUX_A0, 				GPIO.LOW)	
	GPIO.output(FB_MUX_A1, 				GPIO.LOW)
	
def setMux(a0, a1, a2, debug):
		if (a0 == 1):
			GPIO.output(MUX_A0, 				GPIO.HIGH)
			if (debug):
				print "MUX_A0 set to high"
		else:
			GPIO.output(MUX_A0, 				GPIO.LOW)
			if (debug):
				print "MUX_A0 set to low"
		if (a0 == 1):
			GPIO.output(MUX_A1, 				GPIO.HIGH)
			if (debug):
				print "MUX_A1 set to high"
		else:
			GPIO.output(MUX_A1, 				GPIO.LOW)
			if (debug):
				print "MUX_A1 set to low"
		if (a0 == 1):
			GPIO.output(MUX_A2, 				GPIO.HIGH)
			if (debug):
				print "MUX_A2 set to high"
		else:
			GPIO.output(MUX_A2, 				GPIO.LOW)	
			if (debug):
				print "MUX_A2 set to low"
		

def setFBMux(a0, a1, debug):
		if (a0 == 1):
			GPIO.output(FB_MUX_A0, 				GPIO.HIGH)
			if (debug):
				print "FB_MUX_A0 set to high"
		else:
			GPIO.output(FB_MUX_A0, 				GPIO.LOW)
			if (debug):
				print "FB_MUX_A0 set to low"
		if (a1 == 1):
			GPIO.output(FB_MUX_A1, 				GPIO.HIGH)
			if (debug):
				print "FB_MUX_A1 set to high"
		else:
			GPIO.output(FB_MUX_A1, 				GPIO.LOW)			
			if (debug):print "FB_MUX_A1 set to low"
			
			
def setThermistorMux(a0, a1, a2, debug):
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A0, 				GPIO.HIGH)
			if (debug):
				print "thermistor_MUX_A0 set to high"
		else:
			GPIO.output(thermistor_MUX_A0, 				GPIO.LOW)
			if (debug):
				print "thermistor_MUX_A0 set to low"
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A1, 				GPIO.HIGH)
			if (debug):
				print "thermistor_MUX_A1 set to high"
		else:
			GPIO.output(thermistor_MUX_A1, 				GPIO.LOW)
			if (debug):
				print "thermistor_MUX_A1 set to low"
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A2, 				GPIO.HIGH)
			if (debug):
				print "thermistor_MUX_A2 set to high"
		else:
			GPIO.output(thermistor_MUX_A2, 				GPIO.LOW)
			if (debug):
				print "thermistor_MUX_A2 set to low"


def setHeater(meterHeater, gearboxHeater,  arrestmentHeater, conningTowerHeater, debug):
	
		if (meterHeater == 1):
			GPIO.output(meterHeaterFET, 				GPIO.HIGH)
			if (debug):
				print "meterHeaterFET set to high"
		else:
			GPIO.output(meterHeaterFET, 				GPIO.LOW)
			if (debug):
				print "meterHeaterFET set to low"
		if (gearboxHeater == 1):
			GPIO.output(gearboxHeaterFET, 				GPIO.HIGH)
			if (debug):
				print "gearboxHeater set to high"
		else:
			GPIO.output(gearboxHeaterFET, 				GPIO.LOW)
			if (debug):
				print "gearboxHeater set to low"

		if (arrestmentHeater == 1):
			GPIO.output(arrestmentHeaterFET, 			GPIO.HIGH)
			if (debug):
				print "arrestmentHeater set to high"
		else:
			GPIO.output(arrestmentHeaterFET, 			GPIO.LOW)
			if (debug):
				print "arrestmentHeater set to low"
			
		if (conningTowerHeater == 1):
			GPIO.output(conningTowerFET, 				GPIO.HIGH)
			if (debug):
				print "conningTowerHeater set to high"
		else:
			GPIO.output(conningTowerFET, 				GPIO.LOW)
			if (debug):
				print "conningTowerHeater set to low"
		
zlsInit(debug)		
	   	
# setMux(1,1,1,debug)
# setThermistorMux(1,1,1,debug)
# setFBMux(1,1,debug)
setHeater(1, 0, 0, 0, debug)
	   	
