# type: ignore
import board
import busio
import digitalio
import pwmio
from adafruit_motor import motor
from digitalio import DigitalInOut, Direction, Pull
from time import sleep, monotonic

motPWM = pwmio.PWMOut(board.GP14)
backPWM = pwmio.PWMOut(board.GP15)
motor = motor.DCMotor(positive_pwm = motPWM, negative_pwm = backPWM)
motor.decay_mode = motor.SLOW_DECAY = 1
max = .5

while True:
    val = input("Motor speed: ") # 0-1
    motor.throttle = float(val)