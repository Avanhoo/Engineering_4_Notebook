# type: ignore
import board
import busio
import digitalio
import numpy as np
import pwmio
from math import acos, asin, degrees
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050 # Gyro
import adafruit_mpl3115a2 # Altimeter
from adafruit_motor import servo
from time import sleep, monotonic
from simple_pid import PID

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

# LIGHTS
sled = digitalio.DigitalInOut(board.LED) # Maybe capitalize LED?
sled.direction = digitalio.Direction.OUTPUT

# BUTTON
button = DigitalInOut(board.GP15)
button.direction = Direction.INPUT
button.pull = Pull.UP

# SERVOS
pwm1 = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP7, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.GP8, duty_cycle=2 ** 15, frequency=50)
elevator = servo.Servo(pwm1)
lAiler = servo.Servo(pwm2) # Left Aileron
rAiler = servo.Servo(pwm3) # Right Aileron

# SENSORS
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) # Altimeter
#sensor.sealevel_pressure = 1070

# PID & VARIABLES
pairing = False
tandem = False
pidD = PID(.5, 0.1, 0.075, setpoint=-.5) # drop pid
pidD.time_fn = monotonic
pidD.sample_time = 0.01

pidR = PID(.25, 0.1, 0.05, setpoint=-15) # roll pid
pidR.time_fn = monotonic
pidR.sample_time = 0.01
prevMove = (0,0)

calib = 0
calib2 = 0
for i in range (150): # Finds baseline for sensors, DO NOT MOVE PICO while calibrating
    calib += imu.acceleration[0]
    calib2 += imu.acceleration[2]
    sleep(.01)
calib = -(calib/150)
calib2 = -(calib/150)
print(calib2)


while True:
    imuval = (imu.acceleration[0]+calib)/9.8 # Calculates angle in rads
    if imuval > 1: # stops it from breaking the trig
        imuval = 1
    elif imuval < -1:
        imuval = -1

    if imu.acceleration[2] <(-1.5 + calib2): # Checks if plane is flipped
        imuval = 180-(round(degrees(asin(imuval))))
    else:
        imuval = (round(degrees(asin(imuval))))


    window_size = 5
    arr_count = 0
    arr.append(imuval)
    mean = np.convolve(imuval, np.ones(N)/N, mode='valid')
    N+=1
    print(mean)
        # USE NP