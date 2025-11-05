#Goes forward, for start up and returning back
from machine import Pin, PWM
from utime import sleep
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from turn_left import turn_left
from turn_right import turn_right
from stop import stop
#from emergency_stop import emergency_stop
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
from go_forward_continuous import go_forward
from amber_led import amber_led_on
from amber_led import amber_led_off
amber_led_off()

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

#Button to start program
button = Pin(12, Pin.IN, Pin.PULL_DOWN)  
led = Pin(15, Pin.OUT)
latched = False
prev_state = 0  # previous button reading
while True:
    current = button.value()

     #Detect rising edge (0 -> 1)
    if current == 1 and prev_state == 0:
        latched = not latched  # toggle the latch
        led.value(latched)     # update output
        print("Button toggled. Latched =", latched)
        break

    prev_state = current  # store for next loop
    sleep(0.05)  # 50 ms debounce delay

def start_area_forward(t):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    print("Start up go forward")
    amber_led_off()
    while True:
        #Emergency stop
        #if emergency_stop(60) == 1:
            #stop()
            #break
        
        #On the edge
        if left_sensor() == 1 or right_sensor() == 1:
            print("Start Box edge reached")
            """
            stop()
            sleep(1)
            print("a")
            turn_left()
            print("b")
            go_forward(0.01)
            print("c")
            turn_right()
            motor3.off()
            motor4.off()
            stop()
            amber_led_on()
            break
        """
            amber_led_on()
            sleep(0.48)
            turn_left()
            go_forward(0.01)
            break
        #In the dark region
        else:
            motor3.Forward(speed = 75)
            motor4.Forward(speed = 70)
            
        sleep(t)

stop()
start_area_forward(0.01)
