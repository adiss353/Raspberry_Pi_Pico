import machine
import utime
import _thread

led_red = machine.Pin(9, machine.Pin.OUT)
led_yellow = machine.Pin(11, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
buzzer = machine.Pin(6, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

global button_pressed
button_pressed = False

def button_reader():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)

_thread.start_new_thread(button_reader, ())

while True:
    
    if button_pressed == True:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        button_pressed = False

    # led_red.value(0)
    # utime.sleep(2)
    led_red.value(1)
    utime.sleep(5)
    led_yellow.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_yellow.value(1)
    utime.sleep(5)
    led_yellow.value(0)
