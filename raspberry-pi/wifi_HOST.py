import board
import wifi
import time
import ipaddress
import digitalio
import socketpool
from asyncio import async_sleep, run, create_task, gather
from adafruit_httpserver import Server, Request, REQUEST_HANDLED_RESPONSE_SENT, FileResponse, Websocket, GET

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
ssid="avanhooPi"
passwd="piinthesky"

wifi.radio.start_ap(ssid=ssid, password=passwd, max_connections=1)
wifi.radio.start_dhcp()
wifi.radio.start_station()
print(f"gateway: {wifi.radio.ipv4_gateway_ap}")
ip = ipaddress.ip_address("192.168.4.16")


# Websocket test
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/files", debug=True)
websocket: Websocket = None

DATA_TO_SEND = "'ello"


@server.route("/files")
def client(request: Request):
    return Response(request, DATA_TO_SEND, content_type="text/plain")

@server.route("/connect-websocket", GET)
def connect_client(request: Request):
    global websocket  # pylint: disable=global-statement

    if websocket is not None:
        websocket.close()  # Close any existing connection

    websocket = Websocket(request)

    return websocket
    
    
server.start(str(wifi.radio.ipv4_address))

async def handle_http_requests():
    while True:
        server.poll()

        await async_sleep(0)


async def handle_websocket_requests():
    while True:
        if websocket is not None:
            led.value = True
            time.sleep(3)
            led.value = False
            print("recieved")

        await async_sleep(0)


async def send_websocket_messages():
    while True:
        if websocket is not None:
            DATA = "HELLO WORLD"
            websocket.send_message(str(DATA), fail_silently=True)

        await async_sleep(1)


async def main():
    await gather(
        create_task(handle_http_requests()),
        create_task(handle_websocket_requests()),
        create_task(send_websocket_messages()),
    )


run(main())
