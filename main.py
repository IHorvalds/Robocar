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
import sys
#import bluetooth

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
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### Sensor Setup
GPIO.setup(light1,              GPIO.IN)
GPIO.setup(light2,              GPIO.IN)
GPIO.setup(light3,              GPIO.IN)
GPIO.setup(light4,              GPIO.IN)
GPIO.setup(sonicSensorTrigger,  GPIO.IN)
GPIO.setup(echoPin,             GPIO.IN)

### Motor Setup

GPIO.setup(pwmRight,    GPIO.OUT)
GPIO.setup(pwmLeft,     GPIO.OUT)
GPIO.setup(ain1,        GPIO.OUT)
GPIO.setup(ain2,        GPIO.OUT)
GPIO.setup(bin1,        GPIO.OUT)
GPIO.setup(bin2,        GPIO.OUT)

rightOut = GPIO.PWM(pwmRight, 50) ### 100Hz
leftOut  = GPIO.PWM(pwmLeft, 50) ### 100Hz

motorRight = (ain2, ain1)
motorLeft = (bin2, bin1)


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

def lineFollowing():
    try:
        rightOut.start(0)
        leftOut.start(0)
        speed = 60
        #moveForward(motorRight, rightOut, GPIO, speed)
        #moveForward(motorLeft, leftOut, GPIO, speed)
        print("Start moving forward")
        while True:
                l1 = readLightSensor(light1, GPIO)
                l2 = readLightSensor(light2, GPIO)
                l3 = readLightSensor(light3, GPIO)
                l4 = readLightSensor(light4, GPIO)
                if l2 == 1 and l1 == 0:
                    turnRight(rightOut, 60) ### this will turn harder and harder until it recognises something as a straight line
                    print("Turn right")
                #    moveForward(motorRight, rightOut, GPIO, speed)
                if l4 == 0 and l3 == 1:
                    turnLeft(leftOut, 60)
                    print("Turn left")
                #    moveForward(motorLeft, leftOut, GPIO, speed)
                if l1 == 1 and l2 == 1 and l3 == 1 and l4 == 1:
                    moveForward(motorRight, rightOut, GPIO, speed)
                    moveForward(motorLeft, leftOut, GPIO, speed)
                if l1 == 0 and l4 == 0 and l2 == 1 and l3 == 1:
                #    """
                #    Mind you, this might not be aligned to the actual line,
                #    but alignment will be accomplished by the turning functions
                #    """
                    moveForward(motorRight, rightOut, GPIO, speed)
                    moveForward(motorLeft, leftOut, GPIO, speed)
                    print("Forward")
                #print("Idk wtf is going on")
    except Exception as exc:
        print(exc)
        stop(motorLeft, leftOut, GPIO)
        stop(motorRight, rightOut, GPIO)
        sys.exit(0)

#def bluetoothControl():
#    serverSocket = bluetooth.BlueToothSocket(bluetooth.RFCOMM)
#    port = 12
#    serverSocket.bind(("", port))
#    serverSocket.listen(2) ## read from 2 incoming connections
#    ### ERGO, multithread this

lineFollowing()
