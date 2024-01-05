# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1
import board
import wifi
import socketpool
import digitalio
from time import sleep
from adafruit_httpserver import Server, Request, REQUEST_HANDLED_RESPONSE_SENT, FileResponse

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
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
server = Server(pool, "/files", debug=True)


@server.route("/")
def base(request: Request):
    
    #Serve a default static plain text message.
    return Response(request, "Instructions")


server.start(str(wifi.radio.ipv4_address))

while True:
    try:
        pool_result = server.poll()

        if pool_result == REQUEST_HANDLED_RESPONSE_SENT:
            print("Response Recieved!")
            led.value = True
            sleep(3)
            led.value = False
            pass

    except OSError as error:
        print(error)
        continue
    sleep(1)





# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html#id1