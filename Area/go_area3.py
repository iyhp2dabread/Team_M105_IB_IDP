#Goes to area 3
from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left
from turn_right.py import turn_right
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor

from placement_right.py import place_right

def go_to_area2():
    left_sense = left_sensor()
    right_sense = right_sensor()
    turn_left(1)
    while left_sense != 1 and right_sense != 1: #To upper junction
        go_forward(0.3)
        left_sense = left_sensor()
        right_sense = right_sensor()
    
    turn_right(1)
    go_forward(0.2)
    right_sense = 0
    while right_sense != 1:
        go_forward(0.2)
        right_sense = right_sensor()
    
    turn_right(1)
    go_forward(0.2)
    left_sense = 0
    right_sense = 0
    while left_sense != 1 and right_sense != 1: #To area 2
        go_forward(0.2)
        left_sense = left_sensor()
        right_sense = right_sensor()
    place_right()

