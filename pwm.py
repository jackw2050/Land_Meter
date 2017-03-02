import Adafruit_BBIO.PWM as PWM
#PWM.start(channel, duty, freq=2000, polarity=0)
PWM.start("P9_14", 50)

#optionally, you can set the frequency as well as the polarity from their defaults:
PWM.start("P9_14", 50, 1000, 1)




PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)



PWM.stop("P9_14")
PWM.cleanup()