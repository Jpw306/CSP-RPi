import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():
    #Use Physical GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set all ledPins to OUTPUT mode
    GPIO.setup(ledPins, GPIO.OUT)
    #Make all ledPins output HIGH level, turn off all led
    GPIO.output(ledPins, GPIO.HIGH)

def loop():
    while True:
        #Make LED(on) move from left to right
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        #Make LED(on) move from right to left
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

def destroy():
    #Release all GPIO
    GPIO.cleanup()

#Program entrnace
if __name__ == "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    #Press ctrl-c to end the program
    except KeyboardInterrupt:
        destroy()