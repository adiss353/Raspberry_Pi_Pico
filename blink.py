import machine
import utime

led_external = machine.Pin(16, machine.Pin.OUT)
#led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    # 1st option
    led_external.value(1)
    #led_onboard.value(0)
    utime.sleep(1)
    led_external.value(0)
    #led_onboard.value(1)
    utime.sleep(1)
    # 2nd option
    # led_external.toggle()
    # utime.sleep(1)