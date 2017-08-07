import Adafruit_BBIO.GPIO as GPIO
import time

#need alias for GPIO pins

system9VoltEnable = "P8_10"
systemPowerEnable = "P8_22"


# GPIO.setup("P8_10", GPIO.OUT)
# GPIO.setup("GPIO_1_5", GPIO.OUT)
# GPIO.setup("GPIO_2_4", GPIO.OUT)

GPIO.setup(systemPowerEnable, GPIO.OUT)
GPIO.setup(system9VoltEnable, GPIO.OUT)



def test1():
    # enable gpio for DC-DC converters
    
    GPIO.output(systemPowerEnable, GPIO.LOW)
    GPIO.output(system9VoltEnable, GPIO.LOW)
    # while(True):
            
    print("ZLS Beaglebone Black boot complete")
    time.sleep(1)
    print("Enabling GPIO 1-5 for +/- 5V and +12V")
    GPIO.output(systemPowerEnable, GPIO.HIGH)
    time.sleep(1)
    print("DC-DC converters enabled")
    time.sleep(3)
    print("Enabling GPIO 2-4 for +9V")
    GPIO.output(system9VoltEnable, GPIO.LOW)
    time.sleep(1)
    print("9V LDO converter enabled")
    
    # time.sleep(2)
    # GPIO.output(systemPowerEnable, GPIO.LOW)
    # except KeyboardInterrupt:
    #GPIO.cleanup()
    # we only neet the exception if there is a loop setup and we need to exit out using <ctl> C
    # GPIO.cleanup() needs to be added to program shutdown routine
    
    
def test2():
    print("Test 2 starting.")
    
    
    
    
    
    

testNumber = input("Enter test number to be run:\n1)    Simple turn on with time delay\n2)    Turn on with ADC verification\n>")
if(testNumber == 1):
    test1()
elif(testNumber == 2):
    test2()
else:
    print("Invalid number entered.  \nTerminating....")



    