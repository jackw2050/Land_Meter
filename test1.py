
# import zlsGpio as ZLS_GPIO
# import heater
import time
from datetime import datetime
import math

# Arrestment = heater('Arrestment', 54, 55, False,"P8_5", 0.0, 0.0)
temp = 53540
tempList = [[94980, 0],[90410, 1],[86090, 2],[81990, 3],[78110, 4],[74440, 5],[70960, 6],[67660, 7],[64530, 8],[61560, 9],[58750, 10],[56070, 11],[53540, 12],[51130, 13],[48840, 14],[46670, 15],[44600, 16],[42640, 17],[40770, 18],[38990, 19],[37300, 20],[35700, 21],[34170, 22],[32710, 23],[31320, 24],[30000, 25],[28740, 26],[27540, 27],[26400, 28],[25310, 29],[24270, 30],[23280, 31],[22330, 32],[21430, 33],[20570, 34],[19740, 35],[18960, 36],[18210, 37],[17490, 38],[16800, 39],[16150, 40],[15520, 41],[14920, 42],[14350, 43],[13800, 44],[13280, 45],[12770, 46],[12290, 47],[11830, 48],[11390, 49],[10970, 50],[10570, 51],[10180, 52],[9807, 53],[9450, 54],[9109, 55],[8781, 56],[8467, 57],[8166, 58],[7876, 59],[7599, 60],[7332, 61],[7076, 62],[6830, 63],[6594, 64],[6367, 65],[6149, 66],[5940, 67],[5738, 68],[5545, 69],[5359, 70],[5180, 71],[5007, 72],[4842, 73],[4682, 74],[4529, 75],[4381, 76],[4239, 77],[4102, 78],[3970, 79],[3843, 80],[3720, 81],[3602, 82],[3489, 83],[3379, 84],[3273, 85],[3172, 86],[3073, 87],[2979, 88],[2887, 89],[2799, 90],[2714, 91],[2632, 92],[2552, 93],[2476, 94],[2402, 95],[2331, 96],[2262, 97],[2195, 98],[2131, 99],[2069, 100],[2009, 101],[1950, 102],[1894, 103],[1840, 104],[1788, 105],[1737, 106],[1688, 107],[1640, 108],[1594, 109],[1550, 110],[1507, 111],[1465, 112],[1425, 113],[1386, 114],[1348, 115],[1311, 116],[1276, 117],[1241, 118],[1208, 119],[1176, 120],[1145, 121],[1114, 122],[1085, 123],[1057, 124],[1029, 125],[1002, 126],[976.3, 127],[951.1, 128],[926.7, 129],[903, 130],[880, 131],[857.7, 132],[836.1, 133],[815, 134],[794.6, 135],[774.8, 136],[755.6, 137],[736.9, 138],[718.8, 139],[701.2, 140],[684.1, 141],[667.5, 142],[651.3, 143],[635.6, 144],[620.3, 145],[605.5, 146],[591.1, 147],[577.1, 148],[563.5, 149],[550.2, 150]]
# print len(tempList)
# a = datetime.now()
# for values in range(149):
#     lowVal =  tempList[values]
#     highVal = tempList[values + 1]
#     if temp <= lowVal[0] and temp >= highVal[0]:
#         print lowVal[1]
#         print highVal[1]
#     x = values

# b = datetime.now()    
# c = b - a

x1 = 98.70958430147724 - (0.006591497743219753 * temp) + (2.4399630812566e-7 * temp **2) - (4.40537263e-12 * temp **3) + (2.946e-17 * temp **4)
print int(x1)
print math.ceil(x1)

# print a
# print b
# print c.microseconds
    
# new1 =  tempList[0]
# print new1[0]

# ZLS_GPIO.zlsInit()

# import file_ops
# import Levels

# #file_ops.create_log_entry("test")
# #file_ops.create_basic_cal_file()
# #file_ops.read_cal_file()

# print Levels.get_level_in_arc_sec(65000)


# from Adafruit_I2C import Adafruit_I2C
 
# i2c = Adafruit_I2C(0x77)

# P9_19: I2C2, SCL
# P9_20: I2C2, SDA

# write8(self, 0x01, 0xFA)


# systemPower(0, debug)
	   	

# setThermistorMux(0,0,0,debug)
# # # setFBMux(1,1,debug)
# setHeater(1, 1, 0, 0, debug)
# setMux(1,0,0,debug)





# Code for GPIO input detection
GPIO.setup("P9_15", GPIO.IN)

GPIO.add_event_detect("P9_15", GPIO.FALLING)
#your amazing code here
#detect wherever:
while True:
    
    if GPIO.event_detected("P9_15"):
        print "event detected!"
	
	
	
	
	
# Serial port code
import Adafruit_BBIO.GPIO as GPIO
import time
# import Adafruit_BBIO.UART as UART
import serial 
# UART.setup("UART4")
 
# ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
# print(ser.name) 
# ser.close()
# ser.open()
# if ser.isOpen():
#     print "Serial is open!"
#     while True:
#         ser.write("Hello World!")
    
# ser.close()
