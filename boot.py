# boot.py -- run on boot-up
import network
import time
from wifi_config import wifi
from network import WLAN

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)



print("configured wifi")

configured_wifi_ssid = list(wifi.keys())
print(configured_wifi_ssid)
# Let's scan for available networks

print("Scanning for known wifi nets")
available_networks = wlan.scan()
available_networks_ssid = [ i.ssid for i in available_networks]

print("available networks ssid : ")

print (available_networks_ssid)

network_to_use = [ssid for ssid in available_networks_ssid if ssid == configured_wifi_ssid[0] ]

print("network to use : ")
print(network_to_use)

print("try to connect to wifi : ")

pwd = wifi[network_to_use[0]]['pwd']
=
wlan.connect(ssid=network_to_use[0], auth=(WLAN.WPA2, pwd))
while not wlan.isconnected():
    print("not connected")
    machine.idle() # save power while waiting
    time.sleep_ms(5)
print("Connected to "+network_to_use[0]+" with IP address: " + wlan.ifconfig()[0])
print(wlan.ifconfig())

##192.168.1.57
