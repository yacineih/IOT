import socket
import binascii
import cbor2 as cbor
import beebotte
import config_bbt #secret keys
import datetime
import time
import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 33033))

bbt = beebotte.BBT(config_bbt.API_KEY, config_bbt.SECRET_KEY)

def to_bbt(channel, res_name, cbor_msg, factor=1, period=10, epoch=None):
    global bbt

    prev_value = 0
    data_list = []
    if epoch:
        back_time = epoch
    else:
        back_time = time.mktime(datetime.datetime.now().timetuple())

    back_time -= len(cbor_msg)*period

    for e in cbor_msg:
        prev_value += e

        back_time += period

        data_list.append({"resource": res_name,
                          "data" : prev_value*factor,
                          "ts": back_time*1000} )

    pprint.pprint (data_list)

    bbt.writeBulk(channel, data_list)


while True:
    data, addr = s.recvfrom(1500)
    print(data)
    j = cbor.loads(data)
    print(j)
    to_bbt("capteurs", "temperature", j, factor=0.01)
    to_bbt("capteurs", "humidity", j, factor=0.01)
    to_bbt("capteurs", "pressure", j, factor=0.01)