#creating the block placement procedure right side
from machine import Pin, PWM
from utime import sleep

from turn_left import turn_left #Turns left by 90 deg
from turn_right import turn_right #Turns right by 90 deg
from go_forward_continous import go_forward_continous #Increments forward
from drop_crate import drop_crate #Moves forward, drops crate, returns back
from right_line_sensor import right_sensor #Check lines to the right
from distance_sensor import distance_sensor #Reads distance from wall in front

#code for motor
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

#code for linear acuator
class Actuator:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
           
    def set(self, dir, speed):
        self.mDir.value(dir)                     # down = 0 up = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

#actual algorithm
def pickup_box():
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    actuator1 = Actuator(dirPin=0, PWMPin=1)
    #get acuator to the highest position
    actuator1.set(dir = 1, speed = 50)
    sleep(5)
    actuator1.set(dir = 0, speed = 50)
    sleep(4.5)
    actuator1.set(dir=0, speed = 0)
    
    #move forward till we get to the box
    while distance_sensor() > 30:
        go_forward_continous(0.01)
    
    motor3.off() #turns motor 3 off
    motor4.off() #turns motor 4 off
    
    #actually picking up the box
    actautor1.set(dir = 1, speed = 50)
    sleep(5)
    actuator1.set(dir = 1,speed = 0)
