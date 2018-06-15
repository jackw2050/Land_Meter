import Adafruit_BBIO.UART as UART
import serial
import binascii

# Do not need Adafruit.  only pyserial
 
bt_serial = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
disp_serial = serial.Serial(port = "/dev/ttyO1", baudrate=9600)



# handshake  02F9FB  number of bytes, command, checksumm
nbytes1 = []
print(bt_serial.name) 
bt_serial.close()
bt_serial.open()
if bt_serial.isOpen():
    print "Serial is open!"
    t = 0
    while t == 0:
        # t = 1
        # bt_serial.write("Hello World!")
        cmdData = bt_serial.read(1)
        nbytes = hex(ord(cmdData))
        nbytes1.append(ord(cmdData))
        # print "Bytes: ", nbytes
        # print "Bytes: ", nbytes1

        if nbytes1[0] > 0:
            print "2 Bytes"
            for xx in range(nbytes1[0] ):
                cmdData = bt_serial.read(1)
                nbytes1.append(ord(cmdData))
            print nbytes1
            # nbytes = hex(ord(cmdData))
        # print "Bytes: ", nbytes
        
        # cmdData = bt_serial.read(1)
        # nbytes = hex(ord(cmdData))
        # print "Bytes: ", nbytes
        # if nbytes == 2:
        #     cmdData1 = bt_serial.read(1)
        #     print "Commnad #: ", cmdData1
        #     cmdData2 = bt_serial.read(1)
        #     print "Checksum: ", cmdData2
        
      
        nbytes1 = []
        # print "Hello World!"
        x = 0x020705
        to_send = [0x02,0x07,0x05]
        # to_send = b'\x02'
        # print "Sending : ", to_send
        bt_serial.write(to_send)
    
bt_serial.close()


#UART.setup("UART1")

# ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
# ser.close()
# ser.open()
# if ser.isOpen():
#     print "Serial is open!"
#     ser.write("Hello World!")
# ser.close()




def setup_bbb_uart(self):
    # Is this necessary if I don't want to use it myself??
    UART.setup(self.uart)
    self.ser = serial.Serial(port=self.tty, baudrate=9600)
    self.ser.close()
    self.ser.open()
    if self.ser.isOpen():
        return True
    else:
        return False





# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()

#https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/uart



# https://github.com/adafruit/adafruit-beaglebone-io-python/issues/16  interrupts

#  Use PRU






# http://pyserial.readthedocs.io/en/latest/shortintro.html


# import serial
# import time
# import datetime
# import re

# serial = serial.Serial("/dev/ttyO1", baudrate=38400)




# resp = ""

# while True:
#         while (serial.inWaiting() > 0):
#                 data = serial.read()
#                 resp += data
#                 if "\r\n" in resp:
#                         now = datetime.datetime.now()
#                         timestamp = "%02d/%02d/%d %02d:%02d:%02d" % \
#                         (now.month,now.day,now.year,now.hour,now.minute,now.second)
#                         matchObj = re.match(r'\^([0-9A-F]+)\r\n', resp)
#                         print matchObj.group(1)
#                         resp = ""
#                         serial.flush();
#                         serial.write(matchObj.group(1) + " OK: " + timestamp + "\n")





