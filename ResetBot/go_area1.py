from machine import Pin, PWM
from utime import sleep

from go_forward_continuous import go_forward
from turn_left import turn_left
from turn_right import turn_right
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor

def go_to_area1():
    left_sense = left_sensor()
    right_sense = right_sensor()
    while left_sense != 1 and right_sense != 1:
        go_forward(0.01)
        left_sense = left_sensor()
        right_sense = right_sensor()

go_to_area1()
    
