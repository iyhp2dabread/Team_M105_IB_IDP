
#Goes forward, using motors.
from machine import Pin, PWM
from utime import sleep
from refind_line import refind_line

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


def go_forward():   
    print("Go forward")
    while new_detection = False:
        if line_sensor_left == 1 or line_sensor_right == 1:  #If a junction/corner is reached, stop moving forward
            new_detection = True
            motor3.off()
            motor4.off()
            break
        else:
            while line_sensor_front_left == 1: and line_sensor_front_right == 1:
                motor3.Forward()
                motor4.Forward()
                sleep(1)
            if line_sensor_front_left == 0 and line_sensor_front_right == 1:
                motor3.off()
                motor4.Forward() # Puts power through right motor only to make small correction
            if line_sensor_front_left == 1 and line_sensor_front_right == 0:
                motor4.off()
                motor3.Forward() # Puts power through left motor only to make small correction
            else:
                motor3.off()
                motor4.off()
                refind_line()     # Robot has come of line completely and must refind it 
            
def go_forward(t):
    print("Go forward")
    while new_detection = False:
        if line_sensor_left == 1 or line_sensor_right == 1:  #If a junction/corner is reached, stop moving forward
            new_detection = True
            motor3.off()
            motor4.off()
            break
        else:
            while line_sensor_front_left == 1: and line_sensor_front_right == 1:
                motor3.Forward()
                motor4.Forward()
                sleep(t)
                motor3.off()
                motor4.off()
            if line_sensor_front_left == 0 and line_sensor_front_right == 1:
                motor3.off()
                motor4.Forward()
                sleep(t)# Puts power through right motor only to make small correction
                motor4.off()
            if line_sensor_front_left == 1 and line_sensor_front_right == 0:
                motor4.off()
                motor3.Forward() # Puts power through left motor only to make small correction
                sleep(t)
                motor3.off()
            else:
                motor3.off()
                motor4.off()
                refind_line()     # Robot has come of line completely and must refind it 

if __name__ == "__main__":
    go_forward(1)
        



