from rum import rum
import text_utils
import time
from monster import monster
import karaktär
import random

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