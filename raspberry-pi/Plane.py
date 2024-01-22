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
gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False) # GPS
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0") # Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK220,1000") # Sets update to every 1 second

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

def getdata(): # Can be called on to refresh the information about the airplane's position and orientation
    global pitch
    global roll
    global heading
    global speed
    global drop
    pitch = None # might need to switch these around
    roll = None
    heading = None
    drop = None
    print(f"Alt: {sensor.altitude}")

def store():
    datalog.write(f"{monotonic()},{imu.acceleration[0]},{imu.acceleration[1]},{imu.acceleration[2]}\n") # Writes the time, x, y, z acceleration to a file
    datalog.flush()

    sled.value = True # Flashes onboard LED
    sleep(delay/2)
    sled.value = False
    sleep(delay/2)
#with open("/data.csv", "a") as datalog: # Opens the data 

def Roll(angle):
    scalar = 1 # allows for scaling or reversing
    lAiler.angle = angle*scalar
    rAiler.angle = angle*scalar*-1

timer = 0
while timer >= 0: # Wing coupling loop
    timer = monotonic()
    while not button.value:
        if (monotonic() > timer+1): # ADD "and coupling = engaged"
            timer = -1 # Breaks out of the big loop
            print("done")
            pairing = True
            break
        elif button.value:
            # Toggle coupling system
            print("toggle")
            break


while pairing: # Pairing loop
    tandem = True
    break
'''
while tandem:
    # recieve commands
    if not button.value: # if SPLIT SIGNAL RECIEVED
        # physical decouple
        # motor off
        tandem = False
    else:
        # execute commands'''

auto = True
pidD.tunings = (.5, 0.1, 0.075) # Drop tuning
pidD.setpoint = -.5
pidR.tunings = (.25, 0.1, 0.05) # Roll tuning
pidR.setpoint = -15
prevMove = (0, 0)
while auto:
    getdata()
    Roll(pidR(roll))
    # maintain bank angle to left (PID)
    while auto and (sensor.altitude <= 5): # in meters
        getdata()
        # straighten out and maintain drop (PID)
        while sensor.altitude <= 1:
            getdata()
            # flair nose up (PID)
            if prevmove == (imu.acceleration[0], imu.acceleration[1]):
                auto = False
            else:
                prevMove = (imu.acceleration[0], imu.acceleration[1])

# end


# To-do:
# add global data collection on set interval
# research glide PID:               
#     https://simple-pid.readthedocs.io/en/latest/user_guide.html            https://pidexplained.com/how-to-tune-a-pid-controller/
# UART
# Make program to tune PID, just drop, then roll later on