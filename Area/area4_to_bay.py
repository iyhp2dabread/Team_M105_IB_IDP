from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left
from turn_right import turn_right
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
from lower_junction_to_bay_entrance import lower_junction_to_bay_entrance

def area4_to_bay():
    left_sense = left_sensor()
    right_sense = right_sensor()
    
    turn_left(1)
    while left_sense != 1 and right_sense != 1:
        go_forward(0.1)
        left_sense = left_sensor()
        right_sense = right_sensor()
    #on the checkpoint in area 4
    
    turn_left(2) # rotates 180 deg
    go_forward(0.1)
    left_sense = 0
    counter = 0
    while left_sense != 1 and counter < 6:
        go_forward(0.1)
        left_sense = left_sensor() #checking left side markers
        if left_sense == 1:
            counter += 1 #counting markers up to make sure it passes the rack
    #on spot 6
    
    go_forward(0.2)
    left_sense = 0
    while left_sense != 1:
        go_forward(0.2)
        left_sense = left_sensor()
    #on bay entrance
    turn_left(1) #facing east
