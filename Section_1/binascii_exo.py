import binascii

val = b"\x01\x0234"
ser = binascii.hexlify (val)

print(len(b"\x01"))
print(len(b"\x0234"))
print (val, ser)
print(len(val))
print(len(ser))

# Two characters are needed to represent a byte(octet)Ò