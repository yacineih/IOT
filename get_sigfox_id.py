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

sigfox_c = {"Sigfox_Device_ID" : binascii.hexlify(sigfox.id()), "Sigfox_PAC_number" : binascii.hexlify(sigfox.pac())}

file = open("lopy_sigfox_config.py", "w")
str_dictionary = repr(sigfox_c)
file.write("sigfox_c = " + str_dictionary + "\n")

file.close()
