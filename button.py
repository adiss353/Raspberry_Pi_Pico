import machine
import utime

button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

#print(button.value())

while True:
    if button.value() == 1:
        print("Oh, you pressed the button")
        utime.sleep(2)