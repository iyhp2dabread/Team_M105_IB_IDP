from machine import Pin
from utime import sleep

def tiny_code_red_led_switch_on(): #turns QR Code reader and red LED on
    #tiny code reader and red LED control pin
    switch_pin = 8  # Pin 8 = GP8 (labelled 11 on the jumper)
    switch = Pin(switch_pin, Pin.OUT)

    print("QR Code Reader and Red LED ON")
    switch.value(1)

def tiny_code_red_led_switch_off(): #turns QR Code reader and red LED off
    #tiny code reader and red LED control pin
    switch_pin = 8  # Pin 8 = GP8 (labelled 11 on the jumper)
    switch = Pin(switch_pin, Pin.OUT)

    print("QR Code Reader and Red LED OFF")
    switch.value(0)

if __name__ == "__main__":
    tiny_code_red_led_switch_on()
    sleep(5)
    tiny_code_red_led_switch_off()
