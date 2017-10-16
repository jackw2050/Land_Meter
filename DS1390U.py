
from Adafruit_BBIO.SPI import SPI

import time
#https://github.com/adafruit/adafruit-beaglebone-io-python
# Constants
VREF = 4.36


spi = SPI(0,0) 

#spi.fd = -1;
spi.mode = 3;
spi.bpw = 8;#Bits per word
spi.msh=1000000


