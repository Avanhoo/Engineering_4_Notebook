# type: ignore
import board
from digitalio import Direction, DigitalInOut, Pull
from time import sleep
import pwmio
from adafruit_motor import servo

Rled = DigitalInOut(board.GP2) # Fourth pin down, top left
Rled.direction = Direction.OUTPUT
Gled = DigitalInOut(board.GP0) # First pin, top left
Gled.direction = Direction.OUTPUT
button = DigitalInOut(board.GP28) # 7th pin down, right side
button.direction = Direction.INPUT
button.pull = Pull.UP
servo_pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(servo_pwm, min_pulse=500, max_pulse=2500)


launch = False
print("System Active")


while True:
    

    while button.value:
        sleep(.1)
    servo.angle = 0 # Resets system
    Gled.value = False
    
    for i in range (10,0,-1): #start, stop, step; nice and clean
        print("t: -" + str(i))
        Rled.value = True # Flash red
        sleep(.2)
        Rled.value = False
        sleep(.8)
        if not button.value: # Exits for loop and restarts program
            print("ABORT")
            Rled.value = True
            sleep(1)
            for o in range (5): # Overcomplicated code to make the light flash on abort
                Rled.value = True
                sleep(.03)
                Rled.value = False
                sleep(.03)
            break # Exits the countdown for loop
        if i == 1: # Makes sure it only launches if the countdown is finished
            launch = True

    if launch: # Same as above
        launch = False
        print("Liftoff")
        for i in range (0,180,1): # Sweeps the servo from 0 to 180
            servo.angle = (i)
            sleep((1/60))
        Gled.value = True
        sleep(3)
    sleep(.5)
