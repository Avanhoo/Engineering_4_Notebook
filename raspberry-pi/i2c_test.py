# type: ignore
import board 
from time import sleep
import busio

sda_pin = board.GP16
scl_pin = board.GP17
#i2c = busio.I2C(scl_pin, sda_pin) # use for debuggin i2c issues
addr = None

while addr == None: # Connects over I2C
    try:
        i2c = busio.I2C(scl_pin, sda_pin)
        addr = i2c.scan()
    except:
        print("failed, trying again...")
    sleep(.5)
print(f"Successfully paired to {addr}")

# Master
aileron = 9 # Placeholder for real values
elevator = -1

def send_commands(aileron, elevator):
    sendBuffer = bytes(f"{aileron},{elevator}", 'utf-8')
    i2c.writeto(addr, sendBuffer)

# Sub
def recieve_commands():
    recieveBuffer = None
    i2c.readfrom_into(addr, recieveBuffer) # Reads from I2C
    recieve = recieveBuffer.decode('ascii') # Turns bytes into string
    arr = [int(val) for val in recieve.split(",")] # Turns string into array
    aileron = arr[0] # Separates array into variables
    elevator = arr[1]
    return aileron, elevator

mode = 1 # Only necesarry for test file
while mode == 0:
    aileron = -89
    elevator = 37
    send_commands(aileron, elevator)
    print("Sent data")
    sleep(.5)
while mode == 1:
    recieve_commands()
    print(f"Recieved \nAileron: {aileron}\nElevator: {elevator}")
    sleep(.5)