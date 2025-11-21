from random import randint
import time
from skatter import skatt
from skatter import k1, k2, k3, k4
from ormbarst_name_gen import von_ormbarst_namn

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', '', 'Filip']
enamn = [', den fördärvade', 'Bajs', 'McMillen', 'Döden', 'O´ Moriah', 'Kall', 'Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oförfärad', ', den oupplysta', ', den enigmatiska', ', den godtyckliga']

class karaktar:
    bas_kp = randint(1, 5)
    bas_sty = randint(5, 15)//bas_kp
    bas_niva = 0
    kpmod = 0
    stymod = 0
    nivamod = 0
    skada = 0
    def __init__(karaktar, namn, kp, sty, niva, inventarie):
        karaktar.namn = namn
        karaktar.kp = kp
        karaktar.sty = sty
        karaktar.niva = niva
        karaktar.inventarie = inventarie

sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]} {enamn[randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva, [])#Skapar rollpersonen
if sp1.namn[0] == '':
    sp1.namn = von_ormbarst_namn()

evigsakkvalitet = randint(1, 100) #Bestämmer startföremålets (evighetsföremålet) kvalitet
if evigsakkvalitet >= 95:
    evigsakkvalitet = k4
elif evigsakkvalitet >= 80:
    evigsakkvalitet = k3
elif evigsakkvalitet > 60:
    evigsakkvalitet = k2
else:
    evigsakkvalitet = k1

sp1.inventarie.append(evigsakkvalitet[randint(0, len(evigsakkvalitet) - 1)]) #Föremålet läggs till i spelare 1s inventraie
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie[0].namn} | Kvalitet: {sp1.inventarie[0].kvalitet}\n{sp1.inventarie[0].beskrivning}')
if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

while True:
    sp1.kpmod = 0
    sp1.stymod = 0
    sp1.nivamod = 0
    for i in range(len(sp1.inventarie)):
        sp1.kpmod += sp1.inventarie[i - 1].kpmod
        sp1.stymod += sp1.inventarie[i -1].stymod
        sp1.nivamod += sp1.inventarie[i - 1].nivamod
    if sp1.bas_kp + sp1.kpmod < 1:
        sp1.kp = 1
    else:
        sp1.kp = sp1.bas_kp + sp1.kpmod
    sp1.sty = sp1.bas_sty + sp1.stymod
    sp1.niva = sp1.bas_niva + sp1.nivamod
    if sp1.kp - sp1.skada < 1:
        quit()
    val = input('''Vad vill du göra?
                Kolla [R]yggsäcken
                Öppna en [D]örr
                Kolla [F]ärdigheter 
                -> ''').upper()
    if val == 'R':
        for i in range(len(sp1.inventarie)):
            print(f'{i+1}. {sp1.inventarie[i - 1].namn} | Kvalitet: {sp1.inventarie[i - 1].kvalitet}\n  {sp1.inventarie[i - 1].beskrivning}\n   KP mod: {sp1.inventarie[i - 1].kpmod} | STY mod: {sp1.inventarie[i -1].stymod} | Nivå mod: {sp1.inventarie[i - 1].nivamod}\n')
    elif val == 'D':
        print('D')
    elif val == 'F':
        print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} | STY: {sp1.sty}')
    else:
        continue
