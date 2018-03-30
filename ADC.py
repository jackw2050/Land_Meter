# ADC code requirements

from Adafruit_BBIO import ADC

class BBB_ADC:


    AIN0 = "P9_39"  #+12V
    AIN1 = "P9_40"  #Lid thermistor
    AIN2 = "P9_37"  #BBB +5V
    AIN3 = "P9_38"  #N/C
    AIN4 = "P9_33"  #+3.3V
    AIN5 = "P9_36"  # Battery thermistor   
    AIN6 = "P9_35"  # +5V
    
    
    adc_average_count = 100
    
    ain0_divider = 0.090939
    ain1_divider = 1.0
    ain2_divider = 0.33402
    ain3_divider = 1.0
    ain4_divider = 0.13069
    ain5_divider = 1.0
    ain6_divider = 0.33307
    
    #These values should reside in file and loaded at boot
    ain0_offset = 0.0
    ain1_offset = 0.0
    ain2_offset = 0.0
    ain3_offset = 0.0
    ain4_offset = 0.0
    ain5_offset = 0.0
    ain6_offset = 0.0
    ain7_offset = 0.0
    
    
    adc_offset = 0.004  #This value should reside in file


    def __init__(self):
        self.ADC.init()





def updateAinDivider(self, ainChan, offset):
    if(ainChan == 0):
        BBB_ADC.ain0_divider = offset
        return 0
    elif(ainChan == 1):
        BBB_ADC.ain1_divider = offset
        return 0
    elif(ainChan == 2):
        BBB_ADC.ain2_divider = offset
        return 0
    elif(ainChan == 3):
        BBB_ADC.ain3_divider = offset
        return 0
    elif(ainChan == 4):
        BBB_ADC.ain4_divider = offset
        return 0
    elif(ainChan == 5):
        BBB_ADC.ain5_divider = offset
        return 0
    elif(ainChan == 6):
        BBB_ADC.ain6_divider = offset
        return 0
    elif(ainChan == 7):
        BBB_ADC.ain7_divider = offset 
        return 0
    else:   
        print "ADC channel not defined.  divider value not updated"
        return 1
        
def updateAinOffset(self, ainChan, offset):
    if(ainChan == 0):
        BBB_ADC.ain0_offset = offset
        return 0
    elif(ainChan == 1):
        BBB_ADC.ain1_offset = offset
        return 0
    elif(ainChan == 2):
        BBB_ADC.ain2_offset = offset
        return 0
    elif(ainChan == 3):
        BBB_ADC.ain3_offset = offset
        return 0
    elif(ainChan == 4):
        BBB_ADC.ain4_offset = offset
        return 0
    elif(ainChan == 5):
        BBB_ADC.ain5_offset = offset
        return 0
    elif(ainChan == 6):
        BBB_ADC.ain6_offset = offset
        return 0
    elif(ainChan == 7):
        BBB_ADC.ain7_offset = offset 
        return 0
    else:   
        print "ADC channel not defined.  Offset not updated"
        return 1

def calcAdcValue(self, raw, divider, offset):
    adjustedADCvalue = raw * divider + offset
    return adjustedADCvalue

def read_adc(self, adc_chan, loop_count, divider, offset):
    if (adc_chan == "zhSys"):
        chan = "P9_39"  #ZH
        # chan = "ain0 etc."
        # divider = BBB_ADC.ain0_divider
        # offset = BBB_ADC.ain0_offset
    elif (adc_chan == "lidThermistorVolt"):
        chan = "P9_40"  #Lid thermistor
        # chan = "ain1 etc."
        # divider = BBB_ADC.ain1_divider
        # offset = BBB_ADC.ain1_offset
    elif (adc_chan == "p12vSys"):
        chan = "P9_37"  #+12V
        # chan = "ain2 etc."
        # divider = BBB_ADC.ain2_divider
        # offset = BBB_ADC.ain2_offset
    elif (adc_chan == "p5vSys"):
        chan = "P9_38"  #+5V
        # chan = "ain3 etc."
        # divider = BBB_ADC.ain3_divider
        # offset = BBB_ADC.ain3_offset
    elif (adc_chan == "p3p3vSys"):
        chan = "P9_33"  #+3.3V
        # chan = "ain4 etc."
        # divider = BBB_ADC.ain4_divider
        # offset = BBB_ADC.ain4_offset
    elif (adc_chan == "battThermistorVolt"):
        chan = "P9_36"  # Battery thermistor   
        # chan = "ain5 etc."
        # divider = BBB_ADC.ain5_divider
        # offset = BBB_ADC.ain5_offset
    elif (adc_chan == "battVolt"):
        chan = "P9_35"  # Battery voltage
        # chan = "ain6 etc."
        # divider = BBB_ADC.ain6_divider
        # offset = BBB_ADC.ain6_offset

    # adcRange = 1.8 / 1024
    adc_value = 0
    for num in range (1, loop_count):
        adc_value += BBB_ADC.ADC.read(chan)
    adc_value /= loop_count
    adc_value *= 1.8
    adc_value = calcAdcValue(adc_value, divider, offset)
    return adc_value







# a = updateAinOffset(4, .003)
# if(a == 0):
#     print a, ADC.ain4_offset

# zh              = 1.8 * read_adc(AIN0, adc_average_count) * ain0_divider + adc_offset
# lid_thermistor  = 1.8 * read_adc(AIN1, adc_average_count) * ain1_divider + adc_offset
# p12v            = 1.8 * read_adc(AIN2, adc_average_count) * ain2_divider + adc_offset
# p5v             = 1.8 * read_adc(AIN3, adc_average_count) * ain3_divider + adc_offset
# p3p3v           = 1.8 * read_adc(AIN4, adc_average_count) * ain4_divider + adc_offset
# batt_thermistor = 1.8 * read_adc(AIN5, adc_average_count) * ain5_divider + adc_offset
# batt_v          = 1.8 * read_adc(AIN6, adc_average_count) * ain6_divider + adc_offset



# print("ZH voltage                   = {:0.4f}V".format(zh))
# print("Lid thermistor voltage       = {:0.4f}V".format(lid_thermistor))
# print("+12V                         = {:0.4f}V".format(p12v))
# print("+5V                          = {:0.4f}V".format(p5v))
# print("+3.3V voltage                = {:0.4f}V".format(p3p3v))
# print("Battery thermistor voltage   = {:0.4f}V".format(batt_thermistor))
# print("Battery voltage              = {:0.4f}V".format(batt_v))
