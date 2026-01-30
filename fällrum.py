from rum import rum
import random
import text_utils

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