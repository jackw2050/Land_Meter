
from Adafruit_BBIO.SPI import SPI
import time


# Constants

VREF = 4.096
INTERNAL_CLOCK = 0xA8

CHAN0_VRANGE = [0, VREF * 3]
CHAN1_VRANGE = [0, VREF * 3]
CHAN2_VRANGE = [0, VREF * 3]
CHAN3_VRANGE = [0, VREF * 3]
CHAN4_VRANGE = [0, VREF * 3]
CHAN5_VRANGE = [0, VREF * 3]
CHAN6_VRANGE = [0, VREF * 3]
CHAN7_VRANGE = [0, VREF * 3]

CHAN0 = 0x80
CHAN1 = 0x90
CHAN2 = 0xA0
CHAN3 = 0xB0
CHAN4 = 0xC0
CHAN5 = 0xD0
CHAN6 = 0xE0
CHAN7 = 0xF0
	
	
# Single ended
RANGE_SINGLE_MINUS_3_VREF_PLUS_3_VREF 		= 0x07				# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
RANGE_SINGLE_ZERO_PLUS_3_VREF 				= 0x06				# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
RANGE_SINGLE_MINUS_3_VREF_ZERO 				= 0x05				# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
RANGE_SINGLE_MINUS_1P5_VREF_PLUS_1P5_VREF 	= 0x04				# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
RANGE_SINGLE_ZERO_1P5_VREF 					= 0x03				# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.
RANGE_SINGLE_MINUS_1P5_VREF_ZERO 			= 0x02				# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
RANGE_SINGLE_MINUS_P75_VREF_PLUS_P75_VREF 	= 0x01				# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

# Differential

RANGE_DIFFERENTIAL_MINUS_3_VREF_PLUS_3_VREF  	= 0x0F			# Bipolar -6 x VREF to +6 x VREF. FSR = 12 x VREF
RANGE_DIFFERENTAL_MINUS_3_VREF_PLUS_3_VREF 		= 0x0C			# Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF.
RANGE_DIFFERENTIAL_MINUS_1P5_VREF_PLUS_1P5_VREF = 0x04			# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.



SPI_PORT = 0
SPI_DEVICE = 0
# SPI setup

spi = SPI(SPI_PORT,SPI_DEVICE)			#/dev/spidev1.0
spi.msh=100000 			# SPI clock set to 100 kHz
spi.bpw = 8  			# bits/word

spi.lsbfirst = False

# spi.open(0,0)
spi.open(SPI_PORT,SPI_DEVICE)


	
def ADCinit():	

	# Defaults
	print("Initialling MAX1300 ADC to use internal clock reference")
	spi.writebytes([INTERNAL_CLOCK])		# Use internal clock
	time.sleep(1)
	
	print 'Initializing MAX1300 ADC Chan 0 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN0 + RANGE_SINGLE_ZERO_PLUS_3_VREF])	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	print 'Initializing MAX1300 ADC Chan 1 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN1 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 2 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN2 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 3 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN3 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 4 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN4 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 5 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN5 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 6 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN6 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 7 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	spi.writebytes([CHAN7 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
	print 'Initializing MAX1300 ADC Chan 7 range to Unipolar 0 to +3 x VREF. FSR =', 3 * VREF, "V"
	time.sleep(1)
	
	CHAN0_VRANGE = [0, VREF * 3]
	CHAN1_VRANGE = [0, VREF * 3]
	CHAN2_VRANGE = [0, VREF * 3]
	CHAN3_VRANGE = [0, VREF * 3]
	CHAN4_VRANGE = [0, VREF * 3]
	CHAN5_VRANGE = [0, VREF * 3]
	CHAN6_VRANGE = [0, VREF * 3]
	CHAN7_VRANGE = [0, VREF * 3]




def GetChanVrange(self, range_setting):

	self.range_setting = range_setting
	vrange = [0,0]

	if self.range_setting == RANGE_SINGLE_MINUS_3_VREF_PLUS_3_VREF:
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_ZERO_PLUS_3_VREF :	
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_MINUS_3_VREF_ZERO :
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_MINUS_1P5_VREF_PLUS_1P5_VREF 	:
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_ZERO_1P5_VREF : 	
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_MINUS_1P5_VREF_ZERO :	
		vrange[0] = 0
	if self.range_setting == RANGE_SINGLE_MINUS_P75_VREF_PLUS_P75_VREF :	
		vrange[0] = 0



def GetChanVrange(self, range_setting):
	# Returns the offset and full channel range for any setting
	
	chan_setting = [0,0]
	if ( channel == 0):
		setting = setting - 0x80
	elif channel == 1:
		setting = setting - 0x90
	elif channel == 2:
		setting = setting - 0xA0		
	elif channel == 3:
		setting = setting - 0xB0	
	elif channel == 4:
		setting = setting - 0xC0	
	elif channel == 5:
		setting = setting - 0xD0	
	elif channel == 6:
		setting = setting - 0xE0	
	elif channel == 7:
		setting = setting - 0xF0		

	if setting == RANGE_SINGLE_MINUS_3_VREF_PLUS_3_VREF:
		chan_setting[0] = VREF * -3
		chan_setting[1] = VREF * 6
		return chan_setting 
	elif setting == RANGE_SINGLE_ZERO_PLUS_3_VREF:
		chan_setting[0] = 0
		chan_setting[1] = VREF * 3
		return chan_setting 
	elif setting == RANGE_SINGLE_MINUS_3_VREF_ZERO:
		chan_setting[0] = VREF * -3
		chan_setting[1] = VREF * 3
		return chan_setting 
	elif setting == RANGE_SINGLE_MINUS_1P5_VREF_PLUS_1P5_VREF:
		chan_setting[0] = VREF * -1.5
		chan_setting[1] = VREF * 3
		return chan_setting 
	elif setting == RANGE_SINGLE_ZERO_1P5_VREF:
		chan_setting[0] = 0
		chan_setting[1] = VREF * 1.5
		return chan_setting 
	elif setting == RANGE_SINGLE_MINUS_1P5_VREF_ZERO:
		chan_setting[0] = VREF * -1.5
		chan_setting[1] = VREF * 1.5
		return chan_setting 
	elif setting == RANGE_SINGLE_MINUS_P75_VREF_PLUS_P75_VREF:
		chan_setting[0] = VREF * -.75
		chan_setting[1] = VREF * 1.5


	# Differential
	elif setting == RANGE_DIFFERENTIAL_MINUS_3_VREF_PLUS_3_VREF:
		chan_setting[0] = VREF * -6
		chan_setting[1] = VREF * 12
	elif setting == RANGE_DIFFERENTAL_MINUS_3_VREF_PLUS_3_VREF:
		chan_setting[0] = VREF * -3
		chan_setting[1] = VREF * 6
	elif setting == RANGE_DIFFERENTIAL_MINUS_1P5_VREF_PLUS_1P5_VREF:
		chan_setting[0] = VREF * -1.5
		chan_setting[1] = VREF * 3

	else: return -999


	return chan_setting 

				



def ReadADC_average(adc_chan, chan_vrange, averages, rate, loopMax, divider, offset):
	""" Returns average of averages measurments.
		rate is mS 
		loopMax is number of measurements
	"""
	chanVrange = [0,0]
	if (adc_chan == "beam"):
		chan = 0x80
		chanVrange[0] = CHAN0_VRANGE[0]
		chanVrange[1] = CHAN0_VRANGE[1]
	elif (adc_chan == "m5vSys"):	
		chan = 0x90
		chanVrange[0] = CHAN1_VRANGE[0]
		chanVrange[1] = CHAN1_VRANGE[1]
	if (adc_chan == "zpSys"):
		chan = 0xA0
		chanVrange[0] = CHAN2_VRANGE[0]
		chanVrange[1] = CHAN2_VRANGE[1]
	if (adc_chan == "meterThermistor1"):
		chan = 0xB0
		chanVrange[0] = CHAN3_VRANGE[0]
		chanVrange[1] = CHAN3_VRANGE[1]
	if (adc_chan == "meterThermistor2"):
		chan = 0xC0
		chanVrange[0] = CHAN4_VRANGE[0]
		chanVrange[1] = CHAN4_VRANGE[1]
	if (adc_chan == "gearboxThermistor"):
		chan = 0xD0
		chanVrange[0] = CHAN5_VRANGE[0]
		chanVrange[1] = CHAN5_VRANGE[1]
	if (adc_chan == "arrestmentThermistor"):
		chan = 0xE0
		chanVrange[0] = CHAN6_VRANGE[0]
		chanVrange[1] = CHAN6_VRANGE[1]
	if (adc_chan == "conningTowerThermistor"):
		chan = 0xF0
		chanVrange[0] = CHAN7_VRANGE[0]
		chanVrange[1] = CHAN7_VRANGE[1]
	



	data_summ = 0
	data_val = 0
	for x in range (loopMax):
		spi.writebytes([chan])								# Send request for data
		chan_data = spi.readbytes(2)						# Read 2 bytes
		chan_16bit_data = (chan_data[0]<<8 ) + chan_data[1]	# Convert to one 16 bit word
		dec_data = chan_16bit_data / 65535 * chanVrange[1] + chanVrange[0]
		data_summ += dec_data
		time.sleep(rate / 1000)
	data_val = data_summ / loopMax
	data_val = data_val * divider + offset
	
	return data_val	
		


def RegWrite( reg,val):
	spi.xfer2([ADS1248.WREG+(reg & 0xF),0x00,val]);
	return False

def RegRead(reg):
	spi.xfer2([ADS1248.RREG+(reg & 0xF),00]);
	r = spi.xfer2([0x00]); # dummy
	return r
	
def ReadADC(chan, chan_vrange):

	""" Returns a single measurment.

	"""
	chan = chan
	chan_vrange = chan_vrange

	spi.writebytes([chan])								# Send request for data
	chan0_data = spi.readbytes(2)							# Read 2 bytes
	chan0_16bit_data = (chan0_data[0]<<8 ) + chan0_data[1]	# Convert to one 16 bit word
	data_val = chan0_16bit_data / 65535 * CHAN0_VRANGE[1] + CHAN0_VRANGE[0]

	return data_val	
		
		
		
		