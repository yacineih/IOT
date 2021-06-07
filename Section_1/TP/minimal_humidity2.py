from virtual_sensor import virtual_sensor
import time
import socket
import cbor2 as cbor


humidity    = virtual_sensor(start=30, variation = 3, min=20, max=80)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    h = humidity.read_value()

    j = [h]
    s.sendto (cbor.dumps(j), ("127.0.0.1", 33033))
    time.sleep(10)