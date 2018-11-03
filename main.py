#!/bin/python3

from Sensors.lightSensors   import readLightSensor
from Sensors.sonicSensor    import readSonicSensor
from Controls.fwd           import moveForward
from Controls.bwd           import moveBackward
from Controls.stop          import stop
from Controls.left          import turnLeft
from Controls.right         import turnRight

import RPi.GPIO as GPIO
import time     as t

### Sensors
light1              = 23
light2              = 24
light3              = 25
light4              = 7
sonicSensorTrigger  = 13
echoPin             = 19

### Motors
pwmRight    = 17
ain1        = 6
ain2        = 5
pwmLeft     = 4
bin1        = 27
bin2        = 22

### Setup. Lots of typing for clarity
GPIO.setmode(BCM)
GPIO.setwarnings(False)

### Sensor Setup
GPIO.setup(light1,              GPIO.OUT)
GPIO.setup(light2,              GPIO.OUT)
GPIO.setup(light3,              GPIO.OUT)
GPIO.setup(light4,              GPIO.OUT)
GPIO.setup(sonicSensorTrigger,  GPIO.OUT)
GPIO.setup(echoPin,             GPIO.IN)

### Motor Setup

GPIO.setup(pwmRight,    GPIO.OUT)
GPIO.setup(pwmLeft,     GPIO.OUT)
GPIO.setup(ain1,        GPIO.OUT)
GPIO.setup(ain2,        GPIO.OUT)
GPIO.setup(bin1,        GPIO.OUT)
GPIO.setup(bin2,        GPIO.OUT)


############################### DEFINE LINE FOLLOWING LOGIC ################################
### light sensor is 1 when reflecting off white, 0 when reflecting from black (d = 1mm) # TODO: Test longer distances

### GO FORWARD
### l1 l2 l3 l4
###  1  0  0  1

### GO LEFT
### l1 l2 l3 l4
###  0  ?  1  1

### GO RIGHT
### l1 l2 l3 l4
###  1  1  ?  0
