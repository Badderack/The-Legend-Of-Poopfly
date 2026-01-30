from rum import rum
import random
import text_utils
import time

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