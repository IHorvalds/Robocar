from typing import Tuple
import sys

def stop(pins: tuple, pwm, gpio) -> int:
    try:
        pwm.ChangeDutyCycle(0)
        gpio.output(pins[0], 0)
        gpio.output(pins[1], 0)
        return 0
    except Exception as err:
        gpio.cleanup()
        print("Couldn't stop the motors. Something went wrong.")
        print("Error: " + err)
        sys.exit(-1)
