import board
import busio
import adafruit_mpu6050
import adafruit_mpl3115a2
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
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) # Altimeter
#sensor.sealevel_pressure = 1017


led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT

delay = .1
baseAlt = sensor.altitude # base altitude your current position is measured against
Height = 0

sleep(delay)

while True:
    altitude = sensor.altitude
    if (baseAlt + 3 < altitude): # Checks if you're 3m above the starting point
        Height = 1
    else:
        Height = 0
    print("Altitude: {0:0.3f} meters".format(altitude))
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Uses fstring to place the rounded acceleration values into the string
    if (abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3 or (imu.acceleration[2] < 0)) and not (baseAlt + 3 < altitude): # Detects if the imu is tilted 90° in any direction
        led.value = True
    else:
        led.value = False

    splash = displayio.Group() # create the display group
    title = f"ANGULAR V: X:{round(imu.gyro[0]-.6,3)} \n           Y:{round(imu.gyro[1]+.2,3)} \n{Height}          Z:{round(imu.gyro[2],3)} \nAltitude: {altitude}" # add title block to display group
    
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
    splash.append(text_area)    
    
    display.show(splash)# send display group to screen

    sleep(delay)
