# type: ignore
import board
import digitalio
from time import sleep

Rled = digitalio.DigitalInOut(board.GP2) # Fourth pin down, top left
Rled.direction = digitalio.Direction.OUTPUT
Gled = digitalio.DigitalInOut(board.GP0) # First pin, top left
Gled.direction = digitalio.Direction.OUTPUT


for i in range (10,0,-1): #start, stop, step; nice and clean
    print(i)
    Rled.value = True # Flash red
    sleep(.1)
    Rled.value = False
    sleep(.9)
print("Liftoff")
Gled.value = True
sleep(5)
