from Sensors.sonicSensor import readSonicSensor
import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
trigger = 26
sonic = 19
GPIO.setwarnings(False)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(sonic, GPIO.IN)
while True:
    print(readSonicSensor(trigger, sonic, GPIO))
GPIO.cleanup()
