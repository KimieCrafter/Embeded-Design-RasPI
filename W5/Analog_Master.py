import smbus2  # type: ignore
import time

I2C_SLAVE_ADDR = 0x08  # I2C address of the slave device
bus = smbus2.SMBus(1)  # I2C bus number (1 for Raspberry Pi 2 and later)

def read_pot_value():
    try:
        data = bus.read_i2c_block_data(I2C_SLAVE _ADDR, 0, 2) # type: ignore
        value = (data[0] << 8) | data[1]
        return value
    except Exception as e:
        print("Read error:", e)
        return -1

while True:
    pot_value = read_pot_value()
    print("Potentiometer Value:", pot_value)
    time.sleep(0.5)

