import RPi.GPIO as GPIO
import time
import math

#define the buzzerPin
buzzerPin = 11
#Define the buttonPin
buttonPin = 12

def setup():
    global p
    #Use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set RGBLED pins to OUTPUT mode
    GPIO.setup(buzzerPin, GPIO.OUT)
    #Set buttonPin to INPUTmode, and pull up to HiGH level, 3.3V
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            alertor()
            print("Alertor turned on >>>")
        else:
            stopAlertor()
            print("Alertor turned off <<<")

def alertor():
    p.start(50)
    #Make frequency of the alertor consistent with the sine wave
    for x in range(0, 361):
        #Calculate he sine value
        sinVal = math.sin(x * (math.pi / 180.0))
        #add to the resonant frequency with a Weighted
        toneVal = 2000 + sinVal * 500
        #Change Frequency of PWM to toneVal
        p.ChangeFrequency(toneVal)
        time.sleep(0.001)

def stopAlertor():
    p.stop()

def destroy():
    #Turn off buzzer
    GPIO.output(buzzerPin, GPIO.LOW)
    #Release GPIO resource
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