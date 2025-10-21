#backing up from the wall
from machine import Pin, PWM
from utime import sleep

from turn_left.py import turn_left #Turns left by 90 deg
from turn_right.py import turn_right #Turns right by 90 deg
from left_line_sensor.py import left_sensor #Check lines to the left
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

    def Reverse(self, speed=40):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))


def backing_up():
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    left_sense = left_sensor()
    right_sense = right_sensor()
    
    while left_sense != 1 and right_sense != 1:
        motor3.Reverse() #reverses out of rack
        motor4.Reverse() #reverses out of rack
        left_sense = left_sensor()
        right_sense = right_sensor()
    motor3.off() #turns off motor3
    motor4.off() #turns off motor4
