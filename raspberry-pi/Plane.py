# type: ignore
import board
import busio
import digitalio
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050
import servo
import wifi
from time import sleep, monotonic
from simple_pid import PID

sda_pin = board.GP16
scl_pin = board.GP17
#i2c = busio.I2C(scl_pin, sda_pin)
#imu = adafruit_mpu6050.MPU6050(i2c)

# LIGHTS
sled = digitalio.DigitalInOut(board.led) # Maybe capitalize LED?
sled.direction = digitalio.Direction.OUTPUT

# BUTTON
button = DigitalInOut(board.GP28) # 7th pin down, right side
button.direction = Direction.INPUT
button.pull = Pull.UP

# SERVOS
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
elevator = servo.Servo(pwm)
lAiler = servo.Servo(pwm) # Left Aileron
rAiler = servo.Servo(pwm) # Right Aileron

# PID & VARIABLES
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
    pitch =  # might need to switch these around
    roll = 
    heading = 
    drop = 

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

pairing = True
while pairing: # Pairing loop
    try:
        wifi.radio.connect("test", "testtesttest")
    except:
        sleep(.5)
    finally:
        print("connected")
        pairing = False
        break

tandem = True
while tandem:
    # recieve commands
    # execute commands
    if split signal recieved:
        # physical decouple
        # motor off
        tandem = False

auto = True
pidD.tunings = (.5, 0.1, 0.075) # Drop tuning
pidD.setpoint = -.5
pidR.tunings = (.25, 0.1, 0.05) # Roll tuning
pidR.setpoint = -15
while auto:
    getdata()
    # maintain bank angle to left (PID)
    while auto and (altitude <= 5): # in meters
        getdata()
        # straighten out and maintain drop (PID)
        while altitude <= 1:
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
# insert wifi data command code
# Make program to tund PID, just drop, then roll later on