import random
import monster
import text_utils
import time
import karaktär
import skatter
from monsterrum import monsterrum
from rum_med_skatter import rum_med_skatter
from skatterum import skatterum
from bossrum import bossrum
from läkerum import läkerum
from fällrum import fällrum

class rum:
    def __init__(self):
        self.rumstyp = 'Felaktigt rum'
    def få_dörr_beskrivning(self,spelare):
        return 'något har gått riktigt fel här... slut på det roliga :/'
    def gå_in(self,spelare):
        raise("Gick in i ett rum utan typ")
    def få_attackbeskrivning(spelare):
        return random.choice([f'slår {spelare.namn}', f'sparkar {spelare.namn}', f'klöser {spelare.namn} med tånaglarna', f'biter {spelare.namn}', f'slickar {spelare.namn}', f'sticker {spelare.namn}', f'krossar {spelare.namn}',]) #kul beskrivning för hur spelaren attackeras.
    
