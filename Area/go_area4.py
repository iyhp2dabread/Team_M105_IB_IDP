#Goes to area 4
from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left
from turn_right.py import turn_right
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor

from placement_left.py import place_left

def go_to_area4(index):
    go_forward(0.2)
    left_sense = left_sensor()
    right_sense = right_sensor()
    while left_sense != 1: #To corner
        go_forward(0.2)
        left_sense = left_sensor()

    turn_left(1)
    go_forward(0.2)
    left_sense = 0
    right_sense = 0
    while left_sense != 1 and right_sense != 1: #To area 4
        go_forward(0.1)
        left_sense = left_sensor()
        right_sense = right_sensor()
    turn_left(2)
    place_left(index)
