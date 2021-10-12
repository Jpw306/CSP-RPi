import RPi.GPIO as GPIO

#define buzzerPin
buzzerPin = 11
#Define buttonPin
buttonPin = 12

def setup():
    #Use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)
    #Set buzzerPin to OUTPUT mode
    GPIO.setup(buzzerPin, GPIO.OUT)
    #Set buttonPin to PULL UP
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        #If button is pressed
        if GPIO.input(buttonPin) == GPIO.LOW:
            #Turn on buzzer
            GPIO.output(buzzerPin, GPIO.HIGH)
            print("Buzzer turned on >>>")
        #If button is released
        else: 
            #Turn off buzzer
            GPIO.output(buzzerPin, GPIO.LOW)
            print("Buzzer turned off <<<")

def destroy():
    #release all GPIO
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