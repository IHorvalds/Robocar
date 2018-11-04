import time as t

def readLightSensor(pin: int, gpio) -> float:
    try:
        colourVal = gpio.input(pin)
        print(colourVal)
        return colourVal
    except Exception as err:
        print(err)
        return -1
