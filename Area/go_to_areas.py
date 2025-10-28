from go_forward_new import go_forward
from stop import stop
from turn_left import turn_left
from turn_right import turn_right
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from machine import Pin, PWM
from utime import sleep
from left_line_sensor import left_sensor
from go_forward_continuous import go_forward_continuous
from right_line_sensor import right_sensor

def go_area1_v2:
    while left_sensor() == 0 and right_sensor() == 0:
        go_forward(0.01)
        turn_left(1)
        turn_left(1)

def go_area2_v2:
    for i in range(8):
        go_forward(0.01)
    turn_left(1)
    go_forward(0.01)
    #At Lower junction
    turn_left(1)
    go_forward(1)
    #At Upper junction
    turn_left(1)
    go_forward(0.01)
    turn_left(1)
    while left_sensor() == 0 and right_sensor() == 0:
        go_forward(0.01)
    turn_left(1)
    turn_left(1)
    
def go_area3_v2:
    for i in range(8):
        go_forward(0.01)
    turn_left(1)
    go_forward(0.01)
    #At Lower Junction
    turn_left(1)
    go_forward(0.01)
    #at upper junction
    turn_right(1)
    go_forward(0.01)
    turn_right(1)
    while left_sensor() == 0 and right_sensor() == 0:
        go_forward(0.01)
    turn_left(1)
    turn_left(1)
    
def go_area4_v2:
    for i in range(8):
        go_forward(0.01)
    turn_left(1)
    go_forward(0.01)
    go_forward(0.01)
    turn_left(1)
    go_forward(0.01)
    
    
