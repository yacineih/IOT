import time




I2C_ADDRESS_BME280 = 0x77


class Device:
    """Class for communicating with an I2C device.

    Allows reading and writing 8-bit, 16-bit, and byte array values to
    registers on the device."""

    def __init__(self, address, i2c):
        """Create an instance of the I2C device at the specified address using
        the specified I2C interface object."""
        self._address = address
        self._i2c = i2c
    def write8(self, register, value):
        """Write an 8-bit value to the specified register."""
        value = value & 0xFF
        self._i2c.writeto_mem(self._address, register, value.to_bytes(1, 'little'))
    def readU8(self, register):
        """Read an unsigned byte from the specified register."""
        return int.from_bytes(
            self._i2c.readfrom_mem(self._address, register, 1), 'little') & 0xFF

class BME280:
    def __init__(self, mode = 1,address = I2C_ADDRESS_BME280,i2c = None):
        self._mode = mode
        print(mode)
        self._device = Device(address, i2c)
        print(i2c)
        print("ok")
        # Load calibration values.
        #self._load_calibration()
        self._device.write8(0xF4, 0x3F)
        print("ok")
        self.t_fine = 0

    def read_raw_humidity(self):
        """Assumes that the temperature has already been read """
        """i.e. that enough delay has been provided"""
        msb = self._device.readU8(0xFD)
        lsb = self._device.readU8(0xFD + 1)
        raw = (msb << 8) | lsb
        return raw


if __name__ == "__main__":
    from machine import I2C
    import time

    i2c = I2C(0, I2C.MASTER, baudrate=400000)
    print (i2c.scan())
    print ("all ok")

    bme = BME280(i2c=i2c)
    print("not ok")
    ob = 0

    while True:
        a = bme.read_raw_humidity()

        print ("humidity", a )

        time.sleep(5)
