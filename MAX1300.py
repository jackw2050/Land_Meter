#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0


class MCP3(object):
    """Class to represent an Adafruit MCP3008 analog to digital converter.
    """

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

class MAX1300:


	MUX0	= 0x00   
	MUX1	= 0x02

	VBIAS	= 0x01
	SYS0	= 0x03

	OFC0	= 0x04
	OFC1	= 0x05
	OFC2	= 0x06

INTERNAL_CLOCK =    0xA8
CHAN0_FULL_12V_RANGE_SINGLE = 0x80
CHAN0_FULL_6V_RANGE_SINGLE = 0x84
CHAN0_6V_RANGE_SINGLE = 0x83#0x81

CHAN1_FULL_RANGE_SINGLE = 145
CHAN0_READ   = 0x80
CHAN1_READ = 0x90


# internal clock  10101000
# CHAN0_6V_RANGE_SINGLE = 10000011



def RegWrite(reg,val):
	spi.xfer2([ADS1248.WREG+(reg & 0xF),0x00,val]);
	return False

def RegRead(reg):
	spi.xfer2([ADS1248.RREG+(reg & 0xF),00]);
	r = spi.xfer2([0x00]); # dummy
	return r
	
def ReadADC():
	spi.writebytes([ADS1248.RDATA]) # RDATA (read data once, page 49)
	a=spi.readbytes(3)
	spi.writebytes([ADS1248.NOP]) # sending NOP

	return a

def ADCinit():	
	RegWrite(ADS1248.MUX0, 0b00000001);	# MUX0:  Pos. input: AIN0, Neg. input: AIN1 (Burnout current source off) 
	
	print "MUX0:  Pos. input: AIN0, Neg. input: AIN1 (Burnout current source off) "
	RegWrite(ADS1248.MUX1, 0b00100000);	# MUX1:  REF0, normal operation
	print "MUX1:  REF0, normal operation"
	RegWrite(ADS1248.SYS0, 0b00000000);	# SYS0:  PGA Gain = 1, 5 SPS
	RegWrite(ADS1248.IDAC0,0b00000000);	# IDAC0: off
	RegWrite(ADS1248.IDAC1,0b11001100);	# IDAC1: n.c.
	RegWrite(ADS1248.VBIAS,0b00000000);	# VBIAS: BIAS voltage disabled
 	RegWrite(ADS1248.OFC0, 0b00000000);	# OFC0:  0 => reset offset calibration
	RegWrite(ADS1248.OFC1, 0b00000000);	# OFC1:  0 => reset offset calibration
	RegWrite(ADS1248.OFC2, 0b00000000);	# OFC2:  0 => reset offset calibration
	RegWrite(ADS1248.GPIOCFG, 0b00000000);	# GPIOCFG: all used as analog inputs
	RegWrite(ADS1248.GPIODIR, 0b00000000);	# GPIODIR: -
	RegWrite(ADS1248.GPIODAT, 0b00000000);	# GPIODAT: -





spi = SPI(0,0)	#/dev/spidev1.0
spi.msh=100000 # SPI clock set to 100 kHz
spi.bpw = 8  # bits/word
spi.threewire = False
spi.lsbfirst = False
spi.mode = 0
spi.cshigh = False  # ADS1248 chip select (active low)
spi.open(0,0)






RESET = 200

GET_CHAN0_DATA = int("0x80",0) 
GET_CHAN1_DATA = 145
#Only need to execute one of the following lines:
#spi = SPI(bus, device) #/dev/spidev<bus>.<device>
# Enable SPI 0 Chip select 0
# spi = SPI(0,0)
# Set max frequency to 1MHz
# spi.msh = 1000000

# spi.threewire = False
# spi.lsbfirst = False
# spi.cshigh = False
# spi.mode = 0


spi.writebytes([INTERNAL_CLOCK])
spi.writebytes([0x83])

print "Using interanl clock"

# while True:
data_val = 0
for x in range (100):

    spi.writebytes([CHAN0_READ])
    print "Preparing to sleep..."
    time.sleep(.1)
    print "Done sleeping.  Reading bytes"
    chan0_data = spi.readbytes(2)
    # print chan0_data
    # print chan0_data[0]
    # print chan0_data[1]
    # print (chan0_data[0]<<8 )
    
    chan0_16bit_data = (chan0_data[0]<<8 ) + chan0_data[1]
    dec_data = 1.0 * chan0_16bit_data
    # print chan0_16bit_data
    data_val = data_val + dec_data / 65535 * (4.096 *1.5)
    
    print "data ", 0, "is ", dec_data / 65535 * (4.096 *1.5)
    print "sum = ", data_val
print "Average of ", x + 1, "readings is ", data_val / (x + 1)    
      
# hex_string =  hex(GET_CHAN0_DATA)
# print hex_string
# int_number = int(hex_string,0)
# print int_number
