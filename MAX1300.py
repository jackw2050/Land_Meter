#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0


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

while True:

    spi.writebytes([CHAN0_READ])
    print "Preparing to sleep..."
    time.sleep(.01)
    print "Done sleeping.  Reading bytes"
    chan0_data = spi.readbytes(2)
    # print chan0_data
    # print chan0_data[0]
    # print chan0_data[1]
    # print (chan0_data[0]<<8 )
    
    chan0_16bit_data = (chan0_data[0]<<8 ) + chan0_data[1]
    dec_data = 1.0 * chan0_16bit_data
    print chan0_16bit_data
    print  dec_data / 65535 * 6
    
    
      
# hex_string =  hex(GET_CHAN0_DATA)
# print hex_string
# int_number = int(hex_string,0)
# print int_number
