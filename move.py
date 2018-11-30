import json
from os import path

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# =========== loading the settings =========== #
# one direction
forward_pwm = 50
back_pwm = 50
turbo_pwm = 100
# turning
turning_side_pwm = 50
opposite_pwm = 100
#half turning
halfTurningPwm = 50
halfTurningPwmOpp = 100


# loading function
def loadSettings():
    myfile_path = path.join(path.dirname(__file__), 'settings.json')
    with open(myfile_path, "r") as settings:
        global forward_pwm, back_pwm, turbo_pwm, turning_side_pwm, opposite_pwm, halfTurningPwm, halfTurningPwmOpp
        res = json.load(settings)
        forward_pwm = res.get("forward_pwm")
        back_pwm = res.get("back_pwm")
        turbo_pwm = res.get("turbo_pwm")
        turning_side_pwm = res.get("turning_side_pwm")
        opposite_pwm = res.get("opposite_pwm")
        halfTurningPwm = res.get("halfTurningPwm")
        halfTurningPwmOpp = res.get("halfTurningPwmOpp")
    print ("settings updated")

# =========== leftside =========== 
left_pwm = 4 #left pwm
left_output_1 = 27 #leftside output 1
left_output_2 = 22 #leftside output 2

GPIO.setup(left_pwm, GPIO.OUT)
GPIO.setup(left_output_1, GPIO.OUT)
GPIO.setup(left_output_2, GPIO.OUT)
leftside = GPIO.PWM(left_pwm, 50)
leftside.start(0)

# =========== rightside =========== 
right_pwm = 17#right pwm
right_output_1 = 6 #rightside output 1
right_output_2 = 5 #rightside output 2

GPIO.setup(right_pwm, GPIO.OUT)
GPIO.setup(right_output_1, GPIO.OUT)
GPIO.setup(right_output_2, GPIO.OUT)
rightside = GPIO.PWM(right_pwm, 50)
rightside.start(0)

def control(left_1, right_1, left_2, right_2, left_dutycycle, right_dutycycle):
    GPIO.output(left_output_1, left_1) #setting the leftside output 1 to high or low
    GPIO.output(right_output_1, right_1) #setting the rightside output 1 to high or low
    GPIO.output(left_output_2, left_2) #setting the leftside output 2 to high or low
    GPIO.output(right_output_2, right_2) #setting the rightside output 2 to high or low
    leftside.ChangeDutyCycle(left_dutycycle) #changing the dutycycle of the left side
    rightside.ChangeDutyCycle(right_dutycycle) #changing the dutycycle of the right side

def fast_forward():
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, turbo_pwm, turbo_pwm)
    print("fast-forward")
def fast_back(): 
    control(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, turbo_pwm, turbo_pwm)
    print("fast-back")
def forward():
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, forward_pwm, forward_pwm)
    print("forward")
def back():
    control(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, back_pwm, back_pwm)
    print("back")
def right():
    print("right")
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HiGH, opposite_pwm, turning_side_pwm)
def left():
    print("left")
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, turning_side_pwm, opposite_pwm)
def forward_right():
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, halfTurningPwmOpp, halfTurningPwm)
    print("forward-right")
def forward_left():
    control(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, halfTurningPwm, halfTurningPwmOpp)
    print("forward-left")
def back_right():
    control(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, halfTurningPwmOpp, halfTurningPwm)
    print("back-right")
def back_left():
    control(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, halfTurningPwm, halfTurningPwmOpp)
    print("back-left")
def stop():
    print("stop")
    control(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW, 0, 0)
