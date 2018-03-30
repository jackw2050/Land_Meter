#   For testing LM-001-HTR board for land meter
#   Actual heater/ thermistor pair will be plugged in to arrestment heater locations
#   All other thermistor connectors will have plugs with a known resistor.  Vlaue will be selected to match 85 deg C
#   All other heater connections will have plugs with LEDs
#   The levels connector will not be tested

#   Set this up as a class to allow use of global variables


import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.SPI import SPI
import MAX11100 as MAX11100


spi = SPI(0,0)
arrestment_heater = "P8_3"
conning_tower_heater = "P8_4"
meter_heater = "P8_5"
gearbox_heater = "P8_6"





arrestment_thermistor = 0x01
conning_tower_thermistor = 0x02
meter_thermistor_1 = 0x03
meter_thermistor_2 = 0x04
gearbox_thermistor = 0x05

thermistor_mux_a0 = "P8_31"
thermistor_mux_a1 = "P8_32"
thermistor_mux_a2 = "P8_33"

node = "Gearbox Heater"
option = "Off"



GPIO.setup( arrestment_heater, GPIO.OUT)
GPIO.setup( conning_tower_heater, GPIO.OUT)
GPIO.setup( meter_heater, GPIO.OUT)
GPIO.setup( gearbox_heater, GPIO.OUT)

GPIO.setup( thermistor_mux_a0, GPIO.OUT)
GPIO.setup( thermistor_mux_a1, GPIO.OUT)
GPIO.setup( thermistor_mux_a2, GPIO.OUT)




def led_test(option, node):
    print"Please verify ", node, " LED is ", option, " and all others are off"
    user_test = "n"

    user_test = raw_input(" (y/n)")
    
    if user_test == 'Y':
        print  node, " ", option, ": PASS" 
    elif   user_test == 'y':
        print node, " ", option, ": PASS"
    else:
        print node, " ", option, ": FAIL"

    return 0


def set_heater_on(heater):
    #   Return oll heaters to off
    GPIO.output(arrestment_heater, GPIO.LOW)
    GPIO.output(conning_tower_heater, GPIO.LOW)
    GPIO.output(meter_heater, GPIO.LOW)
    GPIO.output(gearbox_heater, GPIO.LOW)

    if heater == "off":
        return None
    #   Turn on heater for test
    else:
        GPIO.output(heater, GPIO.HIGH)


#   Set all heaters to off
GPIO.output( arrestment_heater, GPIO.LOW)
GPIO.output( conning_tower_heater, GPIO.LOW)
GPIO.output( meter_heater, GPIO.LOW)
GPIO.output( gearbox_heater, GPIO.LOW)

#   Test all heater LEDs for off


led_test("Off", "arrestment_heater")
led_test("Off", "conning_tower_heater")
led_test("Off", "meter_heater")
led_test("Off", "gearbox_heater")

#   Turn on and test heaters one at a time

set_heater_on(arrestment_heater)
led_test("On", "Arrestment heater")

set_heater_on(conning_tower_heater)
led_test("On", "Conning tower heater")

set_heater_on(meter_heater)
led_test("On", "Meter heater")

set_heater_on(gearbox_heater)
led_test("On", "Gearbox heater")

set_heater_on("off")




#   Heater test
#   Use MAX11100 ADC to test the thermistors

def set_thermistor_address(thermistor):
    if thermistor == "arrestment":
        GPIO.output(thermistor_mux_a0, GPIO.LOW)
        GPIO.output(thermistor_mux_a1, GPIO.LOW)
        GPIO.output(thermistor_mux_a2, GPIO.LOW)
    elif thermistor == "gearbox":
        GPIO.output(thermistor_mux_a0, GPIO.HIGH)
        GPIO.output(thermistor_mux_a1, GPIO.LOW)
        GPIO.output(thermistor_mux_a2, GPIO.LOW)
    elif thermistor == "conning_tower":
        GPIO.output(thermistor_mux_a0, GPIO.LOW)
        GPIO.output(thermistor_mux_a1, GPIO.HIGH)
        GPIO.output(thermistor_mux_a2, GPIO.LOW)
    elif thermistor == "meter1":
        GPIO.output(thermistor_mux_a0, GPIO.HIGH)
        GPIO.output(thermistor_mux_a1, GPIO.HIGH)
        GPIO.output(thermistor_mux_a2, GPIO.LOW)
    elif thermistor == "meter2":
        GPIO.output(thermistor_mux_a0, GPIO.LOW)
        GPIO.output(thermistor_mux_a1, GPIO.LOW)
        GPIO.output(thermistor_mux_a2, GPIO.HIGH)
    else:
        return 0



#   Set address
#   Measure ADC voltage
#   Convert to resistance
#   Convert resistance to temperature
#   Test temp



system_voltage = 5.0  # Make manual measurment and change as necessary
system_resistor = 6980
set_thermistor_address(thermistor)
thermistor_voltge = MAX11100.ReadADC_average(100, 100)
#




print( "Unplug heater and thermistor test plugs")
i = raw_input ("Press enter/return when complete")
print("Plug heater and thermistor monitor plugs into Arrestment heater and thermistor")
i = raw_input ("Press enter/return when complete")


#   This is for development only.
#   Measure actual thermistor and turn on heater as needed.
#   Print state and temperature every minute












GPIO.cleanup()

