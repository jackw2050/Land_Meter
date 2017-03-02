# Change to full module


#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI









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






class MAX1300M(object):		
    """Base class for Maxim MAX1300 16 bit ADC. 
    """


		def ADCinit(self):	

		# Defaults

		spi.writebytes([INTERNAL_CLOCK])		# Use internal clock


		spi.writebytes([CHAN0 + RANGE_SINGLE_ZERO_PLUS_3_VREF])	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
		spi.writebytes([CHAN1 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN2 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN3 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN4 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN5 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN6 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		spi.writebytes([CHAN7 + RANGE_SINGLE_ZERO_PLUS_3_VREF])
		
		CHAN0_VRANGE = [0, VREF * 3]
		CHAN1_VRANGE = [0, VREF * 3]
		CHAN2_VRANGE = [0, VREF * 3]
		CHAN3_VRANGE = [0, VREF * 3]
		CHAN4_VRANGE = [0, VREF * 3]
		CHAN5_VRANGE = [0, VREF * 3]
		CHAN6_VRANGE = [0, VREF * 3]
		CHAN7_VRANGE = [0, VREF * 3]



    def __init__(self, width, SPI_PORT, SPI_DEVICE):


    def __init__(self, clk=None, cs=None, miso=None, mosi=None, spi=None, gpio=None):
        """Initialize MAX31855 device with software SPI on the specified CLK,
        CS, and DO pins.  Alternatively can specify hardware SPI by sending an
        Adafruit_GPIO.SPI.SpiDev device in the spi parameter.
        """
        self._spi = None
        # Handle hardware SPI
        if spi is not None:
            self._spi = spi
        elif clk is not None and cs is not None and miso is not None and mosi is not None:
            # Default to platform GPIO if not provided.
            if gpio is None:
                gpio = GPIO.get_platform_gpio()
            self._spi = SPI.BitBang(gpio, clk, mosi, miso, cs)
        else:
            raise ValueError('Must specify either spi for for hardware SPI or clk, cs, miso, and mosi for softwrare SPI!')
        self._spi.set_clock_hz(1000000)
        self._spi.set_mode(0)
        self._spi.set_bit_order(SPI.MSBFIRST)







    	

    def _initialize(self):
    	SPI_PORT = 0
		SPI_DEVICE = 0
		# SPI setup
		
		spi = SPI(0,0)			#/dev/spidev1.0
		spi.msh=100000 			# SPI clock set to 100 kHz
		spi.bpw = 8  			# bits/word
		spi.threewire = False
		spi.lsbfirst = False
		spi.mode = 0
		spi.cshigh = False  	# ADS1248 chip select (active low)
		# spi.open(0,0)
		spi.open(SPI_PORT,SPI_DEVICE)
		self.ADCinit()



	def GetChanVrange(self, range_setting):

		self.range_setting = range_setting
		vrange = [0,0]

		if self.range_setting == RANGE_SINGLE_MINUS_3_VREF_PLUS_3_VREF:
			vrange[0] = 
		if self.range_setting == RANGE_SINGLE_ZERO_PLUS_3_VREF :				
		if self.range_setting == RANGE_SINGLE_MINUS_3_VREF_ZERO :				
		if self.range_setting == RANGE_SINGLE_MINUS_1P5_VREF_PLUS_1P5_VREF 	:
		if self.range_setting == RANGE_SINGLE_ZERO_1P5_VREF : 					
		if self.range_setting == RANGE_SINGLE_MINUS_1P5_VREF_ZERO :			
		if self.range_setting == RANGE_SINGLE_MINUS_P75_VREF_PLUS_P75_VREF :	



	def GetChanVrange(self, range_setting):
		# Returns the offset and full channel range for any setting
		
		chan_setting = [0,0]
		if ( channel == 0):
			setting = sertting - 0x80
		elif channel == 1:
			setting = sertting - 0x90
		elif channel == 2:
			setting = sertting - 0xA0		
		elif channel == 3:
			setting = sertting - 0xB0	
		elif channel == 4:
			setting = sertting - 0xC0	
		elif channel == 5:
			setting = sertting - 0xD0	
		elif channel == 6:
			setting = sertting - 0xE0	
		elif channel == 7:
			setting = sertting - 0xF0		
	
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

		else return -999


		return chan_setting 
	
					
	


	def ReadADC_average(self,chan, chan_vrange, averages, rate, loopMax):
		""" Returns average of averages measurments.
			rate is mS 
			loopMax is number of measurements
		"""
		self.chan = chan
		self.chan_vrange = chan_vrange
		self.averages = averages
		self.rate = rate
		self.loopMax = loopMax


		data_summ = 0
		data_val = 0
		for x in range (self.loopMax):
    		spi.writebytes([self.chan])								# Send request for data
    		chan0_data = spi.readbytes(2)							# Read 2 bytes
    		chan0_16bit_data = (chan0_data[0]<<8 ) + chan0_data[1]	# Convert to one 16 bit word
    		dec_data = chan0_16bit_data / 65535 * CHAN0_VRANGE[1] + CHAN0_VRANGE[0]
    		data_summ += dec_data
    		time.sleep(self.rate / 1000)
    	data_val = data_summ / loopMax
    	return data_val	
    		

	
	def RegWrite(self, reg,val):
		spi.xfer2([ADS1248.WREG+(reg & 0xF),0x00,val]);
		return False
	
	def RegRead(reg):
		spi.xfer2([ADS1248.RREG+(reg & 0xF),00]);
		r = spi.xfer2([0x00]); # dummy
		return r
		
	def ReadADC(self,chan, chan_vrange):
	
		""" Returns a single measurment.

		"""
		self.chan = chan
		self.chan_vrange = chan_vrange

    	spi.writebytes([self.chan])								# Send request for data
    	chan0_data = spi.readbytes(2)							# Read 2 bytes
    	chan0_16bit_data = (chan0_data[0]<<8 ) + chan0_data[1]	# Convert to one 16 bit word
    	data_val = chan0_16bit_data / 65535 * CHAN0_VRANGE[1] + CHAN0_VRANGE[0]

    	return data_val	
    		










