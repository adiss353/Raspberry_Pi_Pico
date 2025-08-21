import machine
import utime
import urandom

pressed = False
led = machine.Pin(10, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        time_reaction = utime.ticks_diff(utime.ticks_ms(), time_start)
        print("Your reaction time was " + str(time_reaction) + " milliseconds! ")
        print("Nice time, congratulation!")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

time_start = utime.ticks_ms()

button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
