import RPi.GPIO as GPIO
import time
import random

#Define the pins for RGBLED
pins = {"pinRed": 11, "pinGreen": 12, "pinBlue": 13}

def setup():
    global pwmRed, pwmGreen, pwmBlue
    #Use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set RGBLED pins to OUTPUT mode
    GPIO.setup(pins, GPIO.OUT)
    #Make RGBleD pins output HIGH level
    GPIO.output(pins, GPIO.HIGH)
    #Set PWM Frequence to 2kHz
    pwmRed = GPIO.PWM(pins["pinRed"], 2000)
    #Set PWM Frequence to 2kHz
    pwmGreen = GPIO.PWM(pins["pinGreen"], 2000)
    #Set PWM Frequence to 2kHz
    pwmBlue = GPIO.PWM(pins["pinBlue"], 2000)
    #Set initial Duty Cycle to 0
    pwmRed.start(0)
    pwmGreen.start(0)
    pwmBlue.start(0)

#Change duty cycle for three pins to r_val, g_val, b_val
def setColor(r_val, g_val, b_val):
    #Change pwmRed duty cycle to r_val
    pwmRed.ChangeDutyCycle(r_val)
    pwmGreen.ChangeDutyCycle(g_val)
    pwmBlue.ChangeDutyCycle(b_val)

def loop():
    while True:
        #Get a random in (0, 100)
        r=random.randint(0, 100)
        g=random.randint(0, 100)
        b=random.randint(0, 100)
        #Set random as a duty cycle value
        setColor(r, g, b)
        print("r = %d, g = %d, b = %d" %(r, g, b))
        time.sleep(1)

def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

#Program entrance
if __name__ == "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    #Press ctrl-c to end the program
    except KeyboardInterrupt:
        destroy()