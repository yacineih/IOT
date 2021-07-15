import binascii
import socket
from sigfox_config import sigfox_c

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# send hello world

s.send("Hello world!")
