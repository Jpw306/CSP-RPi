import RPi.GPIO as GPIO

#Define ledPin
ledPin = 11
#Define buttonPin
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#When button is pressed, this function will be executed
def buttonEvent(channel):
    global ledState
    print("buttonEvent GPIO%d" %channel)
    ledState = not ledState
    if ledState:
        print("LED turned on >>>")
    else:
        print("LED turned off <<<")
    GPIO.output(ledPin, ledState)

def loop():
    #Button detect
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime = 300)
    while True:
        pass

def destroy():
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