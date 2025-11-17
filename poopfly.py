from random import randint
import time

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund']
enamn = ['den fördärvade', 'Bajs', 'McMillen', 'Döden', 'O´ Moriah', 'Kall']

class karaktar:
    def __init__(karaktar, namn, kp, sty, niva, inventarie):
        karaktar.namn = namn
        karaktar.kp = kp
        karaktar.sty = sty
        karaktar.niva = niva
        karaktar.inventarie = inventarie

tempkp = randint(1, 5)
tempsty = randint(5, 15)//tempkp
sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]} {enamn[randint(0, len(enamn)-1)]}", tempkp, tempsty, 0, 1)
print(sp1.namn)
print(sp1.kp)
print(sp1.sty)

if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

while True:
    val = input('''Vad vill du göra?
                Kolla [R]yggsäcken
                Öppna en [D]örr
                Kolla [F]ärdigheter 
                -> ''')
    
