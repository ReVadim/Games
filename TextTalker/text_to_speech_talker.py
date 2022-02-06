import pyttsx3
import sys


tts = pyttsx3.init()

print('Enter the text to speak, or "Q" to quit')

while True:
    text = input('> ')
    if text.upper() == 'Q':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)
    tts.runAndWait()
