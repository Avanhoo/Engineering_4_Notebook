import board
import wifi
import time
import ipaddress
import digitalio
import socketpool
from adafruit_httpserver import Server, Request, REQUEST_HANDLED_RESPONSE_SENT, FileResponse

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
ssid="avanhooPi"
passwd="piinthesky"

wifi.radio.start_ap(ssid=ssid, password=passwd, max_connections=1)
wifi.radio.start_dhcp()
wifi.radio.start_station()
print(f"gateway: {wifi.radio.ipv4_gateway_ap}")
ip = ipaddress.ip_address("192.168.4.16")

while True:
    time.sleep(1)
    print("running...")
    request.Request
    print(wifi.radio.ping(wifi.radio.ipv4_gateway_ap))
    Request.request.client_address  # ('192.168.137.1', 40684)
