#!/usr/bin/python
###########################################################################
#Filename      :breathing_led.py
#Description   :make breath led
#Author        :alan
#Website       :www.osoyoo.com
#Update        :2017/06/26
############################################################################

import RPi.GPIO as GPIO
import time
import sys
import os

#set BCM_GPIO 18(GPIO1) as LED pin
LEDPIN = 17

value = None

fileName = 'config.txt'

#setup function for some setup---custom function
def setup():
    global p
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set all LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

    #set LEDPIN as PWM output,and frequency=100Hz
    p = GPIO.PWM(LEDPIN,100)


    #set p begin with value 0
    os.chdir('.')
    print(os.getcwd())
    print(os.listdir('.'))
    with open(fileName, 'r') as file:
        value = int(file.read())
    #p.start(0)
    p.start(value)
    pass

#main function

def getDutyCycle():
    return value

def writeValue(vl):
    with open(fileName, 'w') as file:
        file.write(vl)

def increaseBright():
    global value
    if value < 100 - 4:
        value += 4
        p.changeDutyCycle(value)
        writeValue(value)

def decreaseBright():
    global value
    if value > 0 + 4:
        value -= 4
        p.changeDutyCycle(value)
        writeValue(value)

def main():
    pass

#define a destroy function for clean up everything after the script finished
def destroy():
    #stop p
    p.stop()
    #turn off led
    GPIO.output(LEDPIN,GPIO.LOW)
    #release resource
    GPIO.cleanup()
    pass

# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
        mode = sys.argv[1]
        if mode == 'inc':
            increaseBright()
        elif mode == 'dec':
            decreaseBright()
        else:
            exit()
            
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        #destroy()
        pass
    pass
