# ADC code requirements

import Adafruit_BBIO.ADC as ADC




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

ADC.setup()




def updateAinDivider(ainChan, offset):
    if(ainChan == 0):
        ain0_divider = offset
        return 0
    elif(ainChan == 1):
        ain1_divider = offset
        return 0
    elif(ainChan == 2):
        ain2_divider = offset
        return 0
    elif(ainChan == 3):
        ain3_divider = offset
        return 0
    elif(ainChan == 4):
        ain4_divider = offset
        return 0
    elif(ainChan == 5):
        ain5_divider = offset
        return 0
    elif(ainChan == 6):
        ain6_divider = offset
        return 0
    elif(ainChan == 7):
        ain7_divider = offset 
        return 0
    else:   
        print "ADC channel not defined.  divider value not updated"
        return 1
        
def updateAinOffset(ainChan, offset):
    if(ainChan == 0):
        ain0_offset = offset
        return 0
    elif(ainChan == 1):
        ain1_offset = offset
        return 0
    elif(ainChan == 2):
        ain2_offset = offset
        return 0
    elif(ainChan == 3):
        ain3_offset = offset
        return 0
    elif(ainChan == 4):
        ain4_offset = offset
        return 0
    elif(ainChan == 5):
        ain5_offset = offset
        return 0
    elif(ainChan == 6):
        ain6_offset = offset
        return 0
    elif(ainChan == 7):
        ain7_offset = offset 
        return 0
    else:   
        print "ADC channel not defined.  Offset not updated"
        return 1

def calcAdcValue(self, raw, divider, offset):
    adjustedADCvalue = raw * divider + offset
    return adjustedADCvalue

def read_adc(adc_chan, loop_count, divider, offset):
    chan = "P9_38"

    if (adc_chan == "lidThermistorVolt"):
        chan = "P9_40"  #Lid thermistor
        # chan = "ain1 etc."
        # divider = ain1_divider
        # offset = ain1_offset
    elif (adc_chan == "p12vSys"):
        chan = "P9_37"  #+12V
        # chan = "ain2 etc."
        # divider = ain2_divider
        # offset = ain2_offset
    elif (adc_chan == "p5vSys"):
        chan = "P9_38"  #+5V
        # chan = "ain3 etc."
        # divider = ain3_divider
        # offset = ain3_offset
    elif (adc_chan == "p3p3vSys"):
        chan = "P9_33"  #+3.3V
        # chan = "ain4 etc."
        # divider = ain4_divider
        # offset = ain4_offset
    elif (adc_chan == "battThermistorVolt"):
        chan = "P9_36"  # Battery thermistor   
        # chan = "ain5 etc."
        # divider = ain5_divider
        # offset = ain5_offset

    adcRange = 1.8
    adc_value = 0.0

    for num in range (0, loop_count):
        adc_value += ADC.read(chan)
        #print adc_value
        #print ADC.read(chan)

    adc_value /= loop_count
    adc_value *= adcRange
    adc_value = calcAdcValue(adc_value, divider, offset)
    return adc_value

def checkLimits(chan, adcValue):
    chan = "P9_38"
    target = 5.0
    lowLimit = 4.9
    hiLimit = 5.1

    if (adc_chan == "lidThermistorVolt"):
        chan = "P9_40"  #Lid thermistor
        target = 5.0
        lowLimit = 4.9
        hiLimit = 5.1
    elif (adc_chan == "p12vSys"):
        chan = "P9_37"  #+12V
        target = 5.0
        lowLimit = 4.9
        hiLimit = 5.1
    elif (adc_chan == "p5vSys"):
        chan = "P9_38"  #+5V
        target = 5.0
        lowLimit = 4.9
        hiLimit = 5.1
    elif (adc_chan == "p3p3vSys"):
        chan = "P9_33"  #+3.3V
        target = 5.0
        lowLimit = 4.9
        hiLimit = 5.1
    elif (adc_chan == "battThermistorVolt"):
        chan = "P9_36"  # Battery thermistor   
        target = 5.0
        lowLimit = 4.9
        hiLimit = 5.1


    if (adcValue < lowLimit or adcValue > hiLimit):
        return -99
    else:
        return 1
                    


# print round(read_adc("p12vSys", 10, 11.01, 0), 3)
print round(read_adc("p5vSys", 10, 6.05, 0), 3)
print round(read_adc("p3p3vSys", 10, 2.9568, 0), 3)


# print ADC.read("P9_37") * 1.8
# a = updateAinOffset(4, .003)
# if(a == 0):
#     print a, ADC.ain4_offset

#zh              = 1.8 * read_adc(AIN0, adc_average_count, 1 , 0)

# lid_thermistor  = 1.8 * read_adc(AIN1, adc_average_count , ain1_divider , adc_offset)
# p12v            = 1.8 * read_adc(AIN2, adc_average_count , ain2_divider , adc_offset)
# p5v             = 1.8 * read_adc(AIN3, adc_average_count , ain3_divider , adc_offset)
# p3p3v           = 1.8 * read_adc(AIN4, adc_average_count , ain4_divider , adc_offset)
# batt_thermistor = 1.8 * read_adc(AIN5, adc_average_count , ain5_divider , adc_offset)
# batt_v          = 1.8 * read_adc(AIN6, adc_average_count , ain6_divider , adc_offset)



# print("ZH voltage                   = {:0.4f}V".format(zh))
# print("Lid thermistor voltage       = {:0.4f}V".format(lid_thermistor))
# print("+12V                         = {:0.4f}V".format(p12v))
# print("+5V                          = {:0.4f}V".format(p5v))
# print("+3.3V voltage                = {:0.4f}V".format(p3p3v))
# print("Battery thermistor voltage   = {:0.4f}V".format(batt_thermistor))
# print("Battery voltage              = {:0.4f}V".format(batt_v))
