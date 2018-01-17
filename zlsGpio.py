import Adafruit_BBIO.GPIO as GPIO
import time


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





def zlsInit():
	#Enable GPIO for system power DC-DC converters
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
	
def setMux(a0, a1, a2):
		if (a0 == 1):
			GPIO.output(MUX_A0, 				GPIO.HIGH)
			print "A0 set to high"
		else:
			GPIO.output(MUX_A0, 				GPIO.LOW)
		if (a0 == 1):
			GPIO.output(MUX_A1, 				GPIO.HIGH)
		else:
			GPIO.output(MUX_A1, 				GPIO.LOW)
		if (a0 == 1):
			GPIO.output(MUX_A2, 				GPIO.HIGH)
		else:
			GPIO.output(MUX_A2, 				GPIO.LOW)	
		

def setFBMux(a0, a1):
		if (a0 == 1):
			GPIO.output(FB_MUX_A0, 				GPIO.HIGH)
			print "A0 set to high"
		else:
			GPIO.output(FB_MUX_A0, 				GPIO.LOW)
		if (a1 == 1):
			GPIO.output(FB_MUX_A1, 				GPIO.HIGH)
			print "A0 set to high"
		else:
			GPIO.output(FB_MUX_A1, 				GPIO.LOW)			

			
			
def setThermistorMux(a0, a1, a2):
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A0, 				GPIO.HIGH)
		else:
			GPIO.output(thermistor_MUX_A0, 				GPIO.LOW)
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A1, 				GPIO.HIGH)
		else:
			GPIO.output(thermistor_MUX_A1, 				GPIO.LOW)
		if (a0 == 1):
			GPIO.output(thermistor_MUX_A2, 				GPIO.HIGH)
		else:
			GPIO.output(thermistor_MUX_A2, 				GPIO.LOW)


def setHeater(meterHeater, gearboxHeater,  arrestmentHeater, conningTower):
		if (meterHeater == 1):
			GPIO.output(meterHeaterFET, 				GPIO.HIGH)
		else:
			GPIO.output(meterHeaterFET, 				GPIO.LOW)
			
		if (gearboxHeater == 1):
			GPIO.output(gearboxHeaterFET, 				GPIO.HIGH)
		else:
			GPIO.output(gearboxHeaterFET, 				GPIO.LOW)

		if (arrestmentHeater == 1):
			GPIO.output(arrestmentHeaterFET, 			GPIO.HIGH)
		else:
			GPIO.output(arrestmentHeaterFET, 			GPIO.LOW)
			
		if (conningTower == 1):
			GPIO.output(conningTowerFET, 				GPIO.HIGH)
		else:
			GPIO.output(conningTowerFET, 				GPIO.LOW)			
		
zlsInit()		
	   	
setMux(1,1,1)
setThermistorMux(1,1,1)
setFBMux(1,0)
setHeater(1, 1, 1, 1)


	   	
