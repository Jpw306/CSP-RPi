import RPi.GPIO as GPIO
import time

#Define the buzzerPin
buzzerPin = 11

morseCharacters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
                   "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ""]

def setup():
    global p
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
        GPIO.output(buzzerPin, GPIO.HIGH)
        if character == ".":
            time.sleep(0.1)
        elif character == "-":
            time.sleep(0.3)
        else:
            time.sleep(0.4)
        GPIO.output(buzzerPin, GPIO.LOW)
        time.sleep(0.3)
        
def main():
    setup()
    try:
        userInput = input("Enter English text por favor:\n")
        translatedText = translate(userInput)
        beep(translatedText)
    except KeyboardInterrupt:
        destroy()