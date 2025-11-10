from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left #Turns left by 90 deg
from turn_right import turn_right #Turns right by 90 deg
from go_forward import go_forward #Increments forward
from qr_code_scanner import scan_qr #scans the qr codes
from crate_extraction import extract_crate #extracts crate if it exists
from amber_led import amber_led #flashes the amber led
from drop_item import drop_item


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

def exit_start_bay():
  
