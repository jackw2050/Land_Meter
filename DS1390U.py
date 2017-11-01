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


secondsAddress 		    	= 0x81
minutesAddress 			    = 0x82
hoursAddress			    = 0x83
dayOfWeekAddress		    = 0x84
dayOfMonthAddress		    = 0x85
monthCenturAddressy	    	= 0x86
yearAddressr				= 0x87

secondsReadAddress 			= 0x01
minutesReadAddress 			= 0x02
hoursReadAddress			= 0x03
dayOfWeekReadAddress	    = 0x04
dayOfMonthReadAddress	    = 0x05
monthCenturReadAddressy	    = 0x06
yearReadAddressr			= 0x07


controlReglAddress			= 0x0D
statusRegAddress			= 0x0E
trickleChargerRegAddress    = 0x0F

agingOffsetAddress		    = 0x10
temperatureMSBAddress	    = 0x11
temperatureLSBAddress	    = 0x12



seconds 		= 0x00
minutes 		= 0x00
hours			= 0x00
dayOfWeek		= 00000XXX
dayOfMonth		= 00NNXXXX
monthCentury	= 0x00
year			= 0x00
control			= 00011000 #Enable 1Hz or 00?
status			= 0x00
agingOffset		= 0x00
temperatureMSB	= 0x00
temperatureLSB	= 0x00

SetHeatBeat     = 0x00#For  control register




