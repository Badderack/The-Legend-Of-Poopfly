from random import randint
class skatt:
    kvalitet = 1
    mod_ar_mult = False
    def __init__(skatt, namn, kpmod, stymod, nivamod, beskrivning, synergi_id):
        skatt.namn = namn
        skatt.kpmod = kpmod
        skatt.stymod = stymod
        skatt.nivamod = nivamod
        skatt.beskrivning = beskrivning
        skatt.synergi_id = synergi_id

def print_skatt(sak):
    mod = 'mod'
    if sak.mod_ar_mult == True:
        mod = 'mult'
    output = f' {sak.namn} | Kvalitet: {sak.kvalitet}\n  {sak.beskrivning}\n   KP {mod}: {sak.kpmod} | STY {mod}: {sak.stymod} | Nivå mod {sak.nivamod}'
    return(output)

# skatt('NAMN', kp modifier, sty modifier, niva modifier, '"Beskrivning"')
#Kvalitet 1 föremål
k1 = [
skatt('Teleskop', 0, 0, 0, '"Ökad sikt"', 0),
skatt('Spade', 0, 1, 0, '"Gräva gräva hål!"',0),
skatt('Nagelfil', 0, 2, 0, '"Skönhet dödar!"',0),
skatt('Tändare', 0, 1, 0, '"Hmmm. Jag undrar om dem kan brinna..."', 1),
skatt('Spraydeoderant', 1, 0, 0, '"Teknikelevernas mardröm"', 1),
skatt('Gambeson', 2, 0, 0, '"En fint kviltad linrustning"', 0)
]

#Kvalitet 2 föremål
k2 = [
skatt('Raket i en burk', -1, 2, 0, '"Jag förstår inte riktigt hur man fick in den..."', 0),
skatt('Pandoras ask', randint(-2, 4), randint(-5, 5), randint(0, 1), '"Slumpmässig egenskapsförändring"', 2),
skatt('Ringbrynja', 3, 0, 0, '"En nitad ringbrynja"', 0),
skatt('Sabel', 0, 3, 0, '"Läderlindat handtag och ett skarpt blad"', 0),
skatt('Kofot', 0, 3, 0, '"Muuuuuu..."', 0),
skatt('Nyckel', 0, 0, 0, '"Släpp lös det oönskade"', 2)
]
for i in k2: 
    i.kvalitet = 2 #Ger alla items i listan k2 kvalitetvärde 2

#Kvalitet 3 föremål
k3 = [
skatt('Sten', -1, 5, 0, '"Hur kan en sten gråta?!"', 0),
skatt('Schweizisk armékniv', 0, 6, 0, "Undrar varför pappor älskar såna..", 0),
skatt('Ring', 2, 2, 1, '"Det är ju jag!" - Alwin Ring \n "En skapades för att styra alla"', 5),
skatt('Liten Anton', 1, 5, 1, '"Minibassist i Ormbarst"', 3),
skatt('Liten Ludvig',1, 5, 1, '"Minigitarrist i Ormbarst"', 3),
skatt('Liten Lizi', 1, 5, 1, '"Mini day one till Ormbarst"', 3),
skatt('Minikit', 0, 4, 2, '"Lego Curinirs stolthet"', 0)
]
for i in k3:
    i.kvalitet = 3 #Ger alla items i listan k3 kvalitetvärde 3

#Kvalitet 4 föremål
k4 = [
skatt('Helig utplånare', 1, 2, 1, '"Hellre detta än Universumsförstörare"', 4),
skatt('Universumförstare', 2, 1, 1, '"Hellre detta än Helig utplånare"', 4),
skatt('Glasögon', 1.6, 1.6, -1, '"20/20 syn... minus erfarenhet"', 0),
skatt('Lillens spratt', 1, 2, 0, '"Bam bam!"', 5)
]
for i in k4:
    i.kvalitet = 4 #Ger alla items i listan k4 kvalitetvärde 4
    i.mod_ar_mult = True
