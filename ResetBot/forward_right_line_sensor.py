#line sensor detection for robot
from machine import Pin
from utime import sleep

#Set the line_sensor pin for forward right
sensor_pin = 20 # Pin 21 = GP21 (labelled 27 on the jumper)
sensor_forward_right = Pin(sensor_pin, Pin.IN, Pin.PULL_DOWN)

#Continiously update the sensor value and print said value
def forward_right_sensor():
    #print("Sequence Forward Right Active")
    while True:
      sleep(0.01)
      print(sensor_forward_right.value())
      return sensor_forward_right.value()

if __name__ == "__main__":
    forward_right_sensor()
