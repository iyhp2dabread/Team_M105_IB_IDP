from machine import Pin
from utime import sleep

def amber_led_on(): #turns amber LED on
    #amber LED
    led_amber_pin = 28  # Pin 28 = GP28 (labelled 34 on the jumper)
    led_amber = Pin(led_amber_pin, Pin.OUT)

    print("Amber LED ON")
    led_amber.value(1)

def amber_led_off(): #turns amber LED off
    #amber LED
    led_amber_pin = 28  # Pin 28 = GP28 (labelled 34 on the jumper)
    led_amber = Pin(led_amber_pin, Pin.OUT)

    print("Amber LED OFF")
    led_amber.value(0)

if __name__ == "__main__":
    amber_led_on()
    sleep(5)
    amber_led_off()

