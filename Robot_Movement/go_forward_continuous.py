#Goes forward, using motors.
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
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
button = Pin(12, Pin.IN, Pin.PULL_DOWN)  

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=80):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=30):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))


def go_forward(t):
    motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
    motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7
    
    print("Go forward continuous active")

    #Give a little push off the line
    motor3.Forward(speed = 60)
    motor4.Forward(speed = 40)
    sleep(0.1)
    while True:
        ls = left_sensor()
        rs = right_sensor()
        fl = forward_left_sensor()
        fr = forward_right_sensor()
        #Emergency stop
     #   if emergency_stop(60) == 1:
      #      stop()
       #     break
        
        #Robot lost the line
        if ls == 1 or rs == 1:
            print("Junction/Turn reached, stopping")
            stop()
            break
        if fl == 0 and fr == 0:
            stop()
            sleep(0.1)
            found = False
             # Try turning right slowly
            for _ in range(5):
                motor3.Forward(70)
                motor4.Reverse(70)
                sleep(0.05)
                if fl == 1 or fr == 1:
                    print("Line reacquired (right spin)!")
                    found = True
                    break
            stop()
            sleep(1)
            
            # If not found, try turning left slowly
            if not found:
                for _ in range(10):  # a bit longer sweep the other way
                    motor3.Reverse(70)
                    motor4.Forward(70)
                    sleep(0.05)
                    if fl == 1 or fr == 1:
                        print("Line reacquired (left spin)!")
                        found = True
                        break
                stop()
                sleep(1)
                
            if not found:
                print("Line not found after scanning — stopping.")
                stop()
                break  # end loop safely

            # Resume forward motion after reacquiring
            continue
            break
        
        elif ls == 1 or rs == 1:
            print("Junction/Turn reached, stopping")
            stop()
            break
        
        #Small corrections to stay on line
        elif fl == 1 and fr == 0:
            motor3.Forward(speed = 60)
            motor4.Forward(speed = 65)
        elif fl == 0 and fr == 1:
            motor4.Forward(speed = 60)
            motor3.Forward(speed = 80)
            
        #Fully on line
        else:
            motor3.Forward(speed = 90)
            motor4.Forward(speed = 70)
        
        sleep(t)
        current = button.value()

         #Detect rising edge (0 -> 1)
      #  if current == 1 and prev_state == 0:
       #     latched = not latched  # toggle the latch
        #    led.value(latched)     # update output
         #   print("Button toggled. Latched =", latched)

        #prev_state = current  # store for next loop
    

if __name__ == "__main__":
    go_forward(0.001)

