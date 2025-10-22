#line sensor detection for robot
from machine import Pin
from utime import sleep

#Set the line_sensor pin for left
sensor_pin = 10 # Pin 10 = GP10 (labelled 14 on the jumper)
sensor_left = Pin(sensor_pin, Pin.IN, Pin.PULL_DOWN)

#Continiously update the sensor value and print said value
def left_sensor():
    print("Sequence Left Active")
    while True:
      sleep(0.1)
      return sensor_left.value()

if __name__ == "__main__":
    left_sensor()
