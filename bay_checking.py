from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left #Turns left by 90 deg
from turn_right import turn_right #Turns right by 90 deg
from go_forward import go_forward #Increments forward
from crate_extraction import extract_crate #extracts crate if it exists
from amber_led import amber_led #flashes the amber led
from drop_crate import drop_crate 
#from pickup_crate_sequence.py import pickup_crate
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
from qr_code_scan import scan_qr


#Starting from Bay Entrance Pointing East
def bay_check(unchecked_bays):
    for i in range(1, len(unchecked_bays)):
        if unchecked_bays[i] !=0:
            if i == 3:
                go_forward(1)
                continue
            turn_right(1)
            go_forward(1)
            scan_qr_crate = scan_qr()
            if scan_qr_crate == True:
                print("Crate is found")
                amber_led()
                #pickup_crate()
                turn_left(1)
                turn_left(1)
                go_forward(1)
                turn_right(1)
                while left_sensor() == 0 and right_sensor() == 0:
                    go_forward(1)
                turn_left(1)
            else:
                turn_left(1)
                turn_left(1)
                go_forward(1)
                turn_right(1)
                go_forward(1)
        else:
            go_forward(1)
        
    turn_left(1)

#Finishes at bay Exit facing north

if __name__ == "__main__":
    unchecked_bays = [1, 1, 1, 1]
    bay_check()
    
    
    
