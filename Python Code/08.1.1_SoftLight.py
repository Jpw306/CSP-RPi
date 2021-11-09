import RPi.GPIO as GPIO 
import time
from ADCDevice import *

ledPin = 11
#Define an ADCDevice class object
adc = ADCDevice()

def setup():
    global adc
    #Detect the pcf8591
    if(adc.detectI2C(0x48)):
        adc = PCF8591()
    #Detect the ads7830
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n")
        exit(-1)
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    p = GPIO.PWM(ledPin, 1000)
    p.start(0)