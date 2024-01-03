import board
import wifi
import time
import ipaddress

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
    print(wifi.radio.ping(ip))

'''
print("joining network...")
print(wifi.radio.connect(ssid=ssid,password=passwd))
# the above gives "ConnectionError: Unknown failure" if ssid/passwd is wrong

print("my IP addr:", wifi.radio.ipv4_address)

print("pinging 1.1.1.1...")
ip1 = ipaddress.ip_address("1.1.1.1")
print("ip1:",ip1)
print("ping:", wifi.radio.ping(ip1))'''