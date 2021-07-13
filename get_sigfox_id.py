from network import Sigfox
import binascii
import json

data = {}
data['sigfox'] = []



# initalise Sigfox for RCZ1 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# print Sigfox Device ID
print(binascii.hexlify(sigfox.id()))

# print Sigfox PAC number
print(binascii.hexlify(sigfox.pac()))

data['sigfox'].append({
    'Sigfox_Device_ID': binascii.hexlify(sigfox.id()),
    'Sigfox_PAC_number': binascii.hexlify(sigfox.pac())
})


with open('sigfox_config.txt', 'w') as outfile:
    json.dump(data, outfile)
