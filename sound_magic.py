import winsound
from random import randrange
while True:
    frequency = randrange(5000)
    duration = randrange(2000)
    winsound.Beep(frequency, duration)