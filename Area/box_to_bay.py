#box to bay exit
from stop import stop
from turn_left import turn_left
from turn_right import turn_right
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from machine import Pin, PWM
from utime import sleep
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
from go_forward_continuous import go_forward_continuous

print("Welcome to main.py!")

def box_to_bay():
    #assuming we are on the start box right side facing east
    turn_left(1.1)
    go_forward_continous(0.01)
    turn_left(1.1)
    go_forward_continous(0.01)
    turn_right(1.1)
    go_forward_continous(0.01)
    #we are now out of the box and on the bay line
    
    turn_left(1)
    go_forward_continous(0.01)
    go_forward_continous(0.01)
    #Now at bay entrance
    
    turn_right(2.2)
    #should be facing east
    


