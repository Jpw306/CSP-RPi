import RPi.GPIO as GPIO
import time

#Define ledPin
ledPin = 11

def setup():
    #Use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set the ledPin to OUTPUT mode
    GPIO.setup(ledPin, GPIO.OUT)
    #Make ledPin output LOW level
    GPIO.output(ledPin, GPIO.LOW)
    print("Using pin%d" %ledPin)

def loop():
    while True:
        #Make ledPin output HIGH level to turn on LED
        GPIO.output(ledPin, GPIO.HIGH)
        #Print information on terminal
        print("LED turned On >>>")
        #Wait for 1 second
        time.sleep(1)
        #Make ledPin output LOW level to turn off LED
        GPIO.output(ledPin, GPIO.LOW)
        print("LED turned Off <<<")
        #Wait for 1 second
        time.sleep(1)

def destroy():
    #Release all GPIO
    GPIO.cleanup()

#Program entrance
if __name__ == "__main__":
    print("Program is starting...\n")
    setup()
    try:
        loop()
    #Press ctrl-c to end the program
    except KeyboardInterrupt:
        destroy()