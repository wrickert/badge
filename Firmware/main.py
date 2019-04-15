import rainbowPiano
import time
import machine

machine.freq(80000000)

# POST stuff for testing
f = open('silent.txt')
if f.read() == 'f':
    rainbowPiano.setTone(1)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(1)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(2)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(2)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(3)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(4)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(3)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(3)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(2)
    time.sleep(0.5)
    rainbowPiano.setTone(0)
    rainbowPiano.setTone(1)
    time.sleep(0.5)
    rainbowPiano.setTone(0)

    rainbowPiano.clear()
else:
    f.close()
    f = open('silent.txt', 'w')
    f.write('f')

f.close()
rainbowPiano.keys()
