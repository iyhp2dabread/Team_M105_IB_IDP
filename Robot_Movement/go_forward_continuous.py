#Goes forward, using motors.
from machine import Pin, PWM
from utime import sleep
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from turn_left import turn_left
from turn_right import turn_right
from stop import stop
from emergency_stop import emergency_stop
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=50):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=30):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))


def go_forward_continuous(t):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    print("Go forward continuous active")

    #Give a little push off the line
    motor3.Forward()
    motor4.Forward()
    sleep(0.5)
    while True:
        
        #Emergency stop
        if emergency_stop(60) == 1:
            stop()
            break
        
        #Robot lost the line
        if forward_left_sensor() == 0 and forward_right_sensor() == 0:
            stop()
            break
        
        if left_sensor() == 1 or right_sensor() == 1:
            print("Junction/Turn reached, stopping")
            break
        
        #Small corrections to stay on line
        elif forward_left_sensor() == 1 and forward_right_sensor() == 0:
            motor3.off()
            motor4.Forward()
        elif forward_left_sensor() == 0 and forward_right_sensor() == 1:
            motor4.off()
            motor3.Forward()
            
        #Fully on line
        else:
            motor3.Forward()
            motor4.Forward()
        sleep(t)
    


