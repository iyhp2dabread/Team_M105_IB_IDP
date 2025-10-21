from machine import Pin, PWM
from utime import sleep

from left_line_sensor import left_sensor
from right_line_sensor import right_sensor

from placement_right.py import place_right

def go_to_area1():
    left_sense = left_sensor()
    right_sense = right_sensor()
    while left_sense != 1 and right_sense != 1:
        go_forward(0.1)
        left_sense = left_sensor()
        right_sense = right_sensor()
    place_right()
    
