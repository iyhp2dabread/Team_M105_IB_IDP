#line sensor detection for robot
from machine import Pin
from utime import sleep

#Set the line_sensor pin for right
sensor_pin = 11 # Pin 11 = GP11 (labelled 15 on the jumper)
sensor_left = Pin(sensor_pin, Pin.IN, Pin.PULL_DOWN)

#Continiously update the sensor value and print said value
def right_sensor():
    print("Sequence Right Active")
    while True:
      sleep(0.1)
      print(sensor_right.value())
      return sensor_right.value()

if __name__ == "__main__":
    right_sensor()
