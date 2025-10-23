from machine import Pin, I2C
from libs.VL53L0X.VL53L0X import VL53L0X
from utime import sleep

def distance_sensor():
     # config I2C Bus
    i2c_bus = I2C(id=0, sda=Pin(8), scl=Pin(9)) # I2C0 on GP8 & GP9
    # print(i2c_bus.scan())  # Get the address (nb 41=0x29, 82=0x52)
    
    # Setup vl53l0 object
    vl53l0 = VL53L0X(i2c_bus)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[0], 18)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[1], 14)

    # Start device
    vl53l0.start()
    distance = vl53l0.read()
    print("Distance = {distance}mm")
    vl53.l0.stop()
    return distance 

