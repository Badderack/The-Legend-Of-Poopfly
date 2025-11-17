class skatt:
    def __init__(skatt, namn, kvalitet, kpmod, stymod, nivamod, beskrivning):
        skatt.namn = namn
        skatt.kvalitet = kvalitet
        skatt.kpmod = kpmod
        skatt.stymod = stymod
        skatt.nivamod = nivamod
        skatt.beskrivning = beskrivning

# skatt('NAMN', kvalitet, kp modifier, sty modifier, niva modifier, '"Beskrivning"')
#Kvalitet 1 föremål
teleskop = skatt('Teleskop', 1, 0, 0, 0, '"Ökad sikt"')
spade = skatt('Spade', 1, 0, 1, 0, '"Gräva gräva hål!"')
#Kvalitet 2 föremål

#Kvalitet 3 föremål

#Kvalitet 4 föremål
holy_obliterator = skatt('Helig utplånare', 4, 0, 10, 1, '"Hellre detta än "Universumsförstörare""')
universe_destroyer = skatt('Universumförstare', 4, 10, 0, 1, '"Hellre detta än "Helig utplånare""')