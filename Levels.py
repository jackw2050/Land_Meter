# import file_opsfile_op as file_op
# Code requirements

#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
#	Notes
# Add mux to one chanel of MAX1300 for system voltage measurements. (12V, +/- 5V, 3.3V, 36V, Beam volt, 9V and precision volatage reference)




def ini_levels():
	
	check_ok = 0
	update_data = 0x39
	
	# spi.set_clock_hz(1000000)
	# spi.set_mode(0)
	# spi.set_bit_order(SPI.MSBFIRST)
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
	

	print "SPI port ", SPI_PORT, "  ", SPI_DEVICE, " open"



def get_level_data():
	spi.writebytes([update_data])		# Update data
	print "update data sent"
	time.sleep(1)
	print "delay completed"
	spi.writebytes([0x31])
	time.sleep(1)
	print "reading high byte"
	x_high_data = spi.readbytes(2)
	time.sleep(1)
	print "high byte = ", x_high_data
	spi.writebytes([0x32])
	time.sleep(1)
	x_low_data = spi.readbytes(2)
	print "low byte = ", x_low_data
	
def get_levels_temp():
	print "hi"
	
def byte2word(high_byte, low_byte):
	word = 0
	return word
	
def get_level_in_arc_sec(adc_val):
	level = 1.0
	adc_range 		= 65536
	adc_mid 		= 32768
	level_arc_sec 	= 0
	level_range 	= 3600.0 #arc Seconds
	adc_step = level_range / adc_range

	adc_val = adc_val - adc_mid
	level = adc_val * adc_step
	
	level_deg = int(level / level_range / 2)
	print 'deg ', level_deg
	level_arc_min = int(level - level_deg)
	level_arc_min = int(level_arc_min / 60)
	print 'minutes ', level_arc_min
	level_arc_sec = (level - level_deg) / 60 - level_arc_min
	level_arc_sec *= 60
	print 'seconds', level_arc_sec
	
	level_out = ""
	level_out = str(level_deg), " deg ", level_arc_min, " min "  ,level_arc_sec, " sec"
	return level_out
	