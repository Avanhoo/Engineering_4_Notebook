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
import pygame

'''displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done
i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)'''

fov = 60
pX = 0
pY = 0
pr = 0

cols, rows = (2,64)
map = [[0]*cols]*rows # Creates an array of 128 x 64
disp = [[0]*cols]*rows

pygame.init()
screen = pygame.display.set_mode((128,64))
clock = pygame.time.Clock()
running = True


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



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.image.frombuffer(map, (cols, rows), "RGB")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()