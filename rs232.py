import serial



class Serial_Comms:
    'Common base class for for all system control'
    debug = True
    empCount = 0
    # import Adafruit_BBIO.UART as UART


# UART.setup("UART1")


# for this sample I need to manually load the UART
# echo BB-UART2 > /sys/devices/bone_capemgr.*/slots
# the cape managet may not be in the same location
# need to learn to use PyBBIO so that  device tree is automatically loaded



port = serial.Serial(port = "/dev/ttyO1", baudrate = 9600)
# ser.close()
# ser.open()
# if ser.isOpen():
#   print "Serial is open!"
#     ser.write("Hello World!")
# ser.close()

def serialInit():
  print( "test")
  

def getSerialData():
  # get the data from the buffer
  # parse the data
  # verify the checksumm
  cmdLength = port.read(1)
  cmdData = port.read(cmdLength)
  #Need to check if this returns a list of bytes 
  # https://github.com/pyserial/pyserial/blob/master/examples/wxTerminal.py
  print ("test")

  # while True:
  #   if (port.inWaiting()):
  #     data = ""
  #     while (port.inWaiting()):
  #       data += port.read()
  #       time.sleep(0.005)
  #   # print what was sent
  #   print( "Data received:\n '%s'" % data)
  #   port.write(data)
  #   time.sleep(0.1)


def verify_checksum(comm_data):
    verified = False
    return verified

def calculate_checksum(comm_data):
    checksum = 0x000
    return checksum

def Get_PWM_Duty_Cycle():
  return dutyCycle


# --Meter Commands--

#   PWM Register - Read, Write
#   Gravity Data - Read, Turn On Auto Send, Turn Off Auto Send
#   Sync Counter - Reset
#   System Status - Read
#   Receiver - Send Handshake
def Alternate_Break():
  return 0
"""
Purpose:  Performs same initial hand shake function as a break signal. For use with Bluetooth connection.

Command ID: F9
Parameters: None


--Byte----Function----------------------
  0x02    Number of bytes to follow
  0xF9    Command ID
  0xXX    Chechsum
  01F9XX
  
  
  00000001 ‭11111001‬



Returns:
--Byte----Function----------------------
  0x02    Number of bytes to follow
  0x07    Response ID 0x07
  0xXX    Chechsum
  0207XX
  
"""

"""Purpose: Tells the meter to transmit the current PWM duty cycle value.
The 16 bit value represents the duty cycle stored in the meter,
with 0x0000 = 0% DC and 0xFA00 (64000 decimal) = 100% DC.
This is the full range of the force feedback system.


Command ID: FE
Parameters: None

--Byte----Function----------------------
  0x02    Number of bytes to follow
  0xFE    Command ID
  0xXX    Checksum

Returns:

--Byte----Function----------------------
  0x04    Number of bytes to follow
  0xFE    Respose ID
  0xXX    MSB
  0xXX    LSB
  0xXX    Checksum
"""

# [4, 2, 243, 49, 196] = 5%       F331
# [4, 2, 230, 100, 132] = 10%     E664
# [4, 2, 127, 255, 134]  = 50%    7FFF
# [4, 2, 25, 153, 134] = 90%      1999
# [4, 2, 5, 30, 29] = 98%         051E

def SET_PWM_Duty_Cycle(pwmDataArray):
  # 100% = 65635
    newDutyCycleFloat = 0.0
    newDutyCycleInt = bytes_to_int(pwmDataArray)
    newDutyCycleFloat = 100.0 * (newDutyCycleInt / 0xFFFF)
    print
    newDutyCycleFloat
    return newDutyCycleFloat


# --Meter Inputs--

#   PWM Duty Cycle
#   Turn On 1 Sec Gravity Data Xmit
#   Turn Off 1 Sec Gravity Data Xmit
#   Reset Clock

def parse_commands(command_bytes):
    command_byte = command_bytes[0]

    if command_byte == 0x00:
        Send_System_Status()
    elif command_byte == 0xFE:
        Get_PWM_Duty_Cycle()
    elif command_byte == 0x02:
        SET_PWM_Duty_Cycle(command_bytes)
    elif command_byte == 0x03:
        Send_Data_Sets_at_1_Sec_Intervals(command_bytes)

    elif command_byte == 0xFF:
        Stop_Sending_Data_Sets()

    elif command_byte == 0x00:
        Send_System_Status()

    elif command_byte == 0xF9:
        Alternate_Break()







# --Meter Outputs--

#   PWM Duty Cycle                  Char             Integer
#   Beam Frequency                  Char
#   Long Level Frequency            Char
#   Cross Level Frequency           Char
#   Lid Temperature                 Char             Integer
#   System Status[2]                Char                   

#       Receiver/Queue/Command Error
#       Transmitter/Queqe Error
#       Time Not Set
#       Command Failure
#       Receive Buffer Has Command
#       Transmit Buffer Has command 

    
                                    
#   Meter Outputs

