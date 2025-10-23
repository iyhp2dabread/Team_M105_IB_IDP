#find path
#libraries
from machine import Pin, PWM
from utime import sleep
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from turn_left import turn_left

def auto_correct():
    fl_sense = forward_left_sensor()
    fr_sense = forward_right_sensor()

    print("Auto Correct Start")

    while fl_sense != 1 and fr_sense != 1:
        turn_left(0.1)
        fl_sense = forward_left_sensor()
        fr_sense = forward_right_sensor()

    print("Auto Correct End")
