import RPi.GPIO as GPIO
import time

#Define the buzzerPin
buzzerPin = 11

morseCharacters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
                   "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ""]

global p

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0)

def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()

def translate(string):
    translatedText = ""
    for character in string:
        character = character.lower()
        ascii = ord(character)
        if ascii > 96 and ascii < 123:
            translatedText += morseCharacters[ascii - 97] + " "
        elif ascii > 47 and ascii < 58:
            translatedText += morseCharacters[ascii - 48 + 25] + " "
        elif ascii == 32:
            translatedText += "   "
    return translatedText

def beep(string):
    for character in string:
        print(character)
        if character == ".":
            GPIO.output(buzzerPin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(buzzerPin, GPIO.LOW)
        elif character == "-":
            GPIO.output(buzzerPin, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(buzzerPin, GPIO.LOW)
        else:
            time.sleep(0.4)
        time.sleep(0.3)
        
def main():
    setup()
    userInput = input("Enter English text por favor:\n")
    translatedText = translate(userInput)
    try:
        beep(translatedText)
    except KeyboardInterrupt():
        destroy()
    
main()
