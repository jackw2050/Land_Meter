#import the library
from Adafruit_BBIO.SPI import SPI
import time
#import Adafruit_BBIO.SPI as SPI
SPI_PORT = 0
SPI_DEVICE = 0
AVG_COUNT = 250


define conning_tower()
    # set MAX1300 input and setup
    # take AVG_COUNT measurements and average thermistor
    # convert to temperature
    # set gpio based on value
    # maybe add some hystersis to reduce # of switches
    
define arrestment()

define gearbox()

define meter()
    # measure both thermistors
    # need to decide to average or weighted average etc

define IC()
    # This is for temperture control of the onboard ICs

