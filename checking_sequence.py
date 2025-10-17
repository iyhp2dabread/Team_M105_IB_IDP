from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left #Turns left by 90 deg
from turn_right.py import turn_right #Turns right by 90 deg
from go_forward.py import go_forward #Increments forward
from qr_code_scanner.py import scan_qr #scans the qr codes
from crate_extraction.py import extract_crate #extracts crate if it exists
from amber_led.py import amber_led #flashes the amber led


class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=60):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=60):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))


def left_checking():
    counter = 0 # for checking each crate slot
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    amber_led()
    turn_left()
    turn_left() # rotates 180 deg
    while counter < 6:
        while line_sensor_left == 0: #moves until aligned with a slot
            go_forward()
        turn_left() #turns into slots
        scan_qr = scan_qr() #scans the qr code attempt
        if scan_qr[0] == 1: #first element states whether the qr code exist
            print("Crate is found!")
            amber_led()
            counter = 7
            extract_crate() #crate extraction sequence
            break
        else:
            turn_right()
            counter += 1 #slot is checked
            go_forward()
    
    motor3.off() #turns motor 3 off
    motor4.off() #turns motor 4 off
            
def right_checking():
    counter = 0 # for checking each crate slot
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    amber_led()
    turn_left()
    turn_left() # rotates 180 deg
    while counter < 6:
        while line_sensor_left == 0: #moves until aligned with a slot
            go_forward()
        turn_right() #turns into slots
        if scan_qr[0] == 1: #first element states whether the qr code exist
            print("Crate is found!")
            amber_led()
            counter = 7
            extract_crate() #crate extraction sequence
            break
        else:
            turn_left()
            counter += 1 #slot is checked
            go_forward()
    
    motor3.off() #turns motor 3 off
    motor4.off() #turns motor 3 off

if __name__ == "__main__":
    if area_counter == 0 or area_counter == 2:
        left_checking()
    if area_counter == 1 or area_counter == 3:
        right_checking()
