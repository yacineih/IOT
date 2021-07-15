import os
import machine
from  binascii import hexlify
from wifi_config import wifi


import pycom

uart = machine.UART(0, 115200)
os.dupterm(uart)

if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN
    wl = WLAN()
    wl.mode(WLAN.STA) # Try to connect to a wifi given is wifi_conf.py
    print("mode")
    print(wl.mode())
    print("Scanning for known wifi nets")
    available_nets = wl.scan()
    print (available_nets)
    nets = frozenset([e.ssid for e in available_nets])

    known_nets_names = frozenset([key for key in wifi])
    net_to_use = list(nets & known_nets_names)
    print ("net to use", net_to_use)
    try:
        net_to_use = net_to_use[0]
        print(net_to_use)
        net_properties = wifi[net_to_use]
        print(net_properties)
        pwd = net_properties['pwd']
        print(pwd)
        sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
        print(sec)
        print("all ok")
        if 'wlan_config' in net_properties:
            wl.ifconfig(config=net_properties['wlan_config'])
        print("net_to_use")
        print(net_to_use)
        print("sec")
        print(sec)
        print("pwd")
        print(pwd)
        wl.connect(net_to_use, (sec, pwd), timeout=10000)
        while not wl.isconnected():
            machine.idle() # save power while waiting
        print("Connected to "+net_to_use+" with IP address: " + wl.ifconfig()[0])

    except Exception as e:
        ssid = "PLIDO_"+str(hexlify(wl.mac()[0][4:]))[2:6]
        wl = WLAN()
        wl.init(mode=WLAN.AP,  ssid=ssid, auth=wl.auth(), antenna=WLAN.INT_ANT)
        print("Failed to connect to any known network, going into AP mode")
        print("To connect look for '{}' access point, key = '{}'".format(ssid, wl.auth()[1] ))
        print (wl.mode())
