import smbus
import time
class ENV:

    def __init__(self):
        self.temp = 0
        self.humi = 0
        self.iic = smbus.SMBus(1)
        self._AHT20_ADDR = 0x38
        self.iic.write_i2c_block_data(self._AHT20_ADDR,0,[0xba]) # reset
        time.sleep(0.05)
        self.iic.write_i2c_block_data(self._AHT20_ADDR,0,[0xa8,0x00,0x00]) # normal mode
        time.sleep(0.35)
        self.iic.write_i2c_block_data(self._AHT20_ADDR,0,[0xe1,0x28,0x00]) # calibrate with cycle flag
        s = self._ahtState()

    def _ahtState(self):
        n = self.iic.read_byte(self._AHT20_ADDR)
        return n

    def update(self):
        self.iic.write_i2c_block_data(self._AHT20_ADDR,0,[0xac,0x33,0x00])
        s = self._ahtState()
        while s & 0x80:
            time.sleep(0.01)
            s = self._ahtState()
        n = self.iic.read_i2c_block_data(self._AHT20_ADDR,0,6)
        h = ((n[1] << 16) | (n[2] << 8) | (n[3])) >> 4
        self.humi = round(h*0.000095, 1)
        t = ((n[3]&0x0f)<<16|(n[4]<<8)|n[5])
        self.temp = round(t*0.000191 - 50, 1)
        return (self.temp, self.humi)