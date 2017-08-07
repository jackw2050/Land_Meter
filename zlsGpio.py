import Adafruit_BBIO.GPIO as GPIO
import time

class ZLSGPIO(object):		
    """Base class for GPIO functions. 
    """

    system9VoltEnable   = "P8_10"
    systemPowerEnable   = "P8_22"
    
    meterHeaterFET      = "P8_3"
    gearboxHeaterFET    = "P8_4"
    arrestmentHeaterFET = "P8_5"
    conningTowerFET     = "P8_6"
    icHeaterFET         = "P8_19"
    
    levelsReset         = "P8_28"
    
    rtc1Hz              = "P8_29"
    rtcReset            = "P8_30"
    
    
    
    #Enable GPIO for system power DC-DC converters
    GPIO.setup(systemPowerEnable, GPIO.OUT)
    GPIO.setup(system9VoltEnable, GPIO.OUT)
    
    #Enable GPIO heater for heater FETs
    GPIO.setup(meterHeaterFET, GPIO.OUT)
    GPIO.setup(gearboxHeaterFET, GPIO.OUT)
    GPIO.setup(arrestmentHeaterFET, GPIO.OUT)
    GPIO.setup(conningTowerFET, GPIO.OUT)
    GPIO.setup(icHeaterFET, GPIO.OUT)
    

    
    #Enable GPIO for levels
    GPIO.setup(levelsReset, GPIO.OUT)
    
    
    
    #Initialize GPIOs to low state
    def ADCinit(self):	
        GPIO.output(systemPowerEnable, GPIO.LOW)
        GPIO.output(system9VoltEnable, GPIO.LOW)
        GPIO.output(meterHeaterFET, GPIO.LOW)
        GPIO.output(gearboxHeaterFET, GPIO.LOW)
        GPIO.output(arrestmentHeaterFET, GPIO.LOW)
        GPIO.output(conningTowerFET, GPIO.LOW)
        GPIO.output(icHeaterFET, GPIO.LOW)
        
        GPIO.output(rtcReset, GPIO.LOW)
        GPIO.output(levelsReset, GPIO.LOW)
       