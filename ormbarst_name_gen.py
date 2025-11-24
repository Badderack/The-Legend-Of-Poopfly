import random
from random import randint

def von_ormbarst_namn():
    antal = randint(1, 2) #längd på namnet
    repeat = antal
    name = ""
    for i in range(repeat):
        if i == 0:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz").upper()
        else:
            konsonant = random.choice("bcdfghjklmnpqrstvwxz")
        vokal = random.choice("aeiouy")
        name += konsonant + vokal
    name += "gon von Ormbarst"
    return(name)