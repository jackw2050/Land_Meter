from Adafruit_BBIO.SPI import SPI
import time
#https://github.com/adafruit/adafruit-beaglebone-io-python
spi = SPI(1,0) 

#spi.fd = -1;
spi.mode = 3;
#spi.bpw = 8;#Bits per word
spi.msh=1250000




time.sleep(.300)

#spi.lsbfirst = True
time.sleep(.300)


def readLong():
    x = 0
    time.sleep(.001)
    spi.writebytes([0x33])
    time.sleep(.001)
    x_high_data = spi.readbytes(1)
    time.sleep(.001)
    x = x_high_data[0] << 8
    spi.writebytes([0x34])
    time.sleep(.001)
    x_low_data = spi.readbytes(1)
    x += x_low_data[0]
    longAdc = 0.0
    longAdc += x - 32768
    #y -= 32768
    return longAdc

def readCross():
    x = 0
    spi.writebytes([0x31])
    time.sleep(.001)
    x_high_data = spi.readbytes(1)
    time.sleep(.001)
    x = x_high_data[0] << 8
    spi.writebytes([0x32])
    time.sleep(.001)
    x_low_data = spi.readbytes(1)
    x += x_low_data[0]
    crossAdc = 0.0
    crossAdc += x - 32768
    #y -= 32768
    return crossAdc


def readLevelTemperature():
    x = 0
    spi.writebytes([0x35])
    time.sleep(.001)
    x_high_data = spi.readbytes(1)
    time.sleep(.001)
    # print x_high_data
    x = x_high_data[0] << 2
    spi.writebytes([0x36])
    time.sleep(.001)
    x_low_data = spi.readbytes(1)
    # print x_low_data
    x += x_low_data[0]
    outputVoltage = 0.0
    tempAdc = 0.0
    tempAdc += x 
    print "tempADC ", tempAdc
    outputVoltage = tempAdc / 1023 * 3.3
    print "Output voltage = ", outputVoltage
    boardTemp = (outputVoltage - 0.5) / 0.010

    
    print "Board temp = ", boardTemp

    return tempAdc
    
    
    
def readLevelsAvg():
    crossSumm = 0.0
    longSumm = 0.0
    levelsAvg = (0.0),(0.0)
    averageCount = 10
    for i in range (10):
        crossSumm += readCross()
        longSumm += readLong()
    levelsAvg[0] = crossSumm / averageCount
    levelsAvg[1] = longSumm / averageCount
    #levelsAvg = [crossSumm / averageCount], [longSumm / averageCount]
    
    return levelsAvg
    
    
while(True):

    spi.writebytes([0x39])      # Update data
    time.sleep(.5)
    # crossData = readCross()
    # longData = readLong()
    # print "Cross\t", crossData, "\t\tLong\t", longData
    levelData = readLevelsAvg()


    print "Cross\t", levelData[0], "\t\tLong\t", levelData[1]

   