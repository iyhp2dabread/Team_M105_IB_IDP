from go_forward_continuous import go_forward
from stop import stop
from turn_left import turn_left
from turn_right import turn_right
from forward_left_line_sensor import forward_left_sensor
from forward_right_line_sensor import forward_right_sensor
from machine import Pin, PWM
from utime import sleep
from left_line_sensor import left_sensor
from right_line_sensor import right_sensor
#from area1_to_lower_junction import area1_to_lj
from machine import Pin, I2C
from go_to_areas import go_area1_v2
from go_to_areas import go_area2_v2
from go_to_areas import go_area3_v2
from go_to_areas import go_area4_v2
from start_area_forward import start_area_forward
from stop import stop
from go_to_bay_entrance import go_bay_entrance 

from amber_led import amber_led_on
from amber_led import amber_led_off
#from bay_checking import bay_check
print("Welcome to main.py!")

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
print("I2C devices found:", i2c.scan())

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

motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7

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


test_sensors = False
while test_sensors == True:
    print(left_sensor(), forward_left_sensor(), forward_right_sensor(), right_sensor() )
    sleep(1)


 
ON = False
#!!!!!!!!!!!!!!!!!!
#PUT MAIN PROGRAM IN HERE 
if latched == True:
    print("GO")
    amber_led_off()

    #Call function to leave start bay and go to bay entrance
    start_area_forward(0.01)
    #Now at bay entrance
    #Call function to check bays
    unchecked_bays = [1, 1, 1, 1]
    bay_check(checked_bays)

    #Now has crate and is at bay exit
   
    
    current_qr = ['Rack B', 'Lower', 1]

    if current_qr[0] == 'Rack B' and current_qr[1] == 'Lower':
        #Go to area 1
        go_area1_v2()
        
        sleep(5)
        turn_left(2)
        turn_left(2)
        #At Checkpoint 1, facing south
        #for i in range(7 - int(current_qr[2])):
        #   go_forward(0.01)
        #turn_right(1)

        #Now at correct bay and Facing towards the bay
        #Perform crate drop procedure
        drop_crate()
        area1_to_lj()
        lj_to_be()
        
        

    if current_qr[0] == 'Rack B' and current_qr[1] == 'Upper':
        go_area2_v2()
        #At Area 2 facing onto racks
        for i in range(int(current_qr[2])):
            go_forward(0.01)
        turn_left(1)
        #Now at Correct bay, facing into bay
        #Perform crate drop procedure
        drop_crate()

    if current_qr[0] == 'Rack A' and current_qr[1] == 'Upper':
        #Go to area 3
        go_area3_v2()
        #At Checkpoint facing onto racks (south)
        #At checkpoint 3, facing South
        for i in range(7 - int(current_qr[2])):
            go_forward(0.01)
        turn_right(1)
        #Now at correct bay, facing into bay
        #Perform crate drop procedure
        drop_crate()

    if current_qr[0] == 'Rack A' and current_qr[1] == 'Lower':
        #Go to area 4
        go_area4_v2()
        #At checkpoint 4, facing south
        for i in range(int(current_qr[2])):
            go_forward(0.01)
        turn_left(1)

        #Now at correct bay, facing into bay
        #Perform crate drop procedure
        drop_crate()
else:
    stop()

    
        
    
    

##PUT PROGRAM HERE WHILST BUTTON IS NOT INSTALLED

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


motor3 = Motor(dirPin=4, PWMPin=5)  # Motor 3 is controlled from Motor Driv2 #1, which is on GP4/5
motor4 = Motor(dirPin=7, PWMPin=6)  # Motor 4 is controlled from Motor Driv2 #2, which is on GP6/7

stop()

print("main.py Done!")
