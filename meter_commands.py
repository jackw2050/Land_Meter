import pwm 
import time


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
    # print "Received array ", cmdArray
    # checksum = hex(sum(bytearray(cmdArray)))
    for index in cmdArray:
        checksum = checksum ^ index
    return checksum

def parseRXcommand(rxByteArray):
  rxLength = len(rxByteArray)
  rxCommand = rxByteArray[1]
  checksum = rxByteArray[rxLength - 1]
#   print "Initial array", rxByteArray
#   print "Checksum", checksum
#   print "Command", rxCommand
  rxByteArray.pop(0) # Strip off byte count
  rxByteArray.pop(0) # Strip off command
  rxByteArray.pop() # Strip off checksum
#   print "Array after clean", rxByteArray
#   print "calculated checksum ", calculateChecksum(rxByteArray)
  # print map(hex, rxCommand[0])
  if checksum == calculateChecksum(rxByteArray):
    print "Checksum matches"
    parse_command(rxCommand, rxByteArray)
  else:
    print "Data error"

#   print "Integer value ", bytes_to_int(rxByteArray)
  return rxCommand, bytes_to_int(rxByteArray)
  
  
def SET_PWM_Duty_Cycle(cmd_data):
    # print cmd_data
    pwm_data = (cmd_data[0] << 8) + cmd_data[1]
    # print hex(pwm_data)[2:]
    new_pwm_percent =  pwm_data / 64000.0 *100
    # print new_pwm_percent 
    time.sleep(4)
    pwm.set_force_duty_cycle(new_pwm_percent)
    pwm.current_duty_cycle = pwm_data
    

     
def Get_PWM_Duty_Cycle():
    pwm1 = 0
    pwm1 = int(75.26589 / 100 * 64000)
    print pwm1
    print hex(pwm1)[2:]
    pwm2 = [0x00, 0x03]
    pwm2[0] = pwm1 >> 8
    pwm2[1] = pwm1 & 0xFF
    print pwm2
    print pwm2[0], pwm2[1]
    print 


def Send_System_Status():
    print "Requesting system status"




def parse_command(meter_cmd, cmd_data):
  if meter_cmd == 0x00:
    Send_System_Status()
  elif meter_cmd == 0x01:
      Send_Data_Sets_at_1_Sec_Intervals()
  elif meter_cmd == 0x02:
      SET_PWM_Duty_Cycle()
  elif meter_cmd == 0xFE:
      Get_PWM_Duty_Cycle()
  elif meter_cmd == 0xFF:
     Stop_Sending_Data_Sets() 
  elif meter_cmd == 0x03:
      Send_Current_Data_Set()
  elif meter_cmd == 0xF9:
        Alternate_Break()








# parseRXcommand([0x03, 0x00, 0x00])

cmd_data = [0xbc, 0x2a]
SET_PWM_Duty_Cycle(cmd_data)
