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

inventarie = []
tempkp = randint(1, 5)
tempsty = randint(5, 15)//tempkp
sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]} {enamn[randint(0, len(enamn)-1)]}", tempkp, tempsty, inventarie, 0,)
print(sp1.namn)

if sp1.namn[-1] == 's':
    plural = ""
else:
    plural = "s"

class monster: #strukturen alla monster följer
    def __init__(monster, monstertyp, sty):
        monster.monstertyp = monstertyp
        monster.sty = sty


monsteralternativ = [ #möjliga fiender
    monster('Guldfisk', 1),
    monster('Goblin', 3),
    monster('Häxa', 5),
    monster('Troll', 7),
    monster('Rikard', 10),
]


fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
print(f"Ett vild {fiende.monstertyp} dyker upp!")
print(f"Den har styrkan {fiende.sty}")
print(f"{sp1.namn}{plural} styrka är {sp1.sty}")