from typing import Tuple

def moveForward(pins: tuple, pwm, gpio, speed: float) -> int:
    try:
        pwm.ChangeDutyCycle(speed)
        gpio.output(pins[0], 1)
        gpio.output(pins[1], 0)
        return 0
    except:
        return 1
