import machine 
import utime

#each segment
pins = [
    machine.Pin(13 , machine.Pin.OUT), #DP
    machine.Pin(12 , machine.Pin.OUT), #C - bottom right
    machine.Pin(11 , machine.Pin.OUT), #D - bottom
    machine.Pin(10 , machine.Pin.OUT), #E - bottom left
    machine.Pin(16 , machine.Pin.OUT), #B - top right
    machine.Pin(17 , machine.Pin.OUT), #A - top
    machine.Pin(18 , machine.Pin.OUT), #F - top left
    machine.Pin(19 , machine.Pin.OUT)  #G - middle
]

#leds
leds = [
    machine.Pin(26, machine.Pin.OUT),  #3
    machine.Pin(22, machine.Pin.OUT),  #2
    machine.Pin(21, machine.Pin.OUT),  #1
    machine.Pin(20, machine.Pin.OUT)   #0
]

#buttons
buttons = [
    machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN), #3
    machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN), #2
    machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN), #1
    machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN), #0
]

button_pressed = [
    False,
    False,
    False,
    False
]

# common anode
# each led segment is turned on when a negative value comes from RPI Pico
chars = [
    #DP,C, D, E, B, A, F, G
    [1, 0, 0, 0, 0, 0, 0, 1], #0
    [1, 0, 1, 1, 0, 1, 1, 1], #1
    [1, 1, 0, 0, 0, 0, 1, 0], #2
    [1, 0, 0, 1, 0, 0, 1, 0], #3
    [1, 0, 1, 1, 0, 1, 0, 0], #4
    [1, 0, 0, 1, 1, 0, 0, 0], #5
    [1, 0, 0, 0, 1, 0, 0, 0], #6
    [1, 0, 1, 1, 0, 0, 1, 1], #7
    [1, 0, 0, 0, 0, 0, 0, 0], #8
    [1, 0, 1, 1, 0, 0, 0, 0], #9
    [1, 0, 1, 0, 0, 0, 0, 0], #A
    [1, 0, 0, 0, 1, 1, 0, 0], #B
    [1, 1, 0, 0, 1, 0, 0, 1], #C
    [1, 0, 0, 0, 0, 1, 1, 0], #D
    [1, 1, 0, 0, 1, 0, 0, 0], #E
    [1, 1, 1, 0, 1, 0, 0, 0]  #F
    #DP,C, D, E, B, A, F, G
]

# 4-bit representation
binary = [
    #3, 2, 1, 0 - 2^n
    [0, 0, 0, 0], #0
    [0, 0, 0, 1], #1
    [0, 0, 1, 0], #2
    [0, 0, 1, 1], #3
    [0, 1, 0, 0], #4
    [0, 1, 0, 1], #5
    [0, 1, 1, 0], #6
    [0, 1, 1, 1], #7
    [1, 0, 0, 0], #8
    [1, 0, 0, 1], #9
    [1, 0, 1, 0], #A
    [1, 0, 1, 1], #B
    [1, 1, 0, 0], #C
    [1, 1, 0, 1], #D
    [1, 1, 1, 0], #E
    [1, 1, 1, 1]  #F
    #3, 2, 1, 0 - 2^n
]

def all_off():
    for i in pins:
        i.value(1)
    for i in leds:
        i.value(0)

def all_on():
    for i in pins:
        i.value(0)
    for i in leds:
        i.value(1)

# functions counting from 0 to F
# hex and bin
def hex_and_bin():
    for i in range(16):
        for j in range(len(pins)):
            pins[j].value(chars[i][j])
        for j in range(len(leds)):
            leds[j].value(binary[i][j])
        utime.sleep(1)
# hex
def hex():
    for i in range(len(chars)):
        for j in range(len(pins)):
            pins[j].value(chars[i][j])
        utime.sleep(1)
# bin
def bin():
    for i in range(len(binary)):
        for j in range(len(leds)):
            leds[j].value(binary[i][j])    
        utime.sleep(1)

# bin to hex conversion
def conversion():
    dec = 0
    j = 3
    for i in range(len(leds)):
        if leds[i].value() == 1:
                dec = dec + 2 ** j
        j = j -1  
    for i in range(len(pins)):
        pins[i].value(chars[dec][i])               

# main function #

all_off()

while True:
    for i in range(len(buttons)):
        if buttons[i].value() == 1:
            if button_pressed[i] == False:
                leds[i].value(1)
                button_pressed[i] = True  
                utime.sleep(0.5)     
            elif button_pressed[i] == True:
                leds[i].value(0)
                button_pressed[i] = False
                utime.sleep(0.5)
        conversion()
       