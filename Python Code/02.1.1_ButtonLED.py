import RPi.GPIO as GPIO

#Define ledPin
ledPin = 11 
#Define buttonPin
buttonPin = 12      

def setup():
    #Use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)  
    #Set ledPin to OUTPUT mode  
    GPIO.setup(ledPin, GPIO.OUT)    
    #Set buttonPin to PULL UP INPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    

def loop():
    while True:
        #If button is pressed
        if GPIO.input(buttonPin) == GPIO.LOW:
            #Turn on LED
            GPIO.output(ledPin, GPIO.HIGH)
            #Print information on terminal
            print("LED turned on >>>")
        #If button is released
        else:
            #Turn off LED
            GPIO.output(ledPin, GPIO.LOW)
            #Turn off LED
            print("LED turned off <<<")

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