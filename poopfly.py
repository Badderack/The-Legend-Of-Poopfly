from random import randint
import time
from skatter import skatt
from skatter import k1, k2, k3, k4
from ormbarst_name_gen import von_ormbarst_namn

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', 'gon', 'Filip']
enamn = [', den fördärvade', ' Bajs', ' McMillen', ' Döden', ' O´ Moriah', ' Kall', ' Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oförfärad', ', den oupplysta', ', den enigmatiska', ', den godtyckliga']

class karaktar:
    bas_kp = randint(1, 5)
    bas_sty = randint(5, 15)//bas_kp
    bas_niva = 0
    kpmod = 0
    stymod = 0
    nivamod = 0
    skada = 0
    inventarie = []
    def __init__(self, namn, kp, sty, niva):
        self.namn = namn
        self.kp = kp
        self.sty = sty
        self.niva = niva

    def ge_stats(self):
        self.kpmod = 0
        self.stymod = 0
        self.nivamod = 0
        for i in range(len(self.inventarie)):
            self.kpmod += self.inventarie[i - 1].kpmod
            self.stymod += self.inventarie[i -1].stymod
            self.nivamod += self.inventarie[i - 1].nivamod
        if self.bas_kp + self.kpmod < 1:
            self.kp = 1
        else:
            self.kp = self.bas_kp + self.kpmod
            self.sty = self.bas_sty + self.stymod
            self.niva = self.bas_niva + self.nivamod
        if self.kp - self.skada < 1:
            quit('Förlust: Du har tagit mer träffar än du har KP!')

def tilvinna_skatt(self, skatt):
    output = ''
    print(self.inventarie)
    if len(self.inventarie) > 5:
        for i in range(0, len(self.inventarie)):
            output += f'{i+1}. {self.inventarie[i - 1].namn} | Kvalitet: {self.inventarie[i - 1].kvalitet}\n  {self.inventarie[i - 1].beskrivning}\n   KP mod: {self.inventarie[i - 1].kpmod} | STY mod: {self.inventarie[i -1].stymod} | Nivå mod: {self.inventarie[i - 1].nivamod}\n'
        val = input(f'''Vilken skatt i din ryggsäck vill du byta ut??
            {output}
            -> ''').upper()



sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]}{enamn[randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva)#Skapar rollpersonen
if sp1.namn[0] == 'g':
    sp1.namn = von_ormbarst_namn()

evigsakkvalitet = randint(1, 100) #Bestämmer startföremålets (evighetsföremålet) kvalitet
if evigsakkvalitet >= 96:
    evigsakkvalitet = k4
elif evigsakkvalitet >= 81:
    evigsakkvalitet = k3
elif evigsakkvalitet > 61:
    evigsakkvalitet = k2
else:
    evigsakkvalitet = k1

sp1.inventarie.append(evigsakkvalitet[randint(0, len(evigsakkvalitet)-1)]) #Föremålet läggs till i spelare 1s inventraie
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie[0].namn} | Kvalitet: {sp1.inventarie[0].kvalitet}\n{sp1.inventarie[0].beskrivning}')
if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

#Alla våra monster:

class monster: #strukturen alla monster följer
    def __init__(monster, genus, monstertyp, sty):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty

monsteralternativ = [ #möjliga fiender
    monster('En vild', 'Guldfisk', 2),
    monster('En vild', 'Goblin', 4),
    monster('En vild', 'Häxa', 6),
    monster('Ett vilt', 'Troll', 8),
    monster('En vild', 'Rikard', 10),
    monster('En galen', 'Blottare', 6),
    monster('En kittel', 'fladdermöss', 4)
]

bossmonsteralternativ = [ # möjliga bossar
    monster('Den store och mäktiga fritidsledaren: ', 'Mojje', 100),
    monster('Den fruktansvärt (gulliga): ', 'Bleh', 77),
    monster('"Jag skulle behöva en önskan just nu..."', 'Mortecai', 89)
]

while True: #Hela spelloopen
    rumstyp = ['monsterrum', 'skattkammare', 'skatterum', 'bossrum', 'Läkerum']
    while len(rumstyp) > 3:
        rumstyp.pop(randint(0, len(rumstyp)-1))
    print(f"{sp1.namn} ser tre dörrar {rumstyp}.")
    sp1.ge_stats()

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        
        if val == 'R':
            for i in range(len(sp1.inventarie)):
                print(f'{i+1}. {sp1.inventarie[i - 1].namn} | Kvalitet: {sp1.inventarie[i - 1].kvalitet}\n  {sp1.inventarie[i - 1].beskrivning}\n   KP mod: {sp1.inventarie[i - 1].kpmod} | STY mod: {sp1.inventarie[i -1].stymod} | Nivå mod: {sp1.inventarie[i - 1].nivamod}\n')

        elif val == 'D':
            while True:
                val = input(f'Vilken dörr vill du öppna? \n [1] {rumstyp[0]} \n [2] {rumstyp[1]} \n [3] {rumstyp[2]} \n [4] Avbryt \n ->')
                if val in ['1', '2', '3', '4']:
                    break
                else:
                    print('Ogiltigt val: välj igen')
                    continue
            if val in ['1', '2', '3']:
                print(f'{sp1.namn} kliver in i ett {rumstyp[int(val)-1]}')
                break

        elif val == 'F':
            print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} | STY: {sp1.sty}')

        else:
            continue
        
    print(f'Vi har fixat det, här kollas och öppnas ett rum!') #Rumskod:
    break