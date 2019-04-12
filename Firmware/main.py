import rainbowPiano
import time
from notes import *
from math import ceil

# POST stuff for testing
# rainbowPiano.setTone(1)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(1)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(2)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(2)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(3)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(4)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(3)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(3)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(2)
# time.sleep(0.5)
# rainbowPiano.setTone(0)
# rainbowPiano.setTone(1)
# time.sleep(0.5)
# rainbowPiano.setTone(0)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(A4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(AS4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(A4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(CS4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(A4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(ceil((CS4 + CS5)/2), 1)

rainbowPiano.play_note(ceil((CS5 + A4 + D4)/3), 1)

rainbowPiano.play_note(D4, 1)
rainbowPiano.play_note(C5, 1)
rainbowPiano.play_note(C4, 1)

# Second stave

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(A4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(AS4)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(C5)

rainbowPiano.play_note(D4)
rainbowPiano.play_note(D4)
rainbowPiano.play_note(ceil((CS5 + A3)/2))

rainbowPiano.play_note(ceil((CS4 + A4 + FS4 + D4)/4), 1)
rainbowPiano.play_note(ceil((D6 + FS5 + D5 + D4)/4), 1.5)


rainbowPiano.clear()

rainbowPiano.keys()
