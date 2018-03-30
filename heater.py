#import the library
import MAX1300
import time
import Adafruit_BBIO.GPIO as GPIO



class heater:


def __inti__(self, name, low_setpoint, high_Setpoint, status, heater_fet, thermistor1, thermistor2):
    self.name = name
    self.low_setpoint = low_setpoint
    self.high_Setpoint = high_Setpoint
    self.status = status
    self.heater_fet = heater_fet
    self.thermistor1 = thermistor1
    self.thermistor2 = thermistor2


#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0
AVG_COUNT = 250
#                       [ name,             enable, low_setpoint,   high_setpoint,  status(on'True' or off'False'), temperature(deg C), ADC chan]
conning_tower_heater =  ['Conning Tower',   True,   125,            125,            False,                          26, 7]
arrestment_heater =     ['Arrestment',      True,   125,            125,            False,                          26, 6]
meter_heater =          ['Meter',           True,   125,            125,            False,                          26, 26, 3, 4]
gearbox_heater =        ['Gearbox',         True,   125,            125,            False,                          26, 5]


conningTowerFET = "P8_6"
arrestmentFET   = "P8_5"
gearboxFET      = "P8_4" 
meterFET        = "P8_3"
icHeaterFET     = "P8_14"



heaterList = [conning_tower_heater, arrestment_heater, meter_heater, gearbox_heater]

def heaterInit(self):
    GPIO.setup(conningTowerFET, GPIO.OUT)
    GPIO.setup(arrestmentFET  , GPIO.OUT)
    GPIO.setup(gearboxFET     , GPIO.OUT)
    GPIO.setup(meterFET       , GPIO.OUT)
    GPIO.setup(icHeaterFET    , GPIO.OUT)

def updateHeater(self,heater, newStatus):
    if(heater == 'conning_tower'):
        heaterName = conningTowerFET
    elif(heater == 'Arrestment'):
        heaterName = arrestmentFET
    elif(heater == 'Meter'):
        heaterName = meterFET
    elif(heater == 'Gearbox'):
        heaterName = gearboxFET    
       
    if(newStatus == True):
        GPIO.output(heaterName, GPIO.HIGH)
    else:
        GPIO.output(heaterName, GPIO.LOW)
        
        
        
def setHeaterStatus(heater):
    for i in range (len(heater)):
        if(heater[i][6] < heater[i][3]):
            updateHeater(heater[i][0], True)
            heater[i][5] = True
        else:
            updateHeater(heater[i][0], False)
            heater[i][5] = False


def convertThermistorToTemp(thermistorResistance, system):
    temperatureC = thermistorResistance / 250
    
    if(system == 'C'):
        return temperatureC
    else:
        temperatureF = temperatureC * 1.8 + 32
        return temperatureF

def checkHeaterTemp(hList):
    #loop thourgh list and check temperatures
    # store value in list
    averages = 100
    measDelay = 0.0001
    thermistorValue = 0.0
    localHeaterList = hList
    for i in range (len(localHeaterList)):
        #ReadADC_average(adc_chan, averages, delay,  divider, offset)
        if(localHeaterList[i][0] == 'Meter'):
            reading1 = MAX1300.ReadADC_average(localHeaterList[i][7], averages, measDelay,  0, 1)
            localHeaterList[i][5] = convertThermistorToTemp(thermistorValue, 'C')
            reading2 = MAX1300.ReadADC_average(localHeaterList[i][8], averages, measDelay,  0, 1)
            localHeaterList[i][6] = convertThermistorToTemp(thermistorValue, 'C')
            thermistorValue = (reading1 + reading1) / 2

        # get adc value
            localHeaterList[i][6] = convertThermistorToTemp(thermistorValue, 'C')
        else:
            thermistorValue = MAX1300.ReadADC_average(localHeaterList[i][6], averages, measDelay,  0, 1)
            localHeaterList[i][6] = convertThermistorToTemp(thermistorValue, 'C')

            
    return localHeaterList
      
      
      
      

