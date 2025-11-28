from random import randint
import time
from skatter import skatt
from skatter import k1, k2, k3, k4
from ormbarst_name_gen import von_ormbarst_namn

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', 'gon', 'Filip', 'Holger']
enamn = [', den fördärvade', ' Bajs', ' McMillen', ' Döden', ' O´ Moriah', ' Kall', ' Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oförfärad', ', den oupplysta', ', den enigmatiska', ', den godtyckliga']

class karaktar:
    bas_kp = randint(5, 10)
    bas_sty = randint(25, 50)//bas_kp
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
        stymult = 1
        kpmult = 1
        for i in range(len(self.inventarie)):
            if self.inventarie[i - 1].mod_ar_mult == True:
                stymult += self.inventarie[i - 1].kpmod
                kpmult += self.inventarie[i - 1].stymod
            else:
                self.kpmod += self.inventarie[i - 1].kpmod
                self.stymod += self.inventarie[i -1].stymod
                self.nivamod += self.inventarie[i - 1].nivamod
        if self.bas_kp + self.kpmod * kpmult < 1:
                self.kp = 1
        else:
            self.kp = self.bas_kp + self.kpmod * kpmult + self.niva
        self.sty = self.bas_sty + self.stymod * stymult + self.niva
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
        if val in str(range(1, len(self.inventarie))):
            self.inventarie.pop(int(val))



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
    def __init__(monster, genus, monstertyp, sty, kp):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty
        monster.kp = kp

monsteralternativ = [ #möjliga fiender
    monster('En vild', 'Guldfisk', 2, 1),
    monster('En vild', 'Goblin', 4, 1),
    monster('En vild', 'Häxa', 6, 1),
    monster('Ett vilt', 'Troll', 8, 1),
    monster('En vild', 'Rikard', 10, 1),
    monster('En galen', 'Blottare', 6, 1),
    monster('En kittel', 'fladdermöss', 4, 1)
]

bossmonsteralternativ = [ # möjliga bossar
    monster('Den store och mäktiga fritidsledaren: ', 'Mojje', 100, 100),
    monster('Den fruktansvärt (gulliga): ', 'Bleh', 77, 77),
    monster('"Jag skulle behöva en önskan just nu..."', 'Mortecai', 89, 50),
    monster('Den', 'den', 1, 1)
]

while True: #Hela spelloopen
    rumstyp = ['monsterrum', 'skattkammare', 'skatterum', 'bossrum', 'läkerum']
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
                mod = 'mod'
                if sp1.inventarie[i - 1].mod_ar_mult == True:
                    mod = 'mult'
                print(f'{i+1}. {sp1.inventarie[i - 1].namn} | Kvalitet: {sp1.inventarie[i - 1].kvalitet}\n  {sp1.inventarie[i - 1].beskrivning}\n   KP {mod}: {sp1.inventarie[i - 1].kpmod} | STY {mod}: {sp1.inventarie[i -1].stymod} | Nivå mod: {sp1.inventarie[i - 1].nivamod}\n')

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
            print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}')

        else:
            continue
        
    if rumstyp[int(val)-1] == 'monsterrum':
        
        fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
        print(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        print(f"Den har styrkan {fiende.sty}")
        print(f"{sp1.namn}{plural} styrka är {sp1.sty}")

        time.sleep(0.5)

        (input("här kommer du få fatta beslut, men inte riktigt än :/ (skriv något och tryck enter) \n\n"))


        if sp1.sty > fiende.sty: #kollar vem som vinner
            print(f"{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n")
            sp1.niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: 
            print(f"Det var en svår strid, utan wiener. Du tar ingen skada men går inte upp en nivå. \n\n")
        else:
            print(f"{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade 1 kp. \n\n")
            sp1.skada += 1

        time.sleep(0.5)

        print(f"{sp1.namn} har {sp1.kp - sp1.skada} kp kvar.")
        print(f"{sp1.namn} är nivå {sp1.niva}.")
    
    elif rumstyp[int(val)-1] == 'skattkammare':
        evigsakkvalitet = randint(1, 100)
        if evigsakkvalitet >= 96 and len(k4) > 0:
            tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
            k4.remove(tillvunnet_foremal)
        elif evigsakkvalitet >= 81 and len(k3) > 0:
            tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
            k3.remove(tillvunnet_foremal)
        elif evigsakkvalitet > 61 and len(k2) > 0:
            tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
            k2.remove(tillvunnet_foremal)
        elif len(k1) > 0:
            tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
            k1.remove(tillvunnet_foremal)
        else:
            tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
        sp1.tilvinna_skatt(tillvunnet_foremal)
    # elif rumstyp[int(val)-1] == 'skatterum':

    # elif rumstyp[int(val)-1] == 'bossrum':

    # elif rumstyp[int(val)-1] == 'läkerum':