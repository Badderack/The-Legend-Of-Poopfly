import random
import time
import skatter
import text_utils
from karaktär import karaktar
from monster import monster

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

sp1 = karaktar.skapa_karaktär()

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


while True: #Hela spelloopen
    sp1.ge_stats()
    rumstyp = ['monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'rum med skatter', 'rum med skatter', 'skatterum', 'skatterum', 'bossrum', 'bossrum', 'läkerum', 'läkerum',] #lista med möjliga rumstyper. rumsantalen öker/sänker oddsen att stöta på vissa rum
    for i in range(len(sp1.inventarie)): #lägger till fällor baserat på hur många föremål spelaren har
        rumstyp.append('fällrum') 
    while len(rumstyp) > 3: #tar bort rum tills det bara är tre kvar
        rumstyp.pop(random.randint(0, len(rumstyp)-1)) 
    random.shuffle(rumstyp) #slumpar ordningen på rummen
    dorrbeskrivningar = [] #tom lista för dörrbeskrivningar
    for i in rumstyp:
        if i == 'monsterrum':
            dorrbeskrivningar.append('mörk dörr med blodfläckar...')
        elif i == 'rum med skatter':
            dorrbeskrivningar.append('trädörr med en gyllene ram...')
        elif i == 'skatterum':
            dorrbeskrivningar.append('gyllene dörr med en träram...')
        elif i == 'bossrum':
            dorrbeskrivningar.append('asstor port med en dödskalle på...')
        elif i == 'läkerum':
            dorrbeskrivningar.append('dörr med ett välkomnande ljus bakom...')
        elif i == 'fällrum':
            har_teleskop = False
            for i in sp1.inventarie: 
                if i.namn == "Teleskop": # en skatt som låter spelaren se fällor
                    har_teleskop = True
            if har_teleskop == True:
                dorrbeskrivningar.append(f'{sp1.namn} ser en gyllene dörr, men {sp1.namn + sp1.plural} teleskop låter dig se en fälla bakom...')
            else:
                falldorr = ['mörk dörr med blodfläckar...', 'trädörr med en gyllene ram...', 'gyllene dörr med en träram...', 'asstor port med en dödskalle på...', 'dörr med ett välkomnande ljus bakom...'] #standardbeskrivningar för att fylla ut listan
                dorrbeskrivningar.append(falldorr[random.randint(0, len(falldorr)-1)]) #om spelaren inte har teleskopet får de en slumpmässig beskrivning
        else:
            text_utils.slow('något har gått riktigt fel här... slut på det roliga :/') #errormeddelande som inte bör dyka upp.
    text_utils.slow(f'{sp1.namn} ser tre dörrar: \n en {dorrbeskrivningar[0]} \n en {dorrbeskrivningar[1]} \n och en {dorrbeskrivningar[2]}\n')

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        
        if val == 'R':
            if len(sp1.inventarie) < 1:
                print('Du har inga föremål')
            for i in range(len(sp1.inventarie)):
                print(f'{i+1}.{skatter.print_skatt(sp1.inventarie[i - 1])}\n')
        elif val == 'D':
            while True:
                val = input(f'Vilken dörr vill du öppna? \n [1] {dorrbeskrivningar[0]} \n [2] {dorrbeskrivningar[1]} \n [3] {dorrbeskrivningar[2]} \n [4] Avbryt \n ->')
                if val in ['1', '2', '3', '4']:
                    break
                else:
                    text_utils.slow('Ogiltigt val: välj igen') #om spelaren inte väljer ett giltigt val.
                    continue
            if val in ['1', '2', '3']: #om spelaren väljer att öppna en dörr
                text_utils.slow(f'{sp1.namn} kliver in i ett {rumstyp[int(val)-1]}\n') #rumstypen avsjöjas för spelaren
                time.sleep(1)
                break

        elif val == 'F': #printar spelarens färdigheter
            print(f'{sp1.namn + sp1.plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')

        else:
            continue
        
# RUMSTYPER OCH HÄNDELSER

    # MONSTERRUM

    if rumstyp[int(val)-1] == 'monsterrum':
        sp1.ge_stats() #uppdaterar spelarens stats en funktion
        fiende = monster.generera_monster(sp1)
        text_utils.slow(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        time.sleep(1)
        text_utils.slow(f"Den har styrkan {fiende.sty}")
        time.sleep(1)
        text_utils.slow(f"{sp1.namn}{sp1.plural} styrka är {sp1.sty}")
        time.sleep(1)

        while True: #stridssekvensen
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [M]onstret {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    if len(sp1.inventarie) < 1:
                        print('Du har inga föremål')
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{skatter.print_skatt(sp1.inventarie[i - 1])}\n')
                    print()
                elif val == 'M':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + sp1.plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')
                else:
                    continue

        if sp1.sty > fiende.sty: #kollar om spelaren vinner
            text_utils.slow(f'{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n{sp1.namn} är nu nivå {sp1.niva + 1}')
            sp1.bas_niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: #om selaren varken vinner eller förlorar
            text_utils.slow(f'Det var en svår strid, utan segrare. {sp1.namn} tar ingen skada men går inte upp en nivå. \n\n{sp1.namn} är nu nivå {sp1.niva}')
        else: #om spelaren förlorar
            slag = random.randint(1, fiende.sty) #sp1 tar skada
            text_utils.slow(f'{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade {slag} kp. \n\n{sp1.namn} är nu nivå {sp1.niva + 1}')
            sp1.skada += slag
        
        text_utils.slow(f"{sp1.namn} har {sp1.kp - sp1.skada} kp kvar.")
        time.sleep(1)

    #SKATTKAMMARE, rum att få skatter i

    elif rumstyp[int(val)-1] == 'rum med skatter': 
        tillvunnet_foremal = skatter.generera_skatt(61, 81, 96)
        mod = 'mod'
        if tillvunnet_foremal.mod_ar_mult == True:
            mod = 'mult'
        text_utils.slow('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {skatter.print_skatt(tillvunnet_foremal)}')
        time.sleep(1)
        while True:
            val = input('Vill du plocka upp den? J/N -> ').upper()
            if val == 'J':
                sp1.tilvinna_skatt(sp1, tillvunnet_foremal)
                text_utils.slow(f'{sp1.namn} plockar upp {tillvunnet_foremal.namn}')
                break
            elif val == 'N':
                text_utils.slow(f'{sp1.namn} lämmnar {tillvunnet_foremal.namn} bakom sig.')
                break
            else:
                text_utils.slow('Skriv in [J]a eller [N]ej\n')

    # SKATTERUM, rum att betala skatt i

    elif rumstyp[int(val)-1] == 'skatterum':
        text_utils.slow(f'{sp1.namn} kliver in i en mörk beskattningskammare')
        time.sleep(1)
        text_utils.slow(f'{sp1.namn} ser en dvärg i andra änden av rummet')
        time.sleep(1)
        text_utils.slow('"gadd eller kladd"\n')
        time.sleep(1)
        for i in range(len(sp1.inventarie)):
            print(f'{i+1}.{skatter.print_skatt(sp1.inventarie[i - 1])}')
        print()
        while True:
            val = input('Vad vill du betala i skatt? 1 [S]katt eller 2 [K]P ->').upper()
            if val == 'S' or val == 'K':
                break
            else:
                text_utils.slow('Du MÅSTE skriva S eller K\n')
                continue 
        if val == 'K':
            sp1.skada += 2
            text_utils.slow(f'Dvärgen drar sitt svärd och hugger {sp1.namn}\n\n{sp1.namn} har nu {sp1.kp - sp1.skada} KP kvar')
        elif len(sp1.inventarie) <= 0:
            text_utils.slow(f'{sp1.namn} har inga skatter, det får bli kladd')
            sp1.skada += 2
            text_utils.slow(f'Dvärgen drar sitt svärd och hugger {sp1.namn}\n\n{sp1.namn} har nu {sp1.kp - sp1.skada} KP kvar')
        elif val == 'S':
            text_utils.slow(sp1.avskaffa_skatt(sp1))

    #EN BOSS

    elif rumstyp[int(val)-1] == 'bossrum':
        sp1.ge_stats()
        fiende = monster.generera_boss(sp1)
        text_utils.slow(f'I ett bossrum kommer turer att utkämpas tills spelaren eller bossen är döda. Spelaren kommer bli slagen upp till bossens sty och spelaren slår upp till sin sty, mellan varje tur kan föremål användas.\n')
        time.sleep(2)
        text_utils.slow(f'Plötsligt dyker {fiende.genus} {fiende.monstertyp} upp och ger dig en fördärvande blick!\n')
        
        while fiende.kp > 0: #Du strider tills fienden eller du är död
            text_utils.slow(f'{fiende.monstertyp} gör upp till {fiende.sty} skada!!!\n')
            time.sleep(1)
            text_utils.slow(f'{fiende.monstertyp} har {fiende.kp} kp\n')
            time.sleep(1)
            while True:
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [B]ossen {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    if len(sp1.inventarie) < 1:
                        print('Du har inga föremål')
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{skatter.print_skatt(sp1.inventarie[i - 1])}\n')
                elif val == 'B':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + sp1.plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')
                else:
                    continue


            slag = random.randint(1, fiende.sty) #fiendens attack
            text_utils.slow(f'{fiende.monstertyp} {attackbeskrivning[random.randint(0, len(attackbeskrivning)-1)]} och gör {slag} skada!\n') #beskriver attacken från slumplistan attackbeskrivning
            sp1.skada += slag #spelaren tar slag skada
            time.sleep(1)
            slag = random.randint(1, sp1.sty) #sp1s attack
            text_utils.slow(f'{sp1.namn} slår {fiende.monstertyp} och gör {slag} skada\n')
            fiende.kp -= slag #fienden tar skada
            sp1.ge_stats() #kollar nivå, stats, sp1.kp och allt annat som behöver kollas varje gång det är möjligt


        text_utils.slow(f'{sp1.namn} besegrade {fiende.monstertyp}!\n') #spelaren får skatt om bossen besegras
        foremal_kvalitet = random.randint(1,100) #vikt för sällsyntare skatter
        while True:
            if foremal_kvalitet >= 51:
                if len(skatter.k4) > 0:
                    tillvunnet_foremal = skatter.k4[random.randint(0, len(skatter.k4) - 1)]
                    skatter.k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif foremal_kvalitet >= 1:
                if len(skatter.k3) > 0:
                    tillvunnet_foremal = skatter.k3[random.randint(0, len(skatter.k3) - 1)]
                    skatter.k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif foremal_kvalitet > 0:
                if len(skatter.k2) > 0:
                    tillvunnet_foremal = skatter.k2[random.randint(0, len(skatter.k2) - 1)]
                    skatter.k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif len(skatter.k1) > 0:
                tillvunnet_foremal = skatter.k1[random.randint(0, len(skatter.k1) - 1)]
                skatter.k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatter.skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
            break
        mod = 'mod'
        if skatter.skatt.mod_ar_mult == True:
            mod = 'mult'
        text_utils.slow('I skattkammaren finns det:')
        time.sleep(1)
        text_utils.slow(f'  {skatter.print_skatt(tillvunnet_foremal)}\n')
        while True:
            val = input('\n\nVill du plocka upp den? J/N ->').upper()
            if val == 'J':
                sp1.tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                text_utils.slow('Skriv in [J]a eller [N]ej\n\n')


    # LÄKERUM, spelaren helas

    elif rumstyp[int(val)-1] == 'läkerum':
        val = sp1.skada
        sp1.skada = sp1.skada - random.randint(1, sp1.kp//2) #spelaren läker mellan 1 och halva sin kp
        if sp1.skada <= 0:
            sp1.skada = 0
        text_utils.slow(f'{sp1.namn} helar {val - sp1.skada} KP\n{sp1.namn} är nu hel!\n')
        time.sleep(1)
    
    # FÄLLA, spelaren tar skada
    
    elif rumstyp[int(val)-1] == 'fällrum':
        fallskada = random.randint(0, sp1.kp//2) # Spelaren kan ta upp till halva sin kp i skada
        if fallskada == 0:
            text_utils.slow(f'OJ! {sp1.namn} klev in i en FÄLLA men undvek den, ingen skada tagen!\n\n')
        else:
            text_utils.slow(f'AJ! {sp1.namn} klev in i en FÄLLA och tog {fallskada} skada!\n\n')
            sp1.skada += fallskada #spelaren tar skada
