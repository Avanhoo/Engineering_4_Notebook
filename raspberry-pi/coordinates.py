# Triangle Are Solver - Afton Van Hooser
import board
import busio
import digitalio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
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

def area():
    c1 = [0,0]
    c2 = [0,0]
    c3 = [0,0]
    
    try:                    # Coordinate 1
        r1 = input("Coordinate 1: ")
        c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
    except:
        print("Coordinate 1 Invalid, please enter in 'x,y' format")
        pass
    finally:

        qdisp(f"Coordinates: \n c1: {c1}")
        try:                # Coordinate 2
            r2 = input("Coordinate 2: ")
            c2 = [int(o) for o in r2.split(",")]
        except:
            print("Coordinate 2 Invalid, please enter in 'x,y' format")
            pass
        finally:

            qdisp(f"Coordinates: \n c1: {c1} \n c2: {c2}")
            try:            # Coordinate 3
                r3 = input("Coordinate 3: ")
                c3 = [int(o) for o in r3.split(",")]
            except:
                print("Coordinate 3 Invalid, please enter in 'x,y' format")
                pass

            finally:
                A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                qdisp(f"c1: {c1} \n c2: {c2} \n c3: {c3} \n Area: {A}") # add title block to display group


                

                return A




while True:
    print(area())