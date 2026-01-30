from rum import rum
import text_utils
from monster import monster
import time
import skatter

import random
class bossrum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'bossrum'
    def få_dörr_beskrivning(self, spelare):
        return 'asstor port med en dödskalle på...'
    def gå_in(self, spelare):
        spelare.start_tur()
        fiende = monster.generera_boss(spelare)
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
                    if len(spelare.inventarie) < 1:
                        print('Du har inga föremål')
                    for i in range(len(spelare.inventarie)):
                        print(f'{i+1}.{skatter.print_skatt(spelare.inventarie[i - 1])}\n')
                elif val == 'B':
                    break
                elif val == 'F':
                    print(f'{spelare.namn + spelare.plural} färdigheter:\n  Nivå: {spelare.niva} | KP: {spelare.kp} / {spelare.kp + spelare.skada} | STY: {spelare.sty}\n')
                else:
                    continue


            slag = random.randint(1, fiende.sty) #fiendens attack
            text_utils.slow(f'{fiende.monstertyp} {self.få_attackbeskrivning()} och gör {slag} skada!\n') #beskriver attacken från slumplistan attackbeskrivning
            spelare.skada += slag #spelaren tar slag skada
            time.sleep(1)
            slag = random.randint(1, spelare.sty) #spelares attack
            text_utils.slow(f'{spelare.namn} slår {fiende.monstertyp} och gör {slag} skada\n')
            fiende.kp -= slag #fienden tar skada
            spelare.start_tur() #kollar nivå, stats, spelare.kp och allt annat som behöver kollas varje gång det är möjligt
        
        
        text_utils.slow(f'{spelare.namn} besegrade {fiende.monstertyp}!\n') #spelaren får skatt om bossen besegras
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
                spelare.tilvinna_skatt(tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                text_utils.slow('Skriv in [J]a eller [N]ej\n\n')