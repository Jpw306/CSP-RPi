import RPi.GPIO as GPIO
import time

#Define the LedPin
LedPin = 12

def setup():
    global p
    #use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set LedPin to OUTPUT mode
    GPIO.setup(LedPin, GPIO.OUT)
    #Make ledPin output LOW level to turn off LED
    GPIO.output(LedPin, GPIO.LOW)

    #Set PWM Frequence to 500Hz
    p = GPIO.PWM(LedPin, 500)
    #Set initial Duty Cycle to 0
    p.start(0)

def loop():
    while True:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    #Stop PWM
    p.stop()
    #Release all GPIO
    GPIO.cleanup()

#Program entrance
if __name__ == "__main__":
    print("Program is starting... ")
    setup()
    try:
        loop()
    #Press ctrl-c to end the program
    except KeyboardInterrupt:
        destroy()