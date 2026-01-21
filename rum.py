import random

class rum:
    def __init__(self):
        self.rumstyp = 'Felaktigt rum'
    def få_dörr_beskrivning(self,spelare):
        return 'något har gått riktigt fel här... slut på det roliga :/'
    
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
    def få_dörr_beskrivning(self, spelare):
        return 'mörk dörr med blodfläckar...'

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
