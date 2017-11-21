


def parse_command(meter_cmd, cmd_data):
  if meter_cmd = 0x00:
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
        Send_Current_Data_Set():
    elif meter_cmd == 0xF9:
        Alternate_Break()
