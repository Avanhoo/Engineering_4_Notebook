import board
import busio
import adafruit_mpu6050
import digitalio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label

digitalio.DigitalInOut(board.GP17).deinit()

i2c = busio.I2C(board.GP17, board.GP16)
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17

x = 0
y = 0
z = 0
delay = .1

sleep(delay)

while True:
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}")
    if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3:
        led.value = True
    else:
        led.value = False

    # create the display group
    splash = displayio.Group()

    # add title block to display group
    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    

    # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)

    sleep(delay)
