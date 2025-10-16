#line sensor detection for robot
from machine import Pin
from utime import sleep

#Set the line_sensor pin for forward left
sensor_pin = 20 # Pin 20 = GP20 (labelled 26 on the jumper)
sensor_forward_left = Pin(sensor_pin, Pin.IN, Pin.PULL_DOWN)

#Continiously update the sensor value and print said value
while True:
  sleep(0.1)
  print(sensor_forward_left.value())
  return sensor_forward_left.value()
