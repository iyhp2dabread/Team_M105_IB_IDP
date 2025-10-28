from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left #Turns left by 90 deg
from turn_right import turn_right #Turns right by 90 deg
from go_forward import go_forward #Increments forward
from qr_code_scanner import scan_qr #scans the qr codes
from crate_extraction import extract_crate #extracts crate if it exists
from amber_led import amber_led #flashes the amber led
from drop_crate import drop_crate 
#from pickup_crate_sequence.py import pickup_crate
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor


#facing west
def lj_to_be():
    go_forward(0.01)
    turn_left(1)
    for i in range(8):
        go_forward(0.01)
    turn_left(1)
