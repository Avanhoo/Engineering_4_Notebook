# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1
import board
import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response

ssid="avanhooPi"
passwd="piinthesky"

print(f"Connecting to {ssid}")
while True: # Waits for connection before proceeding
    try:
        wifi.radio.connect(ssid, passwd)
    finally:
        print(f"Connected to {ssid}")
        break

