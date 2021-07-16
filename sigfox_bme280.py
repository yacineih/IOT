import BME280
from machine import I2C
import time
from network import Sigfox
from senml_micropython_library.kpn_senml import cbor_encoder as cbor
# we use cbor module to serialize the data instead of json
# sigfox max message size is 12 bytes
#
import socket

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

i2c = I2C(0, I2C.MASTER, baudrate=400000)


bme = BME280.BME280(i2c=i2c)

temperature_data = []
while True:
    print("let's get the temperature")
    actual_temperature = float(bme.read_temperature())
    print("actual_temperature : "+ str(actual_temperature))

    if len(temperature_data) == 0:
        temperature_data.append(actual_temperature)
    else :

        temperature_data.append(actual_temperature-previous_temperature)

    # send data once the lenght is equal to 12 bytes
    if (len(cbor.dumps(temperature_data))>12):
        print(temperature_data)
        print(cbor.dumps(temperature_data)
        #s.send(cbor.dumps(temperature_data[:-1]))
        temperature_data = [actual_temperature]

    previous_temperature = actual_temperature

    time.sleep(10)
