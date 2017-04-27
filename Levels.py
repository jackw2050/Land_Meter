# import file_opsfile_op as file_op

#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
#	Notes
# Add mux to one chanel of MAX1300 for system voltage measurements. (12V, +/- 5V, 3.3V, 36V, Beam volt, 9V and precision volatage reference)




def initialize_land():
	
	check_ok = 0
	# Sysyewm check.
	# 0)	Call init for all devices. (ssi, i2c etc.)
	# 1)	Check status of all system voltages (Use precistion voltage source on one channel for ADC cal)
	# 2)	Connect to database
	# 3)	Get cal factors etc.
	# 4)	Check status of levels
	# 5)	Start PWM
	# 6)	Check status of beam(measure @ 10% duty cycle and 90% duty cycle then zero via feedback)
	# 7)	Setup interrupts

def comms():
	"""
	Gets serial data and parses command and data
	Returns list with command a data
	n_bytes
	z_command
	z_data
	checksum
	"""
	error = "no error"
	return error


# def main():
# 	x = 1
# 	while True:
# 		if record_data == True:
# 			x = 1
# 			# Measure beam and levels
# 		else 
# 			x = 0
# 			# Measure levels	








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