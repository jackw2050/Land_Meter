import Adafruit_BBIO as GPIO
import time

# enable gpio for DC-DC converters

print("ZLS Beaglebone Black boot complete")
time.sleep(1)
print("Enabling GPIO 1-5 for +/- 5V and +12V")
time.sleep(1)
print("DC-DC converters enabled")
time.sleep(1)
print("Enabling GPIO 2-4 for +9V")
time.sleep(1)
print("9V LDO converter enabled")