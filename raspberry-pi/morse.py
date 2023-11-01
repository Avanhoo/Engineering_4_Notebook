# Morse code translator - Afton Van Hooser
print("Morse code translator - Afton Van Hooser")
finalTxt = ""
char = 0
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

    if "-Q" in rawTxt: # Checks if user would like to exit
        exit()
    try:
        for char in range(len(rawTxt)): # Iterates through each character of the input text
            finalTxt += MORSE_CODE[rawTxt[char]] + " " # Translates and adds a space
    except:
        finalTxt = f'--Invalid input: "{rawTxt[char]}"' # Tells you if a character you typed was invalid

    print(finalTxt)