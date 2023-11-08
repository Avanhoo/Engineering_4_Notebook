'''import board
import busio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect'''
from math import cos, sin, tan

'''displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done
i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)'''

fov = 60
pX = 0
pY = 0
pr = 0

rows, cols = (64,128)
map = [[0]*cols]*rows
map[1][0] = 1
disp = [[0]*cols]*rows
print(map)

def refresh():
    for yray in range(1,64): # Up to down
        for xray in range (1,128): # Left to right
            xval = pX
            yval = pY
            for i in range(0,10):
                xval += cos(pr-(xray/2)+xray)
                yval += sin(pr-(xray/2)+xray)
                if map[int(xval)][int(yval)] == 1:
                    disp[int(xval)][int(yval)] = 1
splash = displayio.Group()
while True:
    inp = input("-")
    if inp == "a":
        pr += 15
    elif inp == "d":
        pr -= 15
                
