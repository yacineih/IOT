from pymodbus.client.sync import ModbusTcpClient # import modbus for Primary
import time

client = ModbusTcpClient('192.168.3.36', port=5020)
client.connect()
while True:
        result = client.read_input_registers(address=255,unit=28,count=2)
        print(result.registers[0])
        print(type(result.registers[0]))
        print(result.registers[0]<5000)
        if (result.registers[0] < 5000):
                print("water is under 5000 let's start the pump")
                client.write_register(address =512,unit =48, value=1)
                print("pump started")
        if (result.registers[0] > 9000):
                print("level of water to high lets stop the pump")
                client.write_register(address =512,unit =48, value=0)
                print("pump stopped")
        time.sleep(5)

client.close()
