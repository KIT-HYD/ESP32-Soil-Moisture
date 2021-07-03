# main.py
from machine import ADC, Pin, deepsleep

import sm


# read in the config
conf = sm.config()

# define the ADC
adc = ADC(Pin(32))

# do the measurement
moisture, raw = sm.read(adc, conf.get('calibrationAir'), conf.get('calibrationWater'))

# here you can sent the data somewhere
print("%.0f%%  - [ADC: %d]" % (moisture, raw))

# go to deepsleep for given amount of miliseconds
deepsleep(conf.get('step'), 10000)
