#line sensor detection for robot
from machine import Pin
from utime import sleep

#Set the line_sensor pin for forward left
sensor_pin = 11 # Pin 11 = GP11 (labelled 15 on the jumper)
sensor_forward_left = Pin(sensor_pin, Pin.IN, Pin.PULL_DOWN)

#Continiously update the sensor value and print said value
def forward_left_sensor():
    print("Sequence Forward Left Active")
    while True:
      sleep(0.1)
      print(sensor_forward_left.value())
      return sensor_forward_left.value()

if __name__ == "__main__":
    forward_left_sensor()
