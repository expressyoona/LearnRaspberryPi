#!/usr/bin/env python3 

"""
$      If KEY_1 is pressed,this script will be executed,LED1 will turn on(or off)
$      LED1 connect to GPIO5(BCM_GPIO 24)
"""
import RPi.GPIO as GPIO
import sys

PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.OUT)

mode = sys.argv[-1]

if mode == 'on':
     GPIO.output(PIN, GPIO.HIGH)
elif mode == 'off':
     GPIO.output(PIN, GPIO.LOW)
else:
     pass

"""
if GPIO.input(PIN) == 0:
     GPIO.output(PIN, GPIO.HIGH)
else:
     GPIO.output(PIN, GPIO.LOW)
"""
