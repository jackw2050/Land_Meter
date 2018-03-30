#http://phant.io
import Adafruit_BBIO.ADC as ADC
import requests, time
PUBLIC_KEY = "q580YQ7mW8IJbdVLaQLo"
PRIVATE_KEY = "BVeW4XZg9eiP1Bgzw7zY"
def postData(data_dict):
 url = "http://data.sparkfun.com/input/{}".format(PUBLIC_KEY)
 headers = {"Phant-Private-Key" : PRIVATE_KEY}
 response = requests.post(url, headers=headers,
 params=data_dict)
ADC.setup()
try:
 while True:
 voltage = ADC.read("AIN0") * 1.8
 postData({"voltage" : voltage})
 time.sleep(1)
except KeyboardInterrupt:
 pass