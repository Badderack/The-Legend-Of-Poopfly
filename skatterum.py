import text_utils
import time
from rum import rum
import karaktär

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