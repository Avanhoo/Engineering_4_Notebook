import board
import wifi
import time
import ipaddress
import socketpool
from adafruit_httpserver import Server, Request, Response


ssid="avanhooPi"
passwd="piinthesky"

wifi.radio.start_ap(ssid=ssid, password=passwd, max_connections=1)
wifi.radio.start_dhcp()
wifi.radio.start_station()
print(f"gateway: {wifi.radio.ipv4_gateway_ap}")
ip = ipaddress.ip_address("192.168.4.16")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)


@server.route("/")
def base(request: Request):
    
    #Serve a default static plain text message.
    return Response(request, "Instructions")


server.serve_forever(str(wifi.radio.ipv4_address))
# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1