from typing import Tuple

def turnLeft(pwmLeft, delta) -> int: #### NOTE: delta value should be calibrated to experimental values. delta belongs to [0, 100]
    try:
        pwmLeft.ChangeDutyCycle(100 - delta)
        return 0
    except:
        return -1
