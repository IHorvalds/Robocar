from Controls.fwd   import moveForward
from Controls.bwd   import moveBackward
from Controls.right import turnRight
from Controls.left  import turnLeft
from Controls.stop  import stop

import RPi.GPIO as GPIO
import time     as t


pwmRight    = 17
ain1        = 6
ain2        = 5
pwmLeft     = 4
bin1        = 27
bin2        = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ain1, GPIO.OUT)
GPIO.setup(ain2, GPIO.OUT)
GPIO.setup(bin1, GPIO.OUT)
GPIO.setup(bin2, GPIO.OUT)
GPIO.setup(pwmRight, GPIO.OUT)
GPIO.setup(pwmLeft, GPIO.OUT)


rightOut = GPIO.PWM(pwmRight, 100) ### 50Hz
leftOut  = GPIO.PWM(pwmLeft, 100) ### 50Hz

rightOut.start(0)
leftOut.start(0)

print("Move forward right: ", moveForward((ain1, ain2), rightOut, GPIO, 100))
print("Move forward left: ", moveForward((bin1, bin2), leftOut, GPIO, 100))
t.sleep(2)
print("Stop: ", stop((ain1, ain2), rightOut, GPIO))
print("Stop: ", stop((bin1, bin2), leftOut, GPIO))
t.sleep(2)
moveForward((ain1, ain2), rightOut, GPIO, 70)
moveForward((bin1, bin2), leftOut, GPIO, 70)
t.sleep(1)
print("Turning right 20%: ", turnRight(rightOut, 20))
t.sleep(2)
stop((ain1, ain2), rightOut, GPIO)
stop((bin1, bin2), leftOut, GPIO)
GPIO.cleanup()
