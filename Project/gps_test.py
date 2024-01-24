# type: ignore
import board
import busio
import digitalio
import pwmio
from math import acos, asin, degrees
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050 # Gyro
import adafruit_mpl3115a2 # Altimeter
import adafruit_gps # GPS
from adafruit_motor import servo
from time import sleep, monotonic
from simple_pid import PID

sda_pin = board.GP16
scl_pin = board.GP17
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=10)


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
gps = adafruit_gps.GPS(uart, debug=False)  # GPS
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0") # Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK220,1000") # Sets update to every 1 second



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



while True:
    gps.update()
    if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print(f"Waiting for fix... {gps.satellites} satellites")
            continue

    print(f"Latitude: {gps.latitude} degrees")
    print(f"Longitude: {gps.longitude} degrees")


    print (f"x: {imuval}")
    sleep(.5)