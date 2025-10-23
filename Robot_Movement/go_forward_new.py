#Goes forward, using motors.
from machine import Pin, PWM
from utime import sleep
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from turn_left import turn_left
from turn_right import turn_right
from auto_correct import auto_correct

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


def go_forward(t):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    for_left_sense = forward_left_sensor()
    for_right_sense = forward_right_sensor()
    if for_left_sense == 0 and for_right_sense == 0:
        auto_correct()
        motor3.off()
        motor4.off()
        #correction here
    else:
        if for_left_sense == 1 and for_right_sense == 0:
            print("Correcting to the left")
            turn_left(0.1)
        if for_left_sense == 0 and for_right_sense == 1:
            print("Correcting to the right")
            turn_right(0.1)
        print("Go Forward")
        
        motor4.Forward()
        motor3.Forward()
        sleep(t)
    
  #  motor3.off() #Stops Motor 3
   # motor4.off() #Stops Motor 4

if __name__ == "__main__":
    go_forward(1)
