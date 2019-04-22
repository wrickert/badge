#rename to main.py to use with the exsisting code
import rainbowPiano
import time
from notes import *
from math import ceil
import machine

machine.freq(80000000)

def play_march():
    """
    Play the Imperial March.
    :return:
    """
		rainbowPiano.play_note(A4, .500)
		rainbowPiano.play_note(A4, .500)
		rainbowPiano.play_note(A4, .500)
		rainbowPiano.play_note(F4, .350)
		rainbowPiano.play_note(C5, .150)
		rainbowPiano.play_note(A4, .500)
		rainbowPiano.play_note(F4, .350)
		rainbowPiano.play_note(C5, .150)
		rainbowPiano.play_note(A4, .650)

		time.sleep(.500)

		rainbowPiano.play_note(E5, .500)
		rainbowPiano.play_note(E5, .500)
		rainbowPiano.play_note(E5, .500)
		rainbowPiano.play_note(F5, .350)
		rainbowPiano.play_note(C5, .150)
		rainbowPiano.play_note(GS4, .500)
		rainbowPiano.play_note(F4, .350)
		rainbowPiano.play_note(C5, .150)
		rainbowPiano.play_note(A4, .650)

		time.sleep(.500)

    #rainbowPiano.clear()

# POST stuff for testing
f = open('silent.txt')
if f.read() == 'f':
    play_march()

    rainbowPiano.inital()

else:
    f.close()
    f = open('silent.txt', 'w')
    f.write('f')

f.close()
machine.freq(40000000)
rainbowPiano.keys()
