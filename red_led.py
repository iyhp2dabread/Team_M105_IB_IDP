from machine import Pin
from utime import sleep

def red_led(): #turns red LED on
    #amber LED
    led_amber_pin = 28  # Pin 28 = GP28 (labelled 34 on the jumper)
    led_amber = Pin(led_amber_pin, Pin.OUT)
    
    #Red LED
    led_red_pin = 22  # Pin 22 = GP22 (labelled 29 on the jumper)
    led_red = Pin(led_red_pin, Pin.OUT)

    print("Red LED ON")
    led_amber.value(0)
    led_red.value(1)

if __name__ == "__main__":
    red_led()
