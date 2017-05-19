from Adafruit_BBIO import ADC

AIN0 = "P9_39"  #ZH
AIN1 = "P9_40"  #Lid thermistor
AIN2 = "P9_37"  #+12V
AIN3 = "P9_38"  #+5V
AIN4 = "P9_33"  #+3.3V
AIN5 = "P9_36"  # Battery thermistor   
AIN6 = "P9_35"  # Battery voltage

adc_average_count = 100

ain0_divider = 1
ain1_divider = 1
ain2_divider = 1
ain3_divider = 1
ain4_divider = 1
ain5_divider = 1
ain6_divider = 1

#These values should reside in file and loaded at boot
ain0_offset = 0
ain1_offset = 0
ain2_offset = 0
ain3_offset = 0
ain4_offset = 0
ain5_offset = 0
ain6_offset = 0






adc_offset = 0.004  #This value should reside in file

ADC.setup()

def read_adc(adc_chan, loop_count):
    adc_value = 0
    for num in range (1, loop_count):
        adc_value += ADC.read(adc_chan)
    adc_value /= num
    return adc_value

zh              = 1.8 * read_adc(AIN0, adc_average_count) * ain0_divider + adc_offset
lid_thermistor  = 1.8 * read_adc(AIN1, adc_average_count) * ain1_divider + adc_offset
p12v            = 1.8 * read_adc(AIN2, adc_average_count) * ain2_divider + adc_offset
p5v             = 1.8 * read_adc(AIN3, adc_average_count) * ain3_divider + adc_offset
p3p3v           = 1.8 * read_adc(AIN4, adc_average_count) * ain4_divider + adc_offset
batt_thermistor = 1.8 * read_adc(AIN5, adc_average_count) * ain5_divider + adc_offset
batt_v          = 1.8 * read_adc(AIN6, adc_average_count) * ain6_divider + adc_offset



print("ZH voltage                   = {:0.4f}V".format(zh))
print("Lid thermistor voltage       = {:0.4f}V".format(lid_thermistor))
print("+12V                         = {:0.4f}V".format(p12v))
print("+5V                          = {:0.4f}V".format(p5v))
print("+3.3V voltage                = {:0.4f}V".format(p3p3v))
print("Battery thermistor voltage   = {:0.4f}V".format(batt_thermistor))
print("Battery voltage              = {:0.4f}V".format(batt_v))