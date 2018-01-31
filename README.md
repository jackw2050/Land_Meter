# Land_Meter
Python code for Beaglebone Black embedded Linux computer.

Linux kernal:
Image:  bone-debian-8.9-iot-armhf-2017-09-01-4gb.img.xz
Python: 2.?
pyserial: 3.?
Other drivers etc...




Batch file:
Configure all pins including GPIO



config-pin P9.11 uart
config-pin P9.13 uart
config-pin P8.22 in
        gpio : 
            Set pinmux to gpio, existing direction and value unchanged
        in | input:
            Set pinmux to gpio and set gpio direction to input
        out | output :
            Set pinmux to gpio and set gpio direction to output
        hi | high | 1 :
            Set pinmux to gpio and set gpio direction to output driving high
        lo | low | 0 :
            Set pinmux to gpio and set gpio direction to output driving low

    To enable pull-up or pull-down resistors, a suffex may be appended to
    any of the above gpio modes.  Use + or _pu to enable the pull-up resistor
    and - or _pd to enable the pull-down resistor.  Examples:

        in+ | in_pu:
            Enable pull-up resistor and setup pin as per input, above.
        hi- | hi_pd:
            Enable pull-down resistor and setup pin as per high, above.
            While the pull-down resistor will be enabled, it will not do much
            until application software changes the pin direction to input.

Alternate is to write directly to file
GPIO
/sys/class/gpio/gpio22
  active_low  
  device  
  direction  
    in
    out
  edge  
  power  
  subsystem  
  uevent  
  value


Loading connman:
  sudo apt-get update
  sudo apt-get install connman
  
 Overlays: 
  https://github.com/beagleboard/bb.org-overlays
  
  PDA performs PID function
  
  Keep commands for motor control.
  Add new commands for smart motor control with absolute encoder
  
  Add commands for level motor control
  
  Add code for air presssure and temp.
  
  Add commands to request date/ time from PDA


http://www.kilobaser.com/blog/2014-07-28-beaglebone-black-devicetreeoverlay-generator

http://klaus.ede.hih.au.dk/index.php/BBB_Enabling_PWM

