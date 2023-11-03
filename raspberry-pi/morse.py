# Morse code translator - Afton Van Hooser
import board
import digitalio
from time import sleep

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
print("Morse code translator - Afton Van Hooser")
finalTxt = ""
delay = .25
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    rawTxt = input("Input Text: ").upper() # Takes input from user and capitalizes it
    finalTxt = ""

    if "-Q" in rawTxt: # Checks if user would like to exit
        exit()
    try:
        for char in range(len(rawTxt)): # Iterates through each character of the input text
            finalTxt += MORSE_CODE[rawTxt[char]] + " " # Translates and adds a space
    except:
        finalTxt = f'--Invalid input: "{rawTxt[char]}"' # Tells you if a character you typed was invalid

    print(finalTxt)

    for i in range(len(finalTxt)):# Flashing light loop
        if finalTxt[i] == ".": #    Dot
            led.value = True
            sleep(delay)
            led.value = False
        elif finalTxt[i] == "-": #  Dash
            led.value = True
            sleep(delay*3)
            led.value = False
        elif finalTxt[i] == " ": #  Between letters: inherent delay(1) + 1 + inherent delay(1) = 3 delay
            sleep(delay)
        if finalTxt[i] == "/": #    Between words: letter delay(3) + 1 + letter delay(3) = 7 delay
            sleep(delay)
        else:
            sleep(delay) #          Inherent Delay after every cycle
        
