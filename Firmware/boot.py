import rainbowPiano

try:
    f = open('silent.txt')
    f.close()
except OSError:
    f = open('silent.txt', 'w')
    f.write('f')
    f.close()
