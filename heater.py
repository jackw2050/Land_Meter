#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0
AVG_COUNT = 250
#[name, enable, address, low_setpoint, high_setpoint, status(on'True' or off'False'), temperature(deg C)]
conning_tower_heater =  ['Conning Tower', True, 2, 125,125, False, 26]
arrestment_heater =     ['Arrestment', True, 2, 125,125, False, 26]
meter_heater =          ['Meter', True, 2, 125,125, False, 26]
gearbox_tower_heater =  ['Gearbox', True, 2, 125,125, False, 26]
ic_heater =             ['IC', True, 2, 125,125, False, 26]



heaterList = [conning_tower_heater, arrestment_heater, meter_heater, gearbox_tower_heater, ic_heater]


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
    thermistorValue = 0
    localHeaterList = hList
    for i in range (len(localHeaterList)):
        
        # get adc value
        localHeaterList[i][6] = convertThermistorToTemp(thermistorValue, 'C')
        print(localHeaterList[i][0])
   
checkHeaterTemp(heaterList)        