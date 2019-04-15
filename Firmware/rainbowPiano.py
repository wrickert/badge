import machine
import time
import neopixel
from notes import *
import random

import esp32

pin13 = machine.Pin(13)
speaker = machine.PWM(pin13)
speaker.duty(0)

current = 0
thresh = 350
colors = [(0,0,0),(0,0,0)]

t0 = machine.TouchPad(machine.Pin(4))
t1 = machine.TouchPad(machine.Pin(15))
t2 = machine.TouchPad(machine.Pin(12))
t3 = machine.TouchPad(machine.Pin(14))

t0.config(thresh)
t1.config(thresh)
t2.config(thresh)
t3.config(thresh)

np = neopixel.NeoPixel(machine.Pin(25), 10)
#np = neopixel.NeoPixel(machine.Pin(25), 10, bpp=4)


esp32.wake_on_touch(True)


# This function controls adding colors to the neopixel strip
def stackColor(key):
    global colors

    if key == 1:
        colors.insert(0,(255,0,0))
    if key == 2:
        colors.insert(0,(0,255,0))
    if key == 3:
        colors.insert(0,(0,0,255))
    if key == 4:
        colors.insert(0,(255,255,0))

    print(colors)
    
    size = len(colors)
    if size > 10:
        size = 10
        colors.pop()

    for i in range(0, size): 
        np[i] = colors[i]

    np.write()

# Program starts here
def keys():
    global thresh
    while True:
        try:
            if t0.read() < thresh:
                time.sleep(0.02)
                if t0.read() < thresh:
                    setTone(1)
            elif t1.read() < thresh:
                time.sleep(0.02)
                if t1.read() < thresh:
                    setTone(2)
            elif t2.read() < thresh:
                time.sleep(0.02)
                if t2.read() < thresh:
                    setTone(3)
            elif t3.read() < thresh:
                time.sleep(0.02)
                if t3.read() < thresh:
                    setTone(4)
            else:
                setTone(0)
            #print("Going to sleep")
            #machine.lightsleep()
        except ValueError:
            f = open('silent.txt', 'w')
            f.write('t')
            f.close()
            machine.reset()

def setTone(key):
    global current
    if key == 0:
        speaker.duty(0)
        current = 0
    elif key == 1 and current != key:
        stackColor(1)
        print("1")
        speaker.duty(100)
        speaker.freq(G4)
        current = 1
    elif key == 2 and current != key:
        stackColor(2)
        print("2")
        speaker.duty(100)
        speaker.freq(B4)
        current = 2
    elif key == 3 and current != key:
        stackColor(3)
        print("3")
        speaker.duty(100)
        speaker.freq(CS5)
        current = 3
    elif key == 4 and current != key:
        stackColor(4)
        print("4")
        speaker.duty(100)
        speaker.freq(D5)
        current = 4

def clear():
    for i in range(10):
        colors[i] = (0,0,0)
        np[i] = (0,0,0)
        np.write() 
        time.sleep(0.02)


def play_note(freq: int, play_time: float = .2):
    """
    Plays a note of frequency `freq` for duration `play_time`, and lights up a random LED for fun
    :param freq: The frequency of the note to play, in hz
    :param play_time: The duration of the note, in seconds
    :return: Null
    """
    speaker.duty(100)
    speaker.freq(freq)
    stackColor(random.randint(1, 4))
    time.sleep(play_time)
    speaker.duty(0)
