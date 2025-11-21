import sys
import time
import random
from random import randint

def zzz (text, väntan=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(väntan)
    print()

def von_ormbarst_namn():
    antal = randint(1, 2)
    repeat = antal
    name = ""
    for _ in range(repeat):
        konsonant = random.choice("bcdfghjklmnpqrstvwxz")
        vokal = random.choice("aeiouy")
        name += konsonant + vokal
        name += "gon von Ormbarst"
    output(name)

zzz(von_ormbarst_namn(), 0.05)