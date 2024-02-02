# type: ignore
import board
import busio
import digitalio
import pwmio
from ulab import numpy as np
from digitalio import DigitalInOut, Direction, Pull
import adafruit_mpu6050 # Gyro
import adafruit_mpl3115a2 # Altimeter
import adafruit_gps # GPS
from adafruit_motor import servo
from time import sleep, monotonic
from simple_pid import PID

# SENSORS
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) # Altimeter
#sensor.sealevel_pressure = 1070

ground = 0
for i in range(25):
    ground += sensor.altitude
    sleep(.01)
ground = (ground/25)
print(f"ground: {ground}")

win_size = 6 # window is smaller because altitude polls slowly
enum = 0
window = np.zeros(win_size) # Creates average array starting at ground

while True:
    alt = sensor.altitude-ground # Calculates altitude relative to ground

    if enum > win_size -1: # Stops array from overflowing
        enum = 0
    window[enum] = alt
    enum += 1
    
    final_alt = round(sum(window) / win_size,1)
    print(final_alt)

    sleep(.01) # Altitude can only be polled every ~.5 seconds
    # Use weighted average because reaction is slow