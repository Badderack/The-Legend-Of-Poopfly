from random import randint
import time
from skatter import skatt
from skatter import print_skatt
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
        
        self.niva = self.bas_niva + self.nivamod
        if self.skada < 0:
            self.skada = 0
        if self.bas_kp + self.kpmod * kpmult < 1:
                self.kp = 1
        else:
            self.kp = self.bas_kp + self.kpmod * kpmult + (self.niva * 2)
        self.sty = self.bas_sty + self.stymod * stymult + (self.niva * 2)
        if self.niva >= 10:
            if self.kp - self.skada < 1:
                quit('Du vann och dog samtidigt... galet...')
            quit('Du vann spelet!!!!!!!!')
        elif self.kp - self.skada < 1:
            quit('Förlust: Du har tagit mer träffar än du har KP!')

def print_inventory(self):
    output = ''
    for i in range(len(sp1.inventarie)):
        output += f'{i+1}.{print_skatt(sp1.inventarie[i])}\n\n'
    return(output)
def print_player_stats(self):
    output = f'{self.namn + plural} färdigheter:\n  Nivå: {self.niva} | KP: {self.kp - self.skada} / {self.kp} | STY: {self.sty}'
    return(output)

def avskaffa_skatt(self):
    print(print_inventory(self))
    while True:
        val = input(f'Vilken skatt i din ryggsäck vill du byta ut??->')
        if int(val) in range(1, len(self.inventarie) + 1):
            if input(f'Är du säker på att du vill byta ut {self.inventarie[int(val) - 1].namn}? J/N ->').upper() == 'J':
                self.inventarie.pop(int(val) - 1)
                return()
            else:
                print('Skriv siffran som representerar föremålet du vill byta ut (1, 2, 3, 4, 5, 6)')

def tilvinna_skatt(self, skatt):
    self.inventarie.append(skatt)
    if len(self.inventarie) > 5:
        avskaffa_skatt(self)




sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]}{enamn[randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva)#Skapar rollpersonen
if sp1.namn[0] == 'g':
    sp1.namn = von_ormbarst_namn()

foremal_kvalitet = randint(1, 100) #Bestämmer föremåls kvalitet
if foremal_kvalitet >= 96:
    foremal_kvalitet = k4
elif foremal_kvalitet >= 81:
    foremal_kvalitet = k3
elif foremal_kvalitet > 61:
    foremal_kvalitet = k2
else:
    foremal_kvalitet = k1

sp1.inventarie.append(foremal_kvalitet[randint(0, len(foremal_kvalitet)-1)]) #Föremålet läggs till i spelare 1s inventraie
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

attackbeskrivning = [f'slår {sp1.namn}', 'sparkar {sp1.namn}', 'klöser {sp1.namn} med tånaglarna', 'biter {sp1.namn}', 'slickar {sp1.namn}', 'sticker {sp1.namn} med sin {monster.vapen}', 'krossar {sp1.namn} med {monster.vapen}',]

while True: #Hela spelloopen
    rumstyp = ['monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'skattkammare', 'skatterum', 'bossrum', 'läkerum']
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
            print(print_inventory(sp1))
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
                time.sleep(1)
                break

        elif val == 'F':
            print(print_player_stats(sp1))
        else:
            continue
        
    if rumstyp[int(val)-1] == 'monsterrum':
        sp1.ge_stats()
        fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
        print(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        print(f"Den har styrkan {fiende.sty}")
        print(f"{sp1.namn}{plural} styrka är {sp1.sty}")

        time.sleep(0.5)

        while True:
                monster_efterfoljande_bokstaver = 1
                if fiende.monstertyp[0] == 'R' or fiende.monstertyp[0] == 'F':
                    monster_bokstav = f'[{fiende.monstertyp[0]}{fiende.monstertyp[1]}]'
                    monster_efterfoljande_bokstaver = 2
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [{fiende.monstertyp[0]}]{fiende.monstertyp[monster_efterfoljande_bokstaver:]}
                                Kolla [F]ärdigheter 
                                -> ''')
                if val.upper() == 'R':
                    print(print_inventory(sp1))
                elif val == monster_bokstav:
                    break
                elif val.upper() == 'F':
                    print(print_player_stats(sp1))
                else:
                    continue

        if sp1.sty > fiende.sty: #kollar vem som vinner
            print(f"{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n")
            sp1.bas_niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: 
            print(f"Det var en svår strid, utan wiener. Du tar ingen skada men går inte upp en nivå. \n\n")
        else:
            print(f"{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade 1 kp. \n\n")
            sp1.skada += 1

        time.sleep(0.5)

        print(f"{sp1.namn} har {sp1.kp - sp1.skada} kp kvar.")
        print(f"{sp1.namn} är nivå {sp1.niva}.")
    
    
    elif rumstyp[int(val)-1] == 'skattkammare': #SKATTKAMMARE
        foremal_kvalitet = randint(1, 100)
        while True:
            if foremal_kvalitet >= 96:
                if len(k4) > 0:
                    tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
                    k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 81
                    continue
            elif foremal_kvalitet >= 81:
                if len(k3) > 0:
                    tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
                    k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 61
                    continue
            elif foremal_kvalitet > 61:
                if len(k2) > 0:
                    tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
                    k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif len(k1) > 0:
                tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
                k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
            break
        mod = 'mod'
        if skatt.mod_ar_mult == True:
            mod = 'mult'
        print('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {print_skatt(tillvunnet_foremal)}')
        while True:
            val = input('\nVill du plocka upp den? J/N ->').upper()
            if val == 'J':
                tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                print('Skriv in [J]a eller [N]ej')

    
    elif rumstyp[int(val)-1] == 'skatterum': #BETALA SKATT RUM
        print(f'{sp1.namn} kliver in i en mörk skattkammare')
        time.sleep(0.5)
        print(f'{sp1.namn} ser en dvärg i andra änden av rummet')
        print('"gadd eller kladd"')
        while True:
            val = input('Vad vill du betala i skatt? 1 [S]katt eller 2 [K]P -> ').upper()
            if val == 'S' or val == 'K':
                break
            else:
                print('Du måste skriva S eller K')
                continue 
        if val == 'K':
            sp1.skada += 2
        elif val == 'S':
            avskaffa_skatt(sp1)

    
    elif rumstyp[int(val)-1] == 'bossrum': #BOSS
        sp1.ge_stats()
        fiende = bossmonsteralternativ[randint(0, len(bossmonsteralternativ)-1)]
        print(f'I ett bossrum kommer turer att utkämpas tills spelaren eller bossen är döda, eller spelaren lyckas fly. Spelaren kommer bli slagen upp till bossens sty och spelaren slår upp till sin sty, mellan varje tur kan föremål användas.')
        print(f'Plötsligt dyker {fiende.genus} {fiende.monstertyp} upp och ger dig en fördärvande blick!')
        
        while fiende.kp > 0:
            print(f'{fiende.monstertyp} gör upp till {fiende.sty} skada!!!')
            print(f'{fiende.monstertyp} har {fiende.kp} kp')

            while True:
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [{fiende.monstertyp[0]}]{fiende.monstertyp[1:]}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
                elif val == fiende.monstertyp[0].upper():
                    break
                elif val == 'F':
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}')
                else:
                    continue


            slag = randint(1, fiende.sty)
            print(f'{fiende.monstertyp} {attackbeskrivning[randint(0, len(attackbeskrivning)-1)]} och gör {slag} skada!')
            sp1.skada += slag

            slag = randint(1, sp1.sty)
            print(f'{sp1.namn} slår {fiende.monstertyp} och gör {slag} skada')
            fiende.kp -= slag
            sp1.ge_stats()

        print(f'{sp1.namn} besegrade {fiende.monstertyp}!')
    
    
    elif rumstyp[int(val)-1] == 'läkerum': #HELNING
        sp1.skada = sp1.skada - randint(1,3)
        print('Du har nu helats!')