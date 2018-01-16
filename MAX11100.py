from Adafruit_BBIO.SPI import SPI
import time
#https://github.com/adafruit/adafruit-beaglebone-io-python
# Constants

class MAX11100:


	VREF = 4.096
		
	spi = SPI(0,0) 
	#spi.fd = -1;
	spi.mode = 3;
	spi.bpw = 8;#Bits per word
	spi.msh=1000000
	
	
	
	def ReadADC_average(self, chan,averages, delay):
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

		return data_val		
		
		



	def adc_read_value(self, raw_data):
		actual_value *= self.VREF
		return actual_value

	
	def ReadADC(self,chan):
		""" Returns a single measurment.
		"""
		chan_16bit_data = 0.0
		chan_data = spi.readbytes(3)	# Read garbage byte.  Not sure why this is necessary
	# 	print "Raw data ",hex(chan_data[1]),hex(chan_data[2])
		
		chan_16bit_data = (chan_data[1]<<8 ) + chan_data[2]	# Convert to one 16 bit word
		data_val = chan_16bit_data / 65535.0


		return adc_read_value(data_val)
		
		
		
		
		
		
	print ReadADC_average(0,1000, 0)
	