import board
import busio
import adafruit_mpu6050
import digitalio
from time import sleep

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sled = digitalio.DigitalInOut(board.LED)
sled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)
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
    sleep(delay)