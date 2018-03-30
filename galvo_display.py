import gaugette.ssd1306
import gaugette.gpio
import gaugette.spi
import time


ROWS = 32  # set to 64 for 128x64 display

RESET_PIN = "P9_15"
DC_PIN    = "P9_23"

# fonts = []
# from gaugette.fonts import arial_16

# fonts = [arial_16]
          
          
          
          

gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(bus=0, device=0)
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=ROWS, cols=128, buffer_cols=256)
# led.reset()
led.begin()
led.clear_display()

offset = 0
led.draw_text2(0,0,'Hello World',2)
led.display()