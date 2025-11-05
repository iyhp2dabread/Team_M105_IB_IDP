#Goes forward, using motors.
from machine import Pin, PWM
from utime import sleep
from stop import stop

def emergency_stop(crit_distance):

    global prev_state
    current = button.value()
    
    #Rising edge
    if current == 1 and prev_state == 0:
        sleep(0.05) #debounce
        if button.value == 1:     #confirm still pressed
            prev_state = 1
            return 1     #Emergency stop should be triggered from this
        
    if current == 0 and prev_state == 1:
        prev_state = 0
    
    #Emergency stop due to distance sensor
    if distance_sensor() <= crit_distance:
        return 1
    
    return 0
    
stop()
