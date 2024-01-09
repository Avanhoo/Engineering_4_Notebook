import board
import busio
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)
print("alive")

while True:
    data = uart.read(32)

    if data is not None: # If anything is recieved
        led.value = True

        data_string = ''.join([chr(b) for b in data]) # Bytes to str
        print(data_string, end="")
        led.value = False