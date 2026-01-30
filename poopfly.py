import random
import time
import text_utils
import rum
from karaktär import karaktar
from monsterrum import monsterrum
from rum_med_skatter import rum_med_skatter
from skatterum import skatterum
from bossrum import bossrum
from läkerum import läkerum
from fällrum import fällrum

print('''
                                _____ _
                               |_   _| |__   ___
                                 | | | '_ \ / _ |
                                 | | | | | |  __/
                                 |_| |_| |_|\___|
             :::       :::::::::::::::::: ::::::::::::::    ::::::::::::
            :+:       :+:      :+:    :+::+:       :+:+:   :+::+:    :+:
           +:+       +:+      +:+       +:+       :+:+:+  +:++:+    +:+
          +#+       +#++:++# :#:       +#++:++#  +#+ +:+ +#++#+    +:+
         +#+       +#+      +#+   +#+#+#+       +#+  +#+#+#+#+    +#+
        #+#       #+#      #+#    #+##+#       #+#   #+#+##+#    #+#
       ############################ #############    #############
                                          __
                                    ___  / _|
                                   / _ \| |_
                                  | (_) |  _|
                                   \___/|_|
         :::::::::  ::::::::  :::::::: ::::::::: :::::::::::::    :::   :::
        :+:    :+::+:    :+::+:    :+::+:    :+::+:       :+:    :+:   :+:
       +:+    +:++:+    +:++:+    +:++:+    +:++:+       +:+     +:+ +:+
      +#++:++#+ +#+    +:++#+    +:++#++:++#+ :#::+::#  +#+      +#++:
     +#+       +#+    +#++#+    +#++#+       +#+       +#+       +#+
    #+#       #+#    #+##+#    #+##+#       #+#       #+#       #+#
   ###        ########  ######## ###       ###       #############
''')

input('Träd in i fängelshålan och ta med dig Poopfly:n på [RETUR]resan')

sp1:karaktar = karaktar.skapa_karaktär()

print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie[0].namn} | Kvalitet: {sp1.inventarie[0].kvalitet}\n{sp1.inventarie[0].beskrivning}\n')

#RESTEN AV INTROT

text_utils.slow(f'{sp1.namn} träder in genom portarna...\n')
time.sleep(1)
text_utils.slow(f'Stendörrarna gnisslar mot golvet när de stängs bakom {sp1.namn}...\n')
time.sleep(1)
text_utils.slow(f'{sp1.namn} tar ett djupt andetag och ser sig omkring...\n')
time.sleep(1)
text_utils.slow(f'{sp1.namn} står i ett stort stenrum med tre dörrar...\n')
time.sleep(1)
text_utils.slow(f'Nu söker du poopfly!\n')

#Alla våra monster:

attackbeskrivning = [f'slår {sp1.namn}', f'sparkar {sp1.namn}', f'klöser {sp1.namn} med tånaglarna', f'biter {sp1.namn}', f'slickar {sp1.namn}', f'sticker {sp1.namn}', f'krossar {sp1.namn}',] #kul beskrivning för hur spelaren attackeras.

sp1.starttid = time.time() #startar en timer för spelet

def generera_rum(spelare) -> list:
    rumstyp = ['monsterrum']*6+['rum med skatter']*2+['skatterum']*2+['bossrum']*2+['läkerum']*2
    rumstyp += ['fällrum']*len(spelare.inventarie)#lägger till fällor baserat på hur många föremål spelaren har
    while len(rumstyp) > 3: #tar bort rum tills det bara är tre kvar
        rumstyp.pop(random.randint(0, len(rumstyp)-1)) 
    random.shuffle(rumstyp) #slumpar ordningen på rumme
    rumslista = []
    for rumsräng in rumstyp:
        if rumsräng == 'monsterrum':
            rumslista.append(monsterrum())
        elif rumsräng == 'rum med skatter':
            rumslista.append(rum_med_skatter())
        elif rumsräng == 'skatterum':
            rumslista.append(skatterum())
        elif rumsräng == 'bossrum':
            rumslista.append(bossrum())
        elif rumsräng == 'läkerum':
            rumslista.append(läkerum())
        elif rumsräng == 'fällrum':
            rumslista.append(fällrum())
    return rumslista 

while True: #Hela spelloopen
    sp1.start_tur()
    rumslista: list[rum.rum] = generera_rum(sp1)
    dörrbeskrivningar = [rummet.få_dörr_beskrivning(sp1) for rummet in rumslista]
    text_utils.slow(f'{sp1.namn} ser tre dörrar: \n en {dörrbeskrivningar[0]} \n en {dörrbeskrivningar[1]} \n och en {dörrbeskrivningar[2]}\n')

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        if val == 'R':
            sp1.print_inventarie()
        elif val == 'F': #printar spelarens färdigheter
            sp1.print_färdigheter()
        elif val == 'D':
            while val not in ['1','2','3','4']:
                val = input(f'Vilken dörr vill du öppna? \n [1] {dörrbeskrivningar[0]} \n [2] {dörrbeskrivningar[1]} \n [3] {dörrbeskrivningar[2]} \n [4] Avbryt \n ->')
                if val not in ['1', '2', '3', '4']:
                    text_utils.slow('Ogiltigt val: välj igen') #om spelaren inte väljer ett giltigt val.
            if val in ['1', '2', '3']: #om spelaren väljer att öppna en dörr
                valt_rum = rumslista[int(val)-1]
                text_utils.slow(f'{sp1.namn} kliver in i ett {valt_rum.rumstyp}\n') #rumstypen avsjöjas för spelaren
                time.sleep(1)
                break

    valt_rum.gå_in(sp1)