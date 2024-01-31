# type: ignore
import board
import busio
import digitalio
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050 # Gyro
import adafruit_mpl3115a2 # Altimeter
import adafruit_gps # GPS
from adafruit_motor import servo
from time import sleep, monotonic
from simple_pid import PID

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)

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
motPWM = pwmio.PWMOut(board.GP14) #Motor PWM
backPWM = pwmio.PWMOut(board.GP15)
motor = motor.DCMotor(positive_pwm = motPWM, negative_pwm = backPWM)
motor.decay_mode = motor.SLOW_DECAY = 1 # set to FAST_DECAY = 0 for coasting

# SENSORS
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) # Altimeter
#sensor.sealevel_pressure = 1070

# PID
pidD = PID(.5, 0.1, 0.075, setpoint=-.5) # drop pid
pidD.time_fn = monotonic
pidD.sample_time = 0.01

pidR = PID(.25, 0.1, 0.05, setpoint=0) # roll pid
pidR.time_fn = monotonic
pidR.sample_time = 0.01
prevMove = (0,0)
go = False

def Roll(angle): # ADD ANGLE UPDATE
    scalar = 1 # allows for scaling or reversing
    lAiler.angle = angle*scalar
    rAiler.angle = angle*scalar*-1

while True:
    while not button.value: # Startup
            if (monotonic() > timer+1): # ADD "and coupling = engaged"
                print("STARTING")
                go = True
                break
    while go:
        motor.throttle = 1
        Roll(pidR(roll))

        





        if (not button.value) or stop: # Immediately stop if button pressed or crash detected
        motor.throttle = 0
        go = False
        break