import machine
import utime

buzzer = machine.PWM(machine.Pin(16))
c = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
d = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
e = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
f = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
g = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
a = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
h = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

button = [c, d, e, f, g, a, h]
tones = [523, 587, 659, 698, 784, 880, 988]

global button_pressed
button_pressed = False

def bequiet():
    buzzer.duty_u16(0)

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    utime.sleep(0.3)
    bequiet()

while True:
    bequiet()
    for i in range(len(button)): 
        if button[i].value() == 1:
            playtone(tones[i])
        