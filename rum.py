import random
import monster
import text_utils
import time
import karaktär
class rum:
    def __init__(self):
        self.rumstyp = 'Felaktigt rum'
    def få_dörr_beskrivning(self,spelare):
        return 'något har gått riktigt fel här... slut på det roliga :/'
    def gå_in(self,spelare):
        raise("Gick in i ett rum utan typ")
    
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
                

class monsterrum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'monsterrum'
    def få_dörr_beskrivning(self, spelare:karaktär.karaktar):
        return 'mörk dörr med blodfläckar...'
    def gå_in(self, spelare:karaktär.karaktar):
        spelare.start_tur() #uppdaterar spelarens stats en funktion
        fiende = monster.generera_monster(spelare)
        text_utils.slow(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        time.sleep(1)
        text_utils.slow(f"Den har styrkan {fiende.sty}")
        time.sleep(1)
        text_utils.slow(f"{spelare.namn}{spelare.plural} styrka är {spelare.sty}")
        time.sleep(1)

        val = ''
        while val != 'M': #stridssekvensen
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [M]onstret {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    spelare.print_inventarie()
                    print()
                elif val == 'M':
                    break
                elif val == 'F':
                    spelare.print_färdigheter()
                else:
                    continue

        if spelare.sty > fiende.sty: #kollar om spelaren vinner
            text_utils.slow(f'{spelare.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n{spelare.namn} är nu nivå {spelare.niva + 1}')
            spelare.bas_niva += 1 #spelare går upp en nivå
        elif spelare.sty == fiende.sty: #om selaren varken vinner eller förlorar
            text_utils.slow(f'Det var en svår strid, utan segrare. {spelare.namn} tar ingen skada men går inte upp en nivå. \n\n{spelare.namn} är nu nivå {spelare.niva}')
        else: #om spelaren förlorar
            slag = random.randint(1, fiende.sty) #spelare tar skada
            text_utils.slow(f'{spelare.namn} blev besegrad av {fiende.monstertyp} och förlorade {slag} kp. \n\n{spelare.namn} är nu nivå {spelare.niva + 1}')
            spelare.skada += slag
        
        text_utils.slow(f"{spelare.namn} har {spelare.kp - spelare.skada} kp kvar.")
        time.sleep(1)

class rum_med_skatter(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'rum med skatter'
    def få_dörr_beskrivning(self, spelare):
        return 'trädörr med en gyllene ram...'

class skatterum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'skatterum'
    def få_dörr_beskrivning(self, spelare):
        return 'gyllene dörr med en träram...'

class bossrum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'bossrum'
    def få_dörr_beskrivning(self, spelare):
        return 'asstor port med en dödskalle på...'

class läkerum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'läkerum'
    def få_dörr_beskrivning(self, spelare):
        return 'dörr med ett välkomnande ljus bakom...'

class fällrum(rum):
    def __init__(self):
        super().__init__()
        self.rumstyp = 'fällrum'
    def få_dörr_beskrivning(self, spelare):
        if "Teleskop" in map(lambda a: a.namn, spelare.inventarie):
            return f'{spelare.namn} ser en gyllene dörr, men {spelare.namn + spelare.plural} teleskop låter dig se en fälla bakom...'
        else:
            return random.choice(['mörk dörr med blodfläckar...', 'trädörr med en gyllene ram...', 'gyllene dörr med en träram...', 'asstor port med en dödskalle på...', 'dörr med ett välkomnande ljus bakom...'])
