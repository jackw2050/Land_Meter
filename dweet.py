simport requests, psutil, datetime

# http://dweet.io/follow/5c7da3e6-22ad-4951-b8e7-860a3fadb026

# Replace "x" sequence with your UUID:
thing_name = "5c7da3e6-22ad-4951-b8e7-860a3fadb026"
#UUID('5c7da3e6-22ad-4951-b8e7-860a3fadb026')


def dweet(thing, **vals):
  url = "http://dweet.io/dweet/for/{}".format(thing)
  requests.post(url, params=vals)
  
#def get_cpu_temp_c():
#   temp_file = "/sys/class/hwmon/hwmon0/device/temp1_input"
#   with open(temp_file, "r") as f:
#       return int(f.read())/1000
       
def get_uptime():
   with open("/proc/uptime", "r") as f:
       raw = f.read()
   seconds = float(raw.split()[0])
   return seconds

while True:
  uptime_s = get_uptime()
  uptime_datetime = datetime.datetime.fromtimestamp(uptime_s)
  uptime = uptime_datetime.strftime("%H:%M:%S")
  load = psutil.cpu_percent(interval=2)
#  temp = get_cpu_temp_c()
  mem = psutil.virtual_memory()[2]
  net_info = psutil.net_io_counters()
  eth_up = net_info[2]
  eth_down = net_info[3]

  dweet(thing_name, uptime=uptime, cpu_load=load,
  memory=mem, eth_up=eth_up, eth_down=eth_down)