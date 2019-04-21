import RPi.GPIO as GPIO
import time

fanPIN = 17

#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set all LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(fanPIN,GPIO.OUT,initial=GPIO.HIGH)

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
    # Turn off LED
    GPIO.output(fanPIN, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()
    pass

# If run this script directly, do:
if __name__ == '__main__':
    try:
        setup()
        GPIO.output(fanPIN, GPIO.HIGH)
        print('The fan is running: ')
        while True:
            print(GPIO.input(fanPIN))
            time.sleep(1)
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()

