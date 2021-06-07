import socket
import binascii
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 33033))
count = 0
temps = []
while True:

    data, addr = s.recvfrom(1500)
    count+=1
    temps.append(float(data))
    
    if (count ==10):
        print("mean temperature for 10 times")
        print(np.mean(temps))
        count =0
        temps = []