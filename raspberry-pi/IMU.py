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
xO = -(imu.acceleration[0],2)
yO = -(imu.acceleration[1],2)
zO = -(imu.acceleration[2],2)
print (xO, yO, zO)
sleep(delay)

while True:
    x += (imu.acceleration[0] + xO)*delay
    y += (imu.acceleration[1] + yO)*delay
    z += (imu.acceleration[2] + zO)*delay
    print(f"X: {x} Y: {y} Z: {z}")
    sleep(delay)
