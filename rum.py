import random
import monster
import text_utils
import time
import karaktär
import skatter
from monsterrum import monsterrum
class rum:
    def __init__(self):
        self.rumstyp = 'Felaktigt rum'
    def få_dörr_beskrivning(self,spelare):
        return 'något har gått riktigt fel här... slut på det roliga :/'
    def gå_in(self,spelare):
        raise("Gick in i ett rum utan typ")
    def få_attackbeskrivning(spelare):
        return random.choice([f'slår {spelare.namn}', f'sparkar {spelare.namn}', f'klöser {spelare.namn} med tånaglarna', f'biter {spelare.namn}', f'slickar {spelare.namn}', f'sticker {spelare.namn}', f'krossar {spelare.namn}',]) #kul beskrivning för hur spelaren attackeras.
    
    def generera(spelare) -> list:
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
                



class rum_med_skatter(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'rum med skatter'
    def få_dörr_beskrivning(self, spelare):
        return 'trädörr med en gyllene ram...'
    def gå_in(self, spelare):
        tillvunnet_foremal = skatter.generera_skatt(61, 81, 96)
        text_utils.slow('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {skatter.print_skatt(tillvunnet_foremal)}')
        time.sleep(1)
        while True:
            val = input('Vill du plocka upp den? J/N -> ').upper()
            if val == 'J':
                spelare.tilvinna_skatt(tillvunnet_foremal)
                text_utils.slow(f'{spelare.namn} plockar upp {tillvunnet_foremal.namn}')
                break
            elif val == 'N':
                text_utils.slow(f'{spelare.namn} lämmnar {tillvunnet_foremal.namn} bakom sig.')
                break
            else:
                text_utils.slow('Skriv in [J]a eller [N]ej\n')

class skatterum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'skatterum'
    def få_dörr_beskrivning(self, spelare):
        return 'gyllene dörr med en träram...'
    def gå_in(self, spelare:karaktär.karaktar):
        text_utils.slow(f'{spelare.namn} kliver in i en mörk beskattningskammare')
        time.sleep(1)
        text_utils.slow(f'{spelare.namn} ser en dvärg i andra änden av rummet')
        time.sleep(1)
        text_utils.slow('"gadd eller kladd"\n')
        time.sleep(1)
        spelare.print_inventarie()
        print()
        while True:
            val = input('Vad vill du betala i skatt? 1 [S]katt eller 2 [K]P ->').upper()
            if val == 'S' or val == 'K':
                break
            else:
                text_utils.slow('Du MÅSTE skriva S eller K\n')
                continue 
        if val == 'K':
            spelare.skada += 2
            text_utils.slow(f'Dvärgen drar sitt svärd och hugger {spelare.namn}\n\n{spelare.namn} har nu {spelare.kp - spelare.skada} KP kvar')
        elif len(spelare.inventarie) <= 0:
            text_utils.slow(f'{spelare.namn} har inga skatter, det får bli kladd')
            spelare.skada += 2
            text_utils.slow(f'Dvärgen drar sitt svärd och hugger {spelare.namn}\n\n{spelare.namn} har nu {spelare.kp - spelare.skada} KP kvar')
        elif val == 'S':
            text_utils.slow(spelare.avskaffa_skatt())

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


class läkerum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'läkerum'
    def få_dörr_beskrivning(self, spelare):
        return 'dörr med ett välkomnande ljus bakom...'
    def gå_in(self, spelare):
        val = spelare.skada
        spelare.skada = spelare.skada - random.randint(1, spelare.kp//2) #spelaren läker mellan 1 och halva sin kp
        if spelare.skada <= 0:
            spelare.skada = 0
        text_utils.slow(f'{spelare.namn} helar {val - spelare.skada} KP\n{spelare.namn} är nu hel!\n')
        time.sleep(1)

class fällrum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'fällrum'
    def få_dörr_beskrivning(self, spelare):
        if "Teleskop" in map(lambda a: a.namn, spelare.inventarie):
            return f'{spelare.namn} ser en gyllene dörr, men {spelare.namn + spelare.plural} teleskop låter dig se en fälla bakom...'
        else:
            return random.choice(['mörk dörr med blodfläckar...', 'trädörr med en gyllene ram...', 'gyllene dörr med en träram...', 'asstor port med en dödskalle på...', 'dörr med ett välkomnande ljus bakom...'])
    def gå_in(self, spelare):
        fallskada = random.randint(0, spelare.kp//2) # Spelaren kan ta upp till halva sin kp i skada
        if fallskada == 0:
            text_utils.slow(f'OJ! {spelare.namn} klev in i en FÄLLA men undvek den, ingen skada tagen!\n\n')
        else:
            text_utils.slow(f'AJ! {spelare.namn} klev in i en FÄLLA och tog {fallskada} skada!\n\n')
            spelare.skada += fallskada #spelaren tar skada