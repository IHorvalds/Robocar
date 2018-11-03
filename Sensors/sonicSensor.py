import time as t

def readSonicSensor(triggerPin: int, echoPin: int, gpio) -> float:
    try:
        pingtime = 0
        echotime = 0
        gpio.output(triggerPin, gpio.HIGH)
        pingtime=t.time()
        t.sleep(0.00001)
        gpio.output(triggerPin, gpio.LOW)
        while gpio.input(echoPin) == 0:
            pingtime = t.time()
        while gpio.input(echoPin) == 1:
            echotime = t.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        return distance
    except Exception as err:
        print(err)
        return -1
