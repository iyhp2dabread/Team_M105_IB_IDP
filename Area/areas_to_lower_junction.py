from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left
from turn_right import turn_right
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
from lower_junction_to_bay_entrance import lower_junction_to_bay_entrance






def area1_to_lj_v2():
    left_sense = left_sensor()
    right_sense = right_sensor()
    
    turn_right(1)
    while left_sense != 1 and right_sense != 1:
        go_forward(0.01)
        left_sense = left_sensor()
        right_sense = right_sensor()
    #on the checkpoint in area 1
    
    go_forward(0.01)
    #on the top right corner
        
    turn_left(1)
    go_forward(0.01)
    #on lower junction
    
    
    
    
def area2_to_lj_v2():
    left_sense = left_sensor()
    right_sense = right_sensor()

    turn_right(1)
    right_sense = 0
    while right_sense != 1:
        go_forward(0.01)
        right_sense = right_sensor()
    #on the middle right corner
    
    turn_right(1)
    go_forward(0.01)
    #on the upper junction
        
    turn_right(1)
    go_forward(0.01)
    #on lower junction
    turn_left(1)
    
   # lower_junction_to_bay_entrance()
   
   
def area3_to_lj_v2():
    left_sense = left_sensor()
    right_sense = right_sensor()

    turn_left(1)
    left_sense = 0
    while left_sense != 1:
        go_forward(0.01)
        left_sense = left_sensor()
    #on the middle left corner
    
    turn_left(1)
    go_forward(0.01)
    #on the upper junction
        
    turn_left(1)
    go_forward(0.01)
    #on lower junction
    turn_left(1)
    
    

