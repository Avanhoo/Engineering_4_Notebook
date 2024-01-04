# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1
import board
import wifi
import socketpool
from time import sleep
from adafruit_httpserver import Server, Request, Response

ssid="avanhooPi"
passwd="piinthesky"
print(f"Connecting to {ssid}")
while True: # Waits for connection before proceeding
    try:
        wifi.radio.connect(ssid, passwd)
    except:
        print("trying...")
    
    if wifi.radio.connected == True:
        print(f"Connected to {ssid}")
        print(wifi.radio.ipv4_address)
        break
    sleep(1)


pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)


@server.route("/")
def base(request: Request):
    
    #Serve a default static plain text message.
    return Response(request, "Instructions")


server.serve_forever(str(wifi.radio.ipv4_address))
# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1