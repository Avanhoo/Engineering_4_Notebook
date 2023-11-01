# Triangle Are Solver and Dispayer - Afton Van Hooser
import board
import busio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle


displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done

i2c = busio.I2C(board.GP17, board.GP16)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

x = 0
y = 1

def qdisp(title): # Stands for quick display. Creates a function that runs all the lines nececarry to update the display in one line
    splash = displayio.Group() # create the display group
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
    splash.append(text_area)    
    display.show(splash)# send display group to screen

def qgraph(c1,c2,c3,A):
    scale = 1
    x0 = 64
    y0 = 32
    splash = displayio.Group()

    for i in range (1,7):
        scale = i
        if (abs(c1[x])*scale > 60) or (abs(c2[x])*scale > 60) or (abs(c3[x])*scale > 60):
            scale = i-1
            break

        elif (abs(c1[y])*scale > 30) or (abs(c2[y])*scale > 30) or (abs(c3[y])*scale > 30):
            scale = i-1
            break


    hline = Line(0,y0,128,y0, color=0xFFFF00)
    vline = Line(x0,0,x0,64, color=0xFFFF00)
    circle = Circle(x0, y0, 2*scale, outline=0xFFFF00)
    text = label.Label(terminalio.FONT, text=f"A={A}\n\n\n{scale}x", color=0xFFFF00, x=5, y=5)
    splash.append(hline) 
    splash.append(vline)
    splash.append(circle)
    splash.append(text)

    triangle = Triangle((c1[x])*scale+x0, (-c1[y])*scale+y0, (c2[x])*scale+x0, (-c2[y])*scale+y0, (c3[x])*scale+x0, (-c3[y])*scale+y0, outline=0xFFFF00)
    splash.append(triangle)

    display.show(splash)


def area():
    c1 = []
    c2 = []
    c3 = []

    while (c1 or c2 or c3) == []:
        r1 = input("Coordinate 1: ")
        try:                    # Coordinate 1
            c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
            a = c1[0] + c1[1]
            qdisp(f"Coordinates: \n c1: {c1}")

            r2 = input("Coordinate 2: ")
            try:                # Coordinate 2
                c2 = [int(o) for o in r2.split(",")]
                qdisp(f"Coordinates: \n c1: {c1} \n c2: {c2}")

                r3 = input("Coordinate 3: ")
                try:            # Coordinate 3
                    c3 = [int(o) for o in r3.split(",")]
                    A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                    qdisp(f" c1: {c1} \n c2: {c2} \n c3: {c3} \nArea: {A}") # add title block to display group
                    sleep(1)
                    qgraph(c1,c2,c3,A)
                    return A

                except:
                    print("Invalid Coordinate 3 , please enter in 'x,y' format")
                    continue
                    
            except:
                print("Invalid Coordinate 2, please enter in 'x,y' format")
                continue
                
        except:
            print("Invalid Coordinate 1 , please enter in 'x,y' format")
            continue


while True:
    area()