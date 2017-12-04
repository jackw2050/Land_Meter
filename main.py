 content of test_sample.py
import csv, sys
from datetime import datetime
import file_ops

class Land_Sys:
    'Common base class for for all system control'
    debug = True
    empCount = 0
    system9VoltEnable = "P8_10"
    systemPowerEnable = "P8_22"

    dutyCycle = 0.50

    Meter = "Land"
    Hardware_revision = 1.0
    Software_revision = 1.5
    Calibration_version = "calibrated"
    Customer = "Orangelamp"

    pwm_freq = 125
    sense_freq = 10000
    adc_offset = 0.0
    zh_offset = 0.0
    lid_thermistor_offset = 0.0
    p12v_offset = 0.0
    p5v_offset = 0.0
    p3p3v_offset = 0.0
    battery_thermistor_offset = 0.0
    batt_v_offset = 0.0

    beam_offset = 0.0
    m5v_offset = 0.0
    zp_offset = 0.0
    gearbox_thermistor_offset = 0.0
    conning_tower_thermistor_offset = 0.0
    arrestment_thermistor_offset = 0.0
    meter_thermistor_1_offset = 0.0
    meter_thermistor_2_offset = 0.0

    adc_divider = 0.0
    zh_divider = 0.0
    lid_thermistor_divider = 0.0
    p12v_divider = 0.0
    p5v_divider = 0.0
    p3p3v_divider = 0.0
    battery_thermistor_divider = 0.0
    batt_v_divider = 0.0

    beam_divider = 0.0
    m5v_divider = 0.0
    zp_divider = 0.0
    gearbox_thermistor_divider = 0.0
    conning_tower_thermistor_divider = 0.0
    arrestment_thermistor_divider = 0.0
    meter_thermistor_1_divider = 0.0
    meter_thermistor_2_divider = 0.0
    beam10 = 0.0
    beam50 = 2.5
    beam90 = 5.0
    p5vTarget = 5.0
    p5vError = 0.2
    n5vTarget = 5.0
    n5vError = 0.2
    p3p3vTarget = 3.3
    p3p3vError = 0.2
    p12vTarget = 12.0
    p12vError = 0.5
    batteryTarget = 12.0
    batteryError = 2.0
    zh_Target = 36.0
    zh_Error = 0.1
    zpTarget = 24.0
    zpError = 0.01

    def __init__(self): # can I run other methods to init?
        #CHECK FOR CAL FINE EXISTANCE.
        #IF NONE CREATE IT
        from pathlib import Path
        print("Checking to see if basic cal file exists")
        my_file = Path("zls_cal.csv")
        if my_file.is_file():
            print(my_file, "exists\n")
            print(Land_Sys.debug )
            if Land_Sys.debug == True:
                print("executing true line")
                file_ops.read_cal_data("zls_cal.csv")    #Need to check on this error
        else:
            file_ops.create_basic_cal_file()    # this should only happen on a new meter
            my_log_file = Path("create_basic_log_file(log.csv)")
            if my_log_file.is_file():
                print("File exixts")
            else:
                file_ops.create_basic_log_file()









emp1 = Land_Sys()
Land_Sys.create_log_entry("This sucks")




# emp2 = Land_Sys("Manni", 5000)
#
# emp1.displayEmployee()
# emp2.displayEmployee()
# print ("Total Employee %d" % Land_Sys.empCount)
# Land_Sys.empCount = 5
# print ("Total Employee %d" % Land_Sys.empCount)
