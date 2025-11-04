#Turns Left, using motors.
from machine import Pin, PWM
from utime import sleep
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from go_forward_continuous import go_forward
from stop import stop

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


def turn_left():
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    fr = forward_right_sensor()
    motor3.Reverse()
    motor4.Forward()
    sleep(1.1)
    stop()    
    
    
    motor3.off() #Stops Motor 3
    motor4.off() #Stops Motor 4

if __name__ == "__main__":
    turn_left()
