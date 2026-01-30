import random, time, collections
import text_utils
import skatter
import ormbarst_name_gen
import vinnst_förlust
class karaktar: #Strukturen för spelarkaraktären
    bas_kp = random.randint(5, 10) #Basvärde för karaktärens KP
    bas_sty = random.randint(25, 50)//bas_kp #Basvärde för karaktärens STY, delat på bas_kp för att balansera
    bas_niva = 0
    kpmod = 0
    stymod = 0
    nivamod = 0
    skada = 0
    inventarie = []
    def __init__(self, namn, kp, sty, niva):
        self.namn = namn
        self.kp = kp
        self.sty = sty
        self.niva = niva
        self.starttid = 0
        self.plural = "" if self.namn[-1] == 's' else "s" # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    
    def print_färdigheter(self):
        print(f"""{self.namn + self.plural} färdigheter:
Nivå: {self.niva} | KP: {self.kp} / {self.kp + self.skada} | STY: {self.sty}
""")
    def print_inventarie(self):
        if len(self.inventarie) < 1:
            print('Du har inga föremål')
        for i, skatt in enumerate(self.inventarie):
            print(f'{i+1}.{str(skatt)}\n')
        
    def start_tur(self):
        self.ge_stats()
        self.kolla_vinst_förlust()


    def ge_stats(self):
        self.kpmod = 0
        self.stymod = 0
        self.nivamod = 0
        stymult = 1
        kpmult = 1
        for i in range(len(self.inventarie)): #applicerar föremålens modifikationer på karaktären, förändringarna kommer från filen skatter.py
            if self.inventarie[i].mod_ar_mult == True:
                stymult += self.inventarie[i].stymod
                kpmult += self.inventarie[i].kpmod
            else:
                self.kpmod += self.inventarie[i].kpmod
                self.stymod += self.inventarie[i].stymod
                self.nivamod += self.inventarie[i].nivamod
        
        self.niva = self.bas_niva + self.nivamod #spelarens totala nivå
        if self.bas_kp + self.kpmod * kpmult < 1:
                self.kp = 1
        else:
            self.kp = (self.bas_kp + self.kpmod) * kpmult + (self.niva * 2)
        self.sty = (self.bas_sty + self.stymod) * stymult + (self.niva * 2)
        
    def kolla_vinst_förlust(self):
        if self.niva >= 10: #En check som kollar om spelaren vunnit eller förlorat varje gång det är möjligt.
            
            vinnst_förlust.vinn(self)
            

        elif self.kp - self.skada < 1: #Om man dör printas detta

            vinnst_förlust.förlust(self)
            

        synergi_array = [] #Används för att kolla synergieffekter mellan föremål i inventarien
        for i in range(len(self.inventarie)):
            if self.inventarie[i].synergi_id != 0: #Loop sparar synergi_id:et hos alla föremål i inventariet
                synergi_array.append(self.inventarie[i].synergi_id)

        a = dict(collections.Counter(synergi_array)) #Gör om listan till ett lexicon för enklare datahantering
        if a.get(1) == 2: #Synergi 1: ELDKASTARE
            text_utils.slow(f'{self.namn} använder pyttelite intution och inser att om man kombinerar tändaren och sprejdeon kan hen göra en eldkastare, den lär göra ont...\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 1:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatter.skatt('Improviserad ELDKASTARE', -2, 5, 0, '"BOCKEN BRINNER!!!"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(str(self.inventarie[-1]))
        
        if a.get(2) == 2: #Synergi 2: Släpp lös det oönskade
            for p in range(2):
                text_utils.slow(f'{self.namn} blir nyfiken till vad som igentligen finns i asken hen hittade tidigare och kommer och tänka på nyckeln hen tidigare fann\n')
                time.sleep(1)
                text_utils.slow(f'{self.namn} rotar fram nyckeln ur packningen och märker att den har samma mönster som asken och börjar föra nyckeln mot nyckelhålet...\n')
                time.sleep(1)
                text_utils.slow('...det är fasansfullt...')
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 2:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatter.skatt('Det oönskade...', -100, 30, 4, '"...borde alldrig ha öppnat asken"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(str(self.inventarie[-1]))

        if a.get(3) == 3: #Synergi 3: Dev console
            del a[3]
            text_utils.slow('Tja, detta är ett medelande direkt från spelutveklarna: Eftersom att du har fått tag på alla tre minivarianter av oss kommer du nu att få ett så kallat SYNERGIföremål\n')
            time.sleep(1)
            text_utils.slow('Ett SYNERGIföremål är en uppgraderad variant av flera föremål man får av att ha alla föremål av samma SYNERGI id\n')
            time.sleep(1)
            text_utils.slow('Helt enkelt förklarat kommer vi att försvinna ur din ryggsäck och bytas ut mot Develpoer Console, ett föremål som är eqvivallent med och på vissa sätt överskrider de föremålen du förlorar.\n')
            time.sleep(1)
            text_utils.slow('På så sätt får du mer plats för andra föremål och kan sammla på dig ännu fler föremål\n')
            time.sleep(1)
            for p in range(3):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 3:
                        self.inventarie.remove(synergi_skatt)
            if 3 not in a and len(a) != 0:
                text_utils.slow('Du verkar dessutom ha några föremål på dig som har SYNERGIvarianter: ')
                for p in self.inventarie:
                    if p.synergi_id != 0:
                        print(f'{p.namn}, ')
            self.inventarie.append(self.skatt('Developer Console', 3, 15, 4, '"/level add 2"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(self.print_skatt(self.inventarie[-1]))

        if a.get(4) == 2: #Synergi 4: 
            text_utils.slow(f'Universumförstare och Helig utplånare börjar att lysa och låta från {self.namn + self.plural} väska')
            time.sleep(1)
            text_utils.slow(f'{self.namn} plockar fram dem och ser på när de börjar slå sig samman')
            time.sleep(1)
            text_utils.slow(f'{self.namn} blir bländad av ett starkt ljus och en blå dörr med ljusblå dörram frammanar sig framför {self.namn}...\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 4:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatter.skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."'), 0)
            self.inventarie[-1].kvalitet = 0

        if a.get(5) == 2:
            text_utils.slow(f'{self.namn} stöter på en mystisk man i fängelshålans gångar...')
            time.sleep(1)
            text_utils.slow('"Jag heter Siv Olgor, men du kan kalla mig Revolvermannen"')
            time.sleep(1)
            text_utils.slow('"Jag ser att du har hittat min ring och min gris, om du ger mig dem kan du få låna min revolver."')
            time.sleep(1)
            text_utils.slow(f'Siv Olgor snarare rycker åt sig ringen från {self.namn + self.plural} hand och grisen (Lillen Spratt) från din sida och springer iväg, men som utlovat lämmnade han revolvern kvar på marken')
            time.sleep(1)
            text_utils.slow(f'{self.namn} plockar upp den:\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 5:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatter.skatt('Revolver', 0, 20, 0, '"Siv Olgors revolver"', 0))
            self.inventarie[-1].kvlitet = 'SYNERGI'
            print(str(self.inventarie[-1]))
    time.sleep(1)
    
    def avskaffa_skatt(self): #Funktion för att ta bort/byta ut ett föremål i spelarens inventarie
        output = ''
        self.print_inventarie() 
        print(output)
        while True:
            val = input(f'Vilken skatt i din ryggsäck vill du byta ut??->')
            if val.isdigit():
                if int(val) in range(1, len(self.inventarie) + 1):
                    if input(f'Är du säker på att du vill byta ut {self.inventarie[int(val) - 1].namn}? J/N ->').upper() == 'J':
                        text_utils.slow(f'{self.namn} släpper sin {self.inventarie[int(val) - 1].namn}')
                        skatt_namn = {self.inventarie[int(val) - 1].namn}
                        self.inventarie.pop(int(val) - 1)
                        return(skatt_namn)
            text_utils.slow('Skriv siffran som representerar föremålet du vill byta ut (1, 2, 3, 4, 5, 6)')

    def tilvinna_skatt(self, skatt): #Funktion för att lägga till ett föremål i spelarens inventarie
        self.inventarie.append(skatt)
        if len(self.inventarie) > 5:
            self.avskaffa_skatt()

    def skapa_karaktär():
        fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', 'gon', 'gon', 'gon', 'Filip', 'Holger', 'Oskar'] 
        enamn = [', den fördärvade', ' Bajs', ' McMillen', ' Döden', ' Nilsson', ' Rosencrantz', ' O´ Moriah', ' Kall', ' Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oupplysta', ', den enigmatiska', ', den godtyckliga', '']
        
        #Skapar rollpersonen utifrån klassen karaktar. Skapar namn från listorna fnamn och enamn.
        sp1 = karaktar(f"{fnamn[random.randint(0, len(fnamn)-1)]}{enamn[random.randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva)

        #Speciell namn-generator för namn som börjar med g, för att få mer passande namn för Von Ormbarst
        if sp1.namn[0] == 'g':
            sp1.namn = ormbarst_name_gen.von_ormbarst_namn()

        #Genererar en skatt att börja med 60% chans för kvalitet 1, 20 för k2, 16% för k3 och 3% för k4 (starting item)
        sp1.inventarie.append(skatter.generera_skatt(61, 81, 97)) 

        return sp1
