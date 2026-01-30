import text_utils
import time
from rum import rum
import skatter

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
        print(f'  {str(tillvunnet_foremal)}')
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