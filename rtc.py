
#!/usr/bin/python
# Write one byte to a device and an address:
# i2cset -y 2 0x77 0xf4 0x34
from bbio import *
# Read one byte from a device and an address:
# i2cdump -y 2 0x77

import smbus
import time
# from Adafruit_I2C import Adafruit_I2C

DS3231M_address = 0x68
bus = smbus.SMBus(2)
# i2c = Adafruit_I2C(address)

BEAT = GPIO3_21
# Interrupts
def timer_handler():
	print "Tick"
	
def setup():
	attachInterrupt (timer_handler)

def loop():
	while True:
		bus.write_byte_data(DS3231M_address, 0x0E, 0x00)	
		
		
run(setup, loop)		
	
	
	
	















SECONDS_ADDRESS = 0x00
MINUTES_ADDRESS = 0x01
HOUR_ADDRESS = 0x02
DAY_ADDRESS = 0x03
DATE_ADDRESS = 0x04
MONTH_ADDRESS = 0x05
YEAR_ADDRESS = 0x06
CONTROL_ADDRESS = 0x0E
STATUS_ADDRESS = 0x0F
AGING_OFFSET = 0x10
TEMPERATURE_MSB = 0x11
TEMPERATURE_LSB = 0x12

SET_1HZ = 0x00



# class DS3231M():		
# 	def __init__(self):
# 		self.MON = 1
# 		self.TUE = 2
# 		self.WED = 3
# 		self.THU = 4
# 		self.FRI = 5
# 		self.SAT = 6
# 		self.SUN = 7
# 		self.DS3231M_I2C_ADDRESS = 0x68
		
# 		print 'begin' 
		
# 	def decToBcd(self, val):
# 		return ( (val/10*16) + (val%10) )
		
# 	def bcdToDec(self,  val):
# 		return ( (val/16*10) + (val%16) )
		
# 	def begin(self, news):
# 		print news
		
# 	def startClock(self):	
# 		bus.write_byte(self.DS3231M_I2C_ADDRESS, 0x00)
# 		self.second = bus.read_byte(self.DS3231M_I2C_ADDRESS) & 0x7f
# 		bus.write_byte_data(self.DS3231M_I2C_ADDRESS, 0x00, self.second)
		
# 		print 'startClock..'
		
# 	def stopClock(self):						
# 		bus.write_byte(self.DS3231M_I2C_ADDRESS, 0x00)
# 		self.second = bus.read_byte(self.DS3231M_I2C_ADDRESS) | 0x80
# 		bus.write_byte_data(self.DS3231M_I2C_ADDRESS, 0x00, self.second)			
		
# 		print 'stopClock..'
		
# 	def setTime(self):
# 		data = [self.decToBcd(self.second), self.decToBcd(self.minute), \
# 				self.decToBcd(self.hour), self.decToBcd(self.dayOfWeek), \
# 				self.decToBcd(self.dayOfMonth), self.decToBcd(self.month), \
# 				self.decToBcd(self.year)]
		
# 		bus.write_byte(self.DS3231M_I2C_ADDRESS, 0x00)
# 		bus.write_i2c_block_data(self.DS3231M_I2C_ADDRESS,0x00,data)
		
# 		print 'setTime..'
		
# 	def getTime(self):
# 		bus.write_byte(self.DS3231M_I2C_ADDRESS, 0x00)
# 		data = bus.read_i2c_block_data(self.DS3231M_I2C_ADDRESS,0x00)
# 		#A few of these need masks because certain bits are control bits
# 		self.second = self.bcdToDec(data[0] & 0x7f)
# 		self.minute = self.bcdToDec(data[1])
# 		self.hour = self.bcdToDec(data[2] & 0x3f)  #Need to change this if 12 hour am/pm
# 		self.dayOfWeek = self.bcdToDec(data[3])
# 		self.dayOfMonth = self.bcdToDec(data[4])
# 		self.month = self.bcdToDec(data[5])
# 		self.year = self.bcdToDec(data[6])
		
# 		print 'getTime..'
		
# 	def fillByHMS(self, _hour,  _minute,  _second):
# 		self.hour = _hour
# 		self.minute = _minute
# 		self.second = _second
		
# 		print 'fillByHMS..'
		
# 	def fillByYMD(self, _year,  _month,  _day):		
# 		self.year = _year - 2000
# 		self.month = _month;
# 		self.dayOfMonth = _day
		
# 		print 'fillByYMD..'
		
# 	def fillDayOfWeek(self,  _dow):		
# 		self.dayOfWeek = _dow
		
# 		print 'fillDayOfWeek..'
		
# if __name__ == "__main__": 


# i2c.write8(0x68, CONTROL_ADDRESS, SET_1HZ)
	
# print i2c.readU8(0x68, CONTROL_ADDRESS)



	# clock = DS3231M()
	# clock.fillByYMD(2015,3,5)
	# clock.fillByHMS(12,42,30)
	# clock.fillDayOfWeek(clock.THU)	
	# clock.setTime()
	# while True:		
	# 	clock.getTime()
	# 	print clock.hour, ":", clock.minute, ":", \
	# 			clock.second, " ", clock.dayOfMonth, "/", \
	# 			clock.month, "/", clock.year,"  ", "weekday", \
	# 			":", clock.dayOfWeek    		
	# 	time.sleep(1)
		
		

	



	
