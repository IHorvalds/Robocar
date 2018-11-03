from Sensors.lightSensors   import readLightSensor
from Sensors.sonicSensor    import readSonicSensor

import RPi.GPIO as GPIO
import time     as t

light1 = 18
light2 = 23
light3 = 24
light4 = 25
sonicSensorTrigger = 13
echoPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(light1, GPIO.IN)
GPIO.setup(light2, GPIO.IN)
GPIO.setup(light3, GPIO.IN)
GPIO.setup(light4, GPIO.IN)
GPIO.setup(sonicSensorTrigger, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setwarnings(False)

try:
    while True:
        for sensor in [18, 23, 24, 25]:
            print("Light sensor " + str(sensor) + ": ", readLightSensor(sensor, GPIO))
        print("Sonic sensor: ", readSonicSensor(sonicSensorTrigger, echoPin, GPIO))
        t.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Closed")
