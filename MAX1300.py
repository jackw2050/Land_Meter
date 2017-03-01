#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0


# SPI setup

spi = SPI(0,0)	#/dev/spidev1.0
spi.msh=100000 # SPI clock set to 100 kHz
spi.bpw = 8  # bits/word
spi.threewire = False
spi.lsbfirst = False
spi.mode = 0
spi.cshigh = False  # ADS1248 chip select (active low)
spi.open(0,0)







class MAX1300M:


	MUX0	= 0x00   
	MUX1	= 0x02

	VBIAS	= 0x01
	SYS0	= 0x03

	OFC0	= 0x04
	OFC1	= 0x05
	OFC2	= 0x06

	INTERNAL_CLOCK =    0xA8
	CHAN0_FULL_12V_RANGE_SINGLE = 0x80 	# +/- 12V
	CHAN0_FULL_6V_RANGE_SINGLE = 0x84	# +/- 6V
	CHAN0_6V_RANGE_SINGLE = 0x83		# 0 - 6V

	VREF = 4.096
	# Single-Ended
	CHAN0_RANGE_6VREF = 0x87 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN0_RANGE_P3VREF = 0x86	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN0_RANGE_M3VREF = 0x85	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN0_RANGE_3VREF = 0x84	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN0_RANGE_P1P5VREF = 0x83	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN0_RANGE_M1P5VREF = 0x82	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN0_RANGE_1P5VREF = 0x81	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN1_RANGE_6VREF = 0x97 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN1_RANGE_P3VREF = 0x96	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN1_RANGE_M3VREF = 0x95	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN1_RANGE_3VREF = 0x94	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN1_RANGE_P1P5VREF = 0x93	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN1_RANGE_M1P5VREF = 0x92	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN1_RANGE_1P5VREF = 0x91	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN2_RANGE_6VREF = 0xA7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN2_RANGE_P3VREF = 0xA6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN2_RANGE_M3VREF = 0xA5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN2_RANGE_3VREF = 0xA4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN2_RANGE_P1P5VREF = 0xA3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN2_RANGE_M1P5VREF = 0xA2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN2_RANGE_1P5VREF = 0xA1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN3_RANGE_6VREF = 0xB7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN3_RANGE_P3VREF = 0xB6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN3_RANGE_M3VREF = 0xB5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN3_RANGE_3VREF = 0xB4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN3_RANGE_P1P5VREF = 0xB3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN3_RANGE_M1P5VREF = 0xB2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN3_RANGE_1P5VREF = 0xB1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN4_RANGE_6VREF = 0xC7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN4_RANGE_P3VREF = 0xC6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN4_RANGE_M3VREF = 0xC5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN4_RANGE_3VREF = 0xC4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN4_RANGE_P1P5VREF = 0xC3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN4_RANGE_M1P5VREF = 0xC2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN4_RANGE_1P5VREF = 0xC1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN5_RANGE_6VREF = 0xD7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN5_RANGE_P3VREF = 0xD6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN5_RANGE_M3VREF = 0xD5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN5_RANGE_3VREF = 0xD4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN5_RANGE_P1P5VREF = 0xD3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN5_RANGE_M1P5VREF = 0xD2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN5_RANGE_1P5VREF = 0xD1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN6_RANGE_6VREF = 0xE7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN6_RANGE_P3VREF = 0xE6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN6_RANGE_M3VREF = 0xE5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN6_RANGE_3VREF = 0xE4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN6_RANGE_P1P5VREF = 0xE3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN6_RANGE_M1P5VREF = 0xE2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN6_RANGE_1P5VREF = 0xE1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.

	CHAN7_RANGE_6VREF = 0xF7 	# DEFAULT SETTING.  Bipolar -3 x VREF to +3 x VREF. FSR = 6 x VREF
	CHAN7_RANGE_P3VREF = 0xF6	# Unipolar 0 to +3 x VREF. FSR = 3 x VREF.
	CHAN7_RANGE_M3VREF = 0xF5	# Unipolar -3 x VREF to 0. FSR = 3 x VREF.
	CHAN7_RANGE_3VREF = 0xF4	# Bipolar (-3 x VREF)/2 to (+3 x VREF)/2. FSR = 3 x VREF.
	CHAN7_RANGE_P1P5VREF = 0xF3	# Unipolar 0 to (+3 x VREF)/2. FSR = (+3 x VREF)/2.ß
	CHAN7_RANGE_M1P5VREF = 0xF2	# Unipolar (-3 x VREF)/2 to 0. FSR = (3 x VREF)/2.
	CHAN7_RANGE_1P5VREF = 0xF1	# Bipolar (-3 x VREF)/4 to (+3 x VREF)/4. Full-Scale Range (FSR) = (3 x VREF)/2.


	CHAN0_VRANGE = VREF * 6
	CHAN1_VRANGE = VREF * 6
	CHAN2_VRANGE = VREF * 6
	CHAN3_VRANGE = VREF * 6
	CHAN4_VRANGE = VREF * 6
	CHAN5_VRANGE = VREF * 6
	CHAN6_VRANGE = VREF * 6
	CHAN7_VRANGE = VREF * 6


	CHAN0_READ = 0x80
	CHAN1_READ = 0x90
	CHAN2_READ = 0xA0
	CHAN3_READ = 0xB0
	CHAN4_READ = 0xC0
	CHAN5_READ = 0xD0
	CHAN6_READ = 0xE0
	CHAN7_READ = 0xF0
		

# internal clock  10101000
# CHAN0_6V_RANGE_SINGLE = 10000011




def GetVrange(channel, setting, vref):

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

	if setting == 0x07:
		chan_setting[0] = vref * -3
		chan_setting[1] = vref * 6
		return chan_setting 
	elif setting == 0x06:
		chan_setting[0] = 0
		chan_setting[1] = vref * 3
		return chan_setting 
	elif setting == 0x05:
		chan_setting[0] = vref * -3
		chan_setting[1] = vref * 3
		return chan_setting 
	elif setting == 0x04:
		chan_setting[0] = vref * -1.5
		chan_setting[1] = vref * 3
		return chan_setting 
	elif setting == 0x03:
		chan_setting[0] = 0
		chan_setting[1] = vref * 1.5
		return chan_setting 
	elif setting == 0x02:
		chan_setting[0] = VREF * -1.5
		chan_setting[1] = vref * 1.5
		return chan_setting 
	elif setting == 0x01:
		chan_setting[0] = vref * -.75
		chan_setting[1] = vref * 1.5
		return chan_setting 

		return chan_setting 						














def RegWrite(reg,val):
	spi.xfer2([ADS1248.WREG+(reg & 0xF),0x00,val]);
	return False

def RegRead(reg):
	spi.xfer2([ADS1248.RREG+(reg & 0xF),00]);
	r = spi.xfer2([0x00]); # dummy
	return r
	
def ReadADC(chan, chan_setting):

	readAddr = 0x00
	if chan == 0x00:
		readAddr = CHAN0_READ
	elif chan = 0x01:
		readAddr = CHAN1_READ
	elif chan = 0x02:
		readAddr = CHAN2_READ
	elif chan = 0x03:
		readAddr = CHAN3_READ
	elif chan = 0x04:
		readAddr = CHAN4_READ
	elif chan = 0x05:
		readAddr = CHAN5_READ
	elif chan = 0x06:
		readAddr = CHAN6_READ
	elif chan = 0x07:
		readAddr = CHAN7_READ

	spi.writebytes([readAddr])
	time.sleep(.01)

	chan_data = spi.readbytes(2)
	chan_data_hex = (chan_data[0] << 8) + chan_data[1]
	chan_value = chan_data_hex * chan_setting[1] + chan_setting[0]


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
    
    print "data ", x, "is ", dec_data / 65535 * (4.096 *1.5)
    print "sum = ", data_val
print "Average of ", x + 1, "readings is ", data_val / (x + 1)    
      
# hex_string =  hex(GET_CHAN0_DATA)
# print hex_string
# int_number = int(hex_string,0)
# print int_number
