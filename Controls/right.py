from typing import Tuple

def turnRight(pwmRight, delta) -> int: #### NOTE: delta value should be calibrated to experimental values.
                                             ### delta belongs to [0, 100]
    try:
        pwmRight.ChangeDutyCycle(60 - delta)
        return 0
    except Exception as err:
        print(err)
        return -1
