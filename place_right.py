#creating the block placement procedure right side
from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left #Turns left by 90 deg
from turn_right.py import turn_right #Turns right by 90 deg
from go_forward.py import go_forward #Increments forward
from drop_crate.py import drop_crate #Moves forward, drops crate, returns back
from right_line_sensor.py import right_sensor #Check lines to the right


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


def place_right(index):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    turn_left(2)# rotates 180 deg
    go_forward(0.1) # get off checkpoint part
    counter = 0
    while counter < index:
        go_forward(0.1)
        right_sense = right_sensor() #count lines to find correct bay
        if right_sense == 1:
            counter += 1
    
    turn_right(1) #turn into bay
    drop_crate()
    
    motor3.off() #turns motor 3 off
    motor4.off() #turns motor 4 off