#       PWM Duty Cycle          (16bit)
#       Beam Frequency          (16bit)
#       Cross Level Frequency   (16bit)
#       Long Level Frequency    (16bit)
#       Temperature             (16bit)
#       Checksum                (8bit)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Message Format

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# Byte    Function

# 0       Number of bytes to follow -11
# 1       Command ID
# 2       Data
# .
# .
# .
# N       Last data byte
# N+1     Check sum (EOR of bytes 2 - N)





def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result


def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return result
   
   
    
def calculateChecksum(cmdArray):
    checksum = 0
    print "Received array ", cmdArray
    # checksum = hex(sum(bytearray(cmdArray)))
    for index in cmdArray:
        checksum = checksum ^ index
    return checksum

def parseRXcommand(rxByteArray):
  rxLength = len(rxByteArray)
  rxCommand = rxByteArray[1]
  checksum = rxByteArray[rxLength - 1]
  print "Initial array", rxByteArray
  print "Checksum", checksum
  print "Command", rxCommand
  rxByteArray.pop(0) # Strip off byte count
  rxByteArray.pop(0) # Strip off command
  rxByteArray.pop() # Strip off checksum
  print "Array after clean", rxByteArray
  print "calculated checksum ", calculateChecksum(rxByteArray)
  # print map(hex, rxCommand[0])
  if checksum == calculateChecksum(rxByteArray):
    print "Checksum matches"
  else:
    print "Data error"

  print "Integer value ", bytes_to_int(rxByteArray)
  return rxCommand, bytes_to_int(rxByteArray)
  
  
  














  
  
SET_PWM_Duty_Cycle(parseRXcommand(parseRXcommand([0x04, 0x1b, 0xff, 0xff, 0x00]))  
 

"""
Purpose: Sends a 16 bit PWM duty cycle value to the meter, which replaces the current value with the new value immediately.

Command ID: 02
Parameters: MSB, LSB


--Byte----Function----------------------
  0x04    Number of bytes to follow
  0x02    Command ID
  0xXX    MSB
  0xXX    LSB
  0xXX    Checksum

        
Returns: None
"""




# def Send_Data_Sets_at_1_Sec_Intervals():
#   """

# Command ID: 01

# Purpose: Tells the meter to send data sets at one second intervals. See 'Send Current Data Set' for message format.
# Parameters: None


# --Byte----Function----------------------
#   0x02    Number of bytes to follow
#   0x01    Command ID
#   0xXX    Chechsum    
# Returns: None
# """




# def Stop_Sending_Data_Sets():
#   return 0
"""
Purpose: Tells the meter to stop sending data sets at one second intervals.

Command ID: FF

Parameters: None


--Byte----Function----------------------

  0x02    Number of bytes to follow
  0xFF    Command ID
  0xXX    Chechsum


Returns: None


"""



def Send_Current_Data_Set():
  return 0

"""Purpose: This command tells the meter to send the current data set. The beam and level values are from a counter that is clocked by the respective signal. The counter counts to 0xFFFF, then rolls over (which of course must be accounted for). The difference between two consecutive values divied by the time interval is the signal frequency. The temperature value is an analog value converted to binary, which can vary from 0 to 255. It is not calibrated, however it is set to about 128 when the meter is at its operating temperature. 

Command ID: 03

Parameters: None

--Byte----Function----------------------

  0x02    Number of bytes to follow
  0x03    Command ID
  0xXX    Chechsum

Returns: Beam Freq, Long Level Freq, Cross Level Freq, Thermometer value

--Byte----Function----------------------

  0x09    Number of bytes to follow
  0x03    Response ID
  0xXX    Beam MSB
  0xXX    Beam LSB
  0xXX    Long Level MSB
  0xXX    Long Level LSB
  0xXX    Cross Level MSB
  0xXX    Cross Level LSB
  0xXX    Temperature
  0xXX    Chechsum
"""




def Send_System_Status():
  return 0

"""Purpose: This command tells the meter to transmit its system status information. 

  Status Byte 0

--Bit----Function----------------------

    0    Command failure
    1    Time not set
    2    Fine stepper motor turning - OBSOLETE
    3    Course stepper motor turning - OBSOLETE
    4    Set high for export meters - OBSOLETE
    5    Not used
    6    Transmitter/transmitter queue error
    7    Receiver/receiver queue error

  Status Byte 1

--Bit----Function----------------------

    0    Not used
    1    Not used
    2    Not used
    3    Not used
    4    Not used
    5    Not used
    6    Receive buffer has command
    7    Transmit buffer has command

  Status Byte 2 - Not used
  Status Byte 3 - Not used

Command ID: 00
Parameters: None


--Byte----Function----------------------

  0x02    Number of bytes to follow
  0x00    Command ID 
  0xXX    Chechsum



Returns: system0, system1, system2, system3

--Byte----Function----------------------

  0x06    Number of bytes to follow
  0x00    Response ID
  0xXX    Status Byte 0
  0xXX    Status Byte 1
  0xXX    Status Byte 2
  0xXX    Status Byte 3
  0xXX    Chechsum

"""



