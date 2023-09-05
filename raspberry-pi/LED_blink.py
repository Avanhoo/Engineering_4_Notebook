import board# type: ignore
import digitalio# type: ignore
from time import sleep
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
print("hello")


while True:
    led.value = True
    sleep(1)
    led.value = False
    sleep(1)