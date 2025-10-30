from machine import Pin
from utime import sleep

def amber_led(): #turns amber LED on
    #amber LED
    led_amber_pin = 28  # Pin 28 = GP28 (labelled 34 on the jumper)
    led_amber = Pin(led_amber_pin, Pin.OUT)
    
    #Red LED
    led_red_pin = 8  # Pin 8 = GP8 (labelled 11 on the jumper)
    led_red = Pin(led_red_pin, Pin.OUT)

    print("Amber LED ON")
    led_red.value(0)
    led_amber.value(1)

if __name__ == "__main__":
    amber_led()
