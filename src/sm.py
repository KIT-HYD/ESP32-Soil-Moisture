import ujson
from machine import ADC, Pin


def config(new_config = None):
    """
    Read and write to the config.json file
    """
    with open('config.json') as f:
        conf = ujson.load(f)
    
    if new_config is None:
        return conf
    else:
        conf.update(new_config)
    
    with open('config.json', 'w') as f:
        ujson.dump(conf, f, indent=4)
    
    return conf


def read(adc = None, calibrationAir = None, calibrationWater = None, attenuation = ADC.ATTN_11DB, resolution = ADC.WIDTH_10BIT, cycle=5):
    """
    Read a Capacitive soil moisture sensor with analog output.
    """
    # create an adc if not given
    if adc is None:
        adc = 32
    if isinstance(adc, int):
        adc = Pin(adc)
    if isinstance(adc, Pin):
        adc = ADC(adc)
    
    # check if the calibration values are given
    if calibrationAir is None or calibrationWater is None:
        conf = config()
        if calibrationAir is None:
            calibrationAir = conf.get('calibrationAir', 750)
        if calibrationWater is None:
            calibrationWater = conf.get('calibrationWater', 450)
    
    # configure the adc
    adc.atten = attenuation
    adc.width = resolution

    # read
    raw = 0
    for _ in range(cycle):
        raw += adc.read()
    raw /= cycle

    # map the value
    sm = (1- (raw - calibrationWater) / (calibrationWater - calibrationAir)) * 100

    return sm, raw