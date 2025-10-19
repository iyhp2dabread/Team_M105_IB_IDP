from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left #Turns left by 90 deg
from turn_right.py import turn_right #Turns right by 90 deg
from go_forward.py import go_forward #Increments forward
from qr_code_scanner.py import scan_qr #scans the qr codes
from crate_extraction.py import extract_crate #extracts crate if it exists
from amber_led.py import amber_led #flashes the amber led
from drop_item.py import drop_item


class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=100):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=30):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))

def bay_return(bay):     #starts assuming orientation is already pointing towards Bay_4 and is located at Bay Entrance
    if bay == 4:
        go_forward(1)  #moves forward until junction at bay
        drop_item()    #function to drop the box
        if item_counter == 1:
            go_to_bay_exit()
    if bay == 3:            #goes to bay 3 and drops box
        turn_right(1)
        go_forward(1)
        turn_left(1)
        go_forward(1)
        drop_item()
        if item_counter == 1:
            go_to_bay_exit()
    if bay == 2:          #goes to bay 2 and drops box
        turn_right(1)
        for i in range(3)
            go_forward(1)
        turn_left(1)
        go_forward(1)
        drop_item()
        if item_counter == 1:
            go_to_bay_exit()
    if bay == 1:          #goes to bay 1 and drops boxs
        turn_right(1)
        for i in range(4)
            go_forward(1)
        turn_left(1)
        go_forward(1)
        drop_item()
        if item_counter == 1:
            go_to_bay_exit()
            
def go_to_bay_exit():
    turn_right(1)
    turn_right(1)
    go_forward(1)
    turn_left(1)
    while line_sensor_right != 1:
        go_forward(1)
    turn_right(1)
    
            
        
        
    

