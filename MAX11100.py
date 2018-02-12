from Adafruit_BBIO.SPI import SPI
# alt use spidev
import time
#https://github.com/adafruit/adafruit-beaglebone-io-python
# Constants




VREF = 4.096
z = time.time()	
spi = SPI(1,0) # 1, 0 is what used to be 0,0
#spi.fd = -1;
spi.mode = 3;
spi.bpw = 8;#Bits per word
spi.msh=1000000
y = time.time()	
print y - z


def ReadADC_average( chan,averages, delay, vref):
	""" Returns average of averages measurments.
		rate is mS 
		loopMax is number of measurements
	"""

	data_summ = 0.0
	data_val = 0.0
	
	for x in range (averages):
		data_summ += self.ReadADC(chan)							
		time.sleep(delay)
		
	data_val = data_summ / (averages )
	data_val = chan_16bit_data / 65535.0
	data_val *= vref

	return data_val		
	
	



def adc_read_value(raw_data, vref):
	actual_value = 1.0
	actual_value *= vref
	return actual_value


def ReadADC(chan, vref):
	""" Returns a single measurment.
	"""
	chan_16bit_data = 0.0
	data_val = 0.0
	rVolt = 0.0
	iVal = 0.0
	chan_data = spi.readbytes(3)	# Read garbage byte.  Not sure why this is necessary
	# print "Raw data ",hex(chan_data[1]),hex(chan_data[2])
	
	chan_16bit_data = (chan_data[1]<<8 ) + chan_data[2]	# Convert to one 16 bit word
	# print chan_16bit_data
	# print data_val
	data_val = chan_16bit_data / 65535.0
	data_val *= vref
	# rVolt = 5.0 - data_val
	# iVal = rVolt / 6980.0
	# rVal = data_val / iVal
	
	return data_val
	
	
def RegWrite():
	spi.xfer2([ 0xFF,0x63]);
	# time.sleep(10)
	return False	
	
# while (True):
# 	print ReadADC(0, VREF)
# 	time.sleep(1)
# 	RegWrite()
	
# spi.xfer2([ 0xFF,0x63]);