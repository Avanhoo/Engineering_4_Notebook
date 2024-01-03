import board
import busio
import adafruit_mpu6050
from time import sleep

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)

d = .1
p = 180/3.14159
x=0
y=0
z=0

for i in range (1,5):
    x+=round(imu.gyro[0])
    y+=round(imu.gyro[1])
    z+=round(imu.gyro[2])
    sleep(.1)
xO=round(x/5,1)
yO=round(y/5,1)
zO=round(x/5,1)
print(xO)

while True:
    print(f"X: {round(imu.gyro[0],2)+.06} \nY: {round(imu.gyro[1]+.015,2)} \nZ: {round(imu.gyro[2],2)}")
    x+=round((imu.gyro[0]-xO)*d*p,1)
    y+=round((imu.gyro[1]-yO)*d*p,1)
    z+=round((imu.gyro[2]-zO)*d*p,1)
    sleep(d)