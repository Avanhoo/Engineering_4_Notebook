import board
import busio
import digitalio
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050
import servo
from time import sleep, monotonic

sda_pin = board.GP16
scl_pin = board.GP17
#i2c = busio.I2C(scl_pin, sda_pin)
#imu = adafruit_mpu6050.MPU6050(i2c)

sled = digitalio.DigitalInOut(board.LED)
sled.direction = digitalio.Direction.OUTPUT

button = DigitalInOut(board.GP28) # 7th pin down, right side
button.direction = Direction.INPUT
button.pull = Pull.UP

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
elevator = servo.Servo(pwm)
lAiler = servo.Servo(pwm) # Left Aileron
rAiler = servo.Servo(pwm) # Right Aileron


def store():
    datalog.write(f"{monotonic()},{imu.acceleration[0]},{imu.acceleration[1]},{imu.acceleration[2]},{tilt}\n") # Writes the time, x, y, z acceleration, and if tilted to a file 
    datalog.flush()

    sled.value = True # Flashes onboard LED
    sleep(delay/2)
    sled.value = False
    sleep(delay/2)
#with open("/data.csv", "a") as datalog: # Opens the data 

timer = 0
while timer >= 0: # Wing coupling loop
    timer = monotonic()
    while not button.value:  
        if (monotonic() > timer+1): # ADD "and coupling = engaged"
            timer = -1 # Breaks out of the big loop
            print("done")
            break
        elif button.value:
            # Toggle coupling system
            print("toggle")
            break

import board
import wifi

wifi.radio.connect("test", "testtesttest")