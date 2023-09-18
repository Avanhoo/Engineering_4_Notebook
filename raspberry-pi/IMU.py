import board
import busio
import adafruit_mpu6050
from time import sleep

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)
x = 0
y = 0
z = 0
xO = 0
yO = 0
zO = 0
rX = 0
rY = 0
rZ = 0
delay = .1

sleep(delay)
xO = -(imu.acceleration[0])
yO = -(imu.acceleration[1])
zO = -(imu.acceleration[2])
print (xO, yO, zO)
sleep(delay)

while True:
    x += round(imu.acceleration[0] + xO ,1)*delay
    y += round(imu.acceleration[1] + yO ,1)*delay
    z += round(imu.acceleration[2] + zO ,1)*delay
    print(f"X: {x} Y: {y} Z: {z}")
    sleep(delay)
