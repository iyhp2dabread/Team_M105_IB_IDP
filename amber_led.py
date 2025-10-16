from machine import Pin
from utime import sleep

def amber_led(): #turns amber LED on
    #amber LED
    led_amber_pin = 28  # Pin 28 = GP28 (labelled 34 on the jumper)
    led_amber = Pin(led_amber_pin, Pin.OUT)
    
    #Red LED
    led_red_pin = 22  # Pin 22 = GP22 (labelled 29 on the jumper)
    led_red = Pin(led_red_pin, Pin.OUT)

    print("Amber LED ON")
    led_amber.value(1)
    led_red.value(0)
    sleep(5)
    led_amber.value(0)
    print("test complete")

if __name__ == "__main__":
    amber_led()
