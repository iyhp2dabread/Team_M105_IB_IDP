from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left #Turns left by 90 deg
from turn_right.py import turn_right #Turns right by 90 deg
from go_forward.py import go_forward #Increments forward
from qr_code_scanner.py import scan_qr #scans the qr codes
from crate_extraction.py import extract_crate #extracts crate if it exists
from amber_led.py import amber_led #flashes the amber led
from drop_crate.py import drop_crate 
from qr_code_scanner.py import scan_qr #scans the qr codes
#from pickup_crate_sequence.py import pickup_crate
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor


#Starting from Bay Exit Pointing East
def bay_check(unchecked_bays):
    for i in range(1, len(unchecked_bays)):
        if unchecked_bays[i] !=0:
            if i == 3:
                go_forward(1)
                continue
            turn_right(1)
            go_forward(1)
            scan_qr = scan_qr()
            if scan_qr[0] == 1:
                print("Crate is found")
                amber_led()
                #pickup_crate()
                turn_left(1)
                turn_left(1)
                go_forward(1)
                turn_right(1)
                while left_sensor and right_sensor == 0:
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
        
                
            
    
    
    
