from typing import Tuple

def moveBackward(pins: tuple, pwm, gpio, speed: float) -> int:
    try:
        pwm.ChangeDutyCycle(speed)
        gpio.output(pins[0], 0)
        gpio.output(pins[1], 1)
        return 0
    except:
        return -1
