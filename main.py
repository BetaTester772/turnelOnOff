#
# Created by 안호성 on 2022-10-26.
#


import time

import RPi.GPIO as GPIO  # 'RPi.GPIO-def (version: 0.2)' Package in PyCharm.

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO Sensor Setup
GPIO.setup(17, GPIO.IN)  # Sensor 1
GPIO.setup(27, GPIO.IN)  # Sensor 2
GPIO.setup(22, GPIO.IN)  # Sensor 3
GPIO.setup(5, GPIO.IN)  # Sensor 4
GPIO.setup(13, GPIO.IN)  # Sensor 5

# GPIO LED Setup
GPIO.setup(6, GPIO.OUT)  # LED 1
GPIO.setup(19, GPIO.OUT)  # LED 2
GPIO.setup(26, GPIO.OUT)  # LED 3
GPIO.setup(24, GPIO.OUT)  # LED 4

# make Sector var
SeCtor1 = 0
SeCtor2 = 0
SeCtor3 = 0
SeCtor4 = 0

# loop process
while True:
    # make and set Sensor var with Sensor value
    Sen1 = GPIO.input(17)
    Sen2 = GPIO.input(27)
    Sen3 = GPIO.input(22)
    Sen4 = GPIO.input(5)
    Sen5 = GPIO.input(13)

    # Delay
    time.sleep(0.05)

    # Set Sector value with Sensor Value
    if Sen1:
        SeCtor1 += 1
        SeCtor2 += 1
    elif Sen2:
        SeCtor1 -= 1
        SeCtor3 += 1
    elif Sen3:
        SeCtor2 -= 1
        SeCtor4 += 1
    elif Sen4:
        SeCtor3 -= 1
    elif Sen5:
        SeCtor4 -= 1

    # Set LED On/Off with Sector value
    if SeCtor1 > 0:
        GPIO.output(6, GPIO.HIGH)
        print(1, end=' ')
    else:
        GPIO.output(6, GPIO.LOW)
        print(0, end=' ')

    if SeCtor2 > 0:
        GPIO.output(19, GPIO.HIGH)
        print(1, end=' ')
    else:
        GPIO.output(19, GPIO.LOW)
        print(0, end=' ')

    if SeCtor3 > 0:
        GPIO.output(26, GPIO.HIGH)
        print(1, end=' ')
    else:
        GPIO.output(26, GPIO.LOW)
        print(0, end=' ')

    if SeCtor4 > 0:
        GPIO.output(24, GPIO.HIGH)
        print(1, end=' ')
    else:
        GPIO.output(24, GPIO.LOW)
        print(0, end=' ')

    print(True)
