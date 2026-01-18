from random import randint
from random import shuffle
import time
from skatter import skatt
from skatter import print_skatt
from skatter import k1, k2, k3, k4
from ormbarst_name_gen import von_ormbarst_namn
from collections import Counter

def slow(text, delay=0.04): #tar input i text och sekunder delay
    for char in text:
        print (char, end='', flush=True) #skriver ut et
        time.sleep(delay) #väntar delay sekunder innan nästa tecken
    print()


print('''
                                _____ _
                               |_   _| |__   ___
                                 | | | '_ \ / _ |
                                 | | | | | |  __/
                                 |_| |_| |_|\___|
             :::       :::::::::::::::::: ::::::::::::::    ::::::::::::
            :+:       :+:      :+:    :+::+:       :+:+:   :+::+:    :+:
           +:+       +:+      +:+       +:+       :+:+:+  +:++:+    +:+
          +#+       +#++:++# :#:       +#++:++#  +#+ +:+ +#++#+    +:+
         +#+       +#+      +#+   +#+#+#+       +#+  +#+#+#+#+    +#+
        #+#       #+#      #+#    #+##+#       #+#   #+#+##+#    #+#
       ############################ #############    #############
                                          __
                                    ___  / _|
                                   / _ \| |_
                                  | (_) |  _|
                                   \___/|_|
         :::::::::  ::::::::  :::::::: ::::::::: :::::::::::::    :::   :::
        :+:    :+::+:    :+::+:    :+::+:    :+::+:       :+:    :+:   :+:
       +:+    +:++:+    +:++:+    +:++:+    +:++:+       +:+     +:+ +:+
      +#++:++#+ +#+    +:++#+    +:++#++:++#+ :#::+::#  +#+      +#++:
     +#+       +#+    +#++#+    +#++#+       +#+       +#+       +#+
    #+#       #+#    #+##+#    #+##+#       #+#       #+#       #+#
   ###        ########  ######## ###       ###       #############
''')

input('Träd in i fängelshålan och ta med dig Poopfly:n på [RETUR]resan')

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew', 'gon', 'Filip', 'Holger'] 
enamn = [', den fördärvade', ' Bajs', ' McMillen', ' Döden', ' Nilsson', ' Rosencrantz', ' O´ Moriah', ' Kall', ' Von Ormbarst', ', den trosfanatiska', ', den skurna', ', den oupplysta', ', den enigmatiska', ', den godtyckliga', '']

class karaktar: #Strukturen för spelarkaraktären
    bas_kp = randint(5, 10) #Basvärde för karaktärens KP
    bas_sty = randint(25, 50)//bas_kp #Basvärde för karaktärens STY, delat på bas_kp för att balansera
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

    def ge_stats(self):
        self.kpmod = 0
        self.stymod = 0
        self.nivamod = 0
        stymult = 1
        kpmult = 1
        for i in range(len(self.inventarie)): #applicerar föremålens modifikationer på karaktären, förändringarna kommer från filen skatter.py
            if self.inventarie[i - 1].mod_ar_mult == True:
                stymult += self.inventarie[i - 1].kpmod
                kpmult += self.inventarie[i - 1].stymod
            else:
                self.kpmod += self.inventarie[i - 1].kpmod
                self.stymod += self.inventarie[i -1].stymod
                self.nivamod += self.inventarie[i - 1].nivamod
        
        self.niva = self.bas_niva + self.nivamod #spelarens totala nivå
        if self.bas_kp + self.kpmod * kpmult < 1:
                self.kp = 1
        else:
            self.kp = self.bas_kp + self.kpmod * kpmult + (self.niva * 2)
        self.sty = self.bas_sty + self.stymod * stymult + (self.niva * 2)
        
    
        if self.niva >= 10: #En check som kollar om spelaren vunnit eller förlorat varje gång det är möjligt.
            sluttid = time.time() #stoppar timern

            #Vinnst men har slut på kp samtidigt

            if self.kp - self.skada < 1:
                slow(f'{sp1.namn} springer ifrån det fasansfulla monstret men det kommer ikapp. {sp1.namn} ser en dörr på glänt i slutet av korridoren... en blå dörr...')
                time.sleep(1)
                slow(f'{sp1.namn} ser en pedistal innanför dörren, med något ovanpå...')
                time.sleep(1)
                slow(f'...kan det vara poopfly?')
                time.sleep(1)
                slow(f'{sp1.namn} hinner presis in i rummet och smäller igen dörren bakom sig... {sp1.namn} plockar upp poopfly och känner en stor glädje i sin själ...')
                time.sleep(1)
                slow('PANG', 1)
                slow(f'Monstret bakom {sp1.namn} fann en revolver någon måste ha tappat och sköt dig i ryggen igeonm dörren...')
                time.sleep(2)
                slow(f'Grattis! Du har vunnit spelet!... men till vilket pris? \n Det tog dig {int(sluttid - starttid)}')
                while True: #Liten meny där man kan kolla sina stats och föremål innan man stänger ner spelet
                    val = input('Tryck [F] för att kolla dina stats, [R] för att kolla rygsäcken eller Tryck [D] för att avsluta spelet')
                    if val == 'R': #printar inventroty
                        for i in range(len(sp1.inventarie)):
                            print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')

                    elif val == 'D': #avslutar spelet
                        quit('Vinnst??')

                    elif val == 'F': #printar spelarens färdigheter
                        print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')
                    
                    quit()

            #Vinnst!

            slow(f'{sp1.namn} finner dig framför en blå dörr')
            time.sleep(1)
            slow(f'{sp1.namn} har inget annat val än att gå in i dörren')
            time.sleep(1)
            slow(f'Kan detta vara det {sp1.namn} har letat efter hela tiden?   \nKan det vara poopfly?\n')
            time.sleep(1)
            slow(f'{sp1.namn} öppnar dörren och ser en pedestal...')
            time.sleep(1)
            slow(f'{sp1.namn + plural} haka ramlar ner i marken\n')
            slow('Herregud \n', 0.5)
            slow('är det där...?\n')
            slow('poopfly!?!?!?\n\n')
            
            time.sleep(2)
    
        #Förlust

        elif self.kp - self.skada < 1: #Om man dör printas detta
            slow(f'Du har FÖRLORAT SPELET! \n Det tog dig {int(sluttid - starttid)}')
            while True: #Liten meny där man kan kolla sina stats och föremål innan man stänger ner spelet
                val = input('Tryck [F] för att kolla dina stats, [R] för att kolla rygsäcken eller Tryck [D] för att avsluta spelet')
                if val == 'R': #printar inventroty
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')

                elif val == 'D': #avslutar spelet
                    quit('Förlust')

                elif val == 'F': #printar spelarens färdigheter
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')

        synergi_array = [] #Används för att kolla synergieffekter mellan föremål i inventarien
        for i in range(len(self.inventarie)):
            if self.inventarie[i].synergi_id != 0: #Loop sparar synergi_id:et hos alla föremål i inventariet
                synergi_array.append(self.inventarie[i].synergi_id)

        a = dict(Counter(synergi_array)) #Gör om listan till ett lexicon för enklare datahantering
        if a.get(1) == 2: #Synergi 1: ELDKASTARE
            slow(f'{sp1.namn} använder pyttelite intution och inser att om man kombinerar tändaren och sprejdeon kan hen göra en eldkastare, den lär göra ont...\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 1:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatt('Improviserad ELDKASTARE', -2, 5, 0, '"BOCKEN BRINNER!!!"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(print_skatt(self.inventarie[-1]))
        
        if a.get(2) == 2: #Synergi 2: Släpp lös det oönskade
            for p in range(2):
                slow(f'{sp1.namn} blir nyfiken till vad som igentligen finns i asken hen hittade tidigare och kommer och tänka på nyckeln hen tidigare fann\n')
                time.sleep(1)
                slow(f'{sp1.namn} rotar fram nyckeln ur packningen och märker att den har samma mönster som asken och börjar föra nyckeln mot nyckelhålet...\n')
                time.sleep(1)
                slow('...det är fasansfullt...')
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 2:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatt('Det oönskade...', -100, 30, 4, '"...borde alldrig ha öppnat asken"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(print_skatt(self.inventarie[-1]))

        if a.get(3) == 3: #Synergi 3: Dev console
            del a[3]
            slow('Tja, detta är ett medelande direkt från spelutveklarna: Eftersom att du har fått tag på alla tre minivarianter av oss kommer du nu att få ett så kallat SYNERGIföremål\n')
            time.sleep(1)
            slow('Ett SYNERGIföremål är en uppgraderad variant av flera föremål man får av att ha alla föremål av samma SYNERGI id\n')
            time.sleep(1)
            slow('Helt enkelt förklarat kommer vi att försvinna ur din ryggsäck och bytas ut mot Develpoer Console, ett föremål som är eqvivallent med och på vissa sätt överskrider de föremålen du förlorar.\n')
            time.sleep(1)
            slow('På så sätt får du mer plats för andra föremål och kan sammla på dig ännu fler föremål\n')
            time.sleep(1)
            for p in range(3):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 3:
                        self.inventarie.remove(synergi_skatt)
            if 3 not in a and len(a) != 0:
                slow('Du verkar dessutom ha några föremål på dig som har SYNERGIvarianter: ')
                for p in self.inventarie:
                    if p.synergi_id != 0:
                        print(f'{p.namn}, ')
            self.inventarie.append(skatt('Developer Console', 3, 15, 4, '"/level add 2"', 0))
            self.inventarie[-1].kvalitet = 'SYNERGI'
            print(print_skatt(self.inventarie[-1]))

        if a.get(4) == 2: #Synergi 4: 
            slow(f'Universumförstare och Helig utplånare börjar att lysa och låta från {sp1.namn + plural} väska')
            time.sleep(1)
            slow(f'{sp1.namn} plockar fram dem och ser på när de börjar slå sig samman')
            time.sleep(1)
            slow(f'{sp1.namn} blir bländad av ett starkt ljus och en blå dörr med ljusblå dörram frammanar sig framför {sp1.namn}...\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 4:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."'), 0)
            self.inventarie[-1].kvalitet = 0

        if a.get(5) == 2:
            slow(f'{sp1.namn} stöter på en mystisk man i fängelshålans gångar...')
            time.sleep(1)
            slow('"Jag heter Siv Olgor, men du kan kalla mig Revolvermannen"')
            time.sleep(1)
            slow('"Jag ser att du har hittat min ring och min gris, om du ger mig dem kan du få låna min revolver."')
            time.sleep(1)
            slow(f'Siv Olgor snarare rycker åt sig ringen från {sp1.namn + plural} hand och grisen (Lillen Spratt) från din sida och springer iväg, men som utlovat lämmnade han revolvern kvar på marken')
            time.sleep(1)
            slow(f'{sp1.namn} plockar upp den:\n')
            for p in range(2):
                for synergi_skatt in self.inventarie:
                    if synergi_skatt.synergi_id == 5:
                        self.inventarie.remove(synergi_skatt)
            self.inventarie.append(skatt('Revolver', 0, 20, 0, '"Siv Olgors revolver"', 0))
            self.inventarie[-1].kvlitet = 'SYNERGI'
            print(print_skatt(self.inventarie[-1]))
    time.sleep(1)




def avskaffa_skatt(self): #Funktion för att ta bort/byta ut ett föremål i spelarens inventarie
    output = ''
    for i in range(0, len(self.inventarie)):
        output += f'{i + 1}. {print_skatt(self.inventarie[i])}\n\n'
    print(output)
    while True:
        val = input(f'Vilken skatt i din ryggsäck vill du byta ut??->')
        if int(val) in range(1, len(self.inventarie) + 1):
            if input(f'Är du säker på att du vill byta ut {self.inventarie[int(val) - 1].namn}? J/N ->').upper() == 'J':
                slow(f'{sp1.namn} släpper sin {self.inventarie[int(val) - 1].namn}')
                self.inventarie.pop(int(val) - 1)
                return()
            else:
                slow('Skriv siffran som representerar föremålet du vill byta ut (1, 2, 3, 4, 5, 6)')

def tilvinna_skatt(self, skatt): #Funktion för att lägga till ett föremål i spelarens inventarie
    self.inventarie.append(skatt)
    if len(self.inventarie) > 5:
        avskaffa_skatt(self)




sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]}{enamn[randint(0, len(enamn)-1)]}", karaktar.bas_kp, karaktar.bas_sty, karaktar.bas_niva)#Skapar rollpersonen utifrån klassen karaktar. Skapar namn från listorna fnamn och enamn.
if sp1.namn[0] == 'g':
    sp1.namn = von_ormbarst_namn() #Speciell namn-generator för namn som börjar med g, för att få mer passande namn för Von Ormbarst

foremal_kvalitet = randint(1, 100) #Bestämmer föremåls kvalitet för evighetsföremålet
if foremal_kvalitet >= 96:
    foremal_kvalitet = k4
elif foremal_kvalitet >= 81:
    foremal_kvalitet = k3
elif foremal_kvalitet > 61:
    foremal_kvalitet = k2
else:
    foremal_kvalitet = k1

sp1.inventarie.append(foremal_kvalitet[randint(0, len(foremal_kvalitet)-1)]) #Föremålet läggs till i spelare 1s inventraie
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)
print(f'Startföremål: {sp1.inventarie[0].namn} | Kvalitet: {sp1.inventarie[0].kvalitet}\n{sp1.inventarie[0].beskrivning}\n')

if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

#RESTEN AV INTROT

slow(f'{sp1.namn} träder in genom portarna...\n')
time.sleep(1)
slow(f'Stendörrarna gnisslar mot golvet när de stängs bakom {sp1.namn}...\n')
time.sleep(1)
slow(f'{sp1.namn} tar ett djupt andetag och ser sig omkring...\n')
time.sleep(1)
slow(f'{sp1.namn} står i ett stort stenrum med tre dörrar...\n')
time.sleep(1)
slow(f'Nu söker du poopfly!\n')

#Alla våra monster:

class monster: #strukturen alla monster följer
    def __init__(monster, genus, monstertyp, sty, kp):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty
        monster.kp = kp

monsteralternativ = [ #möjliga fiender
    monster('En vild', 'Guldfisk', 1 + randint(sp1.niva, sp1.niva + 1), 1),
    monster('En vild', 'Goblin', 3 + randint(sp1.niva, sp1.niva + 8), 1),
    monster('En vild', 'Häxa', 5 + randint(sp1.niva, sp1.niva + 8), 1),
    monster('Ett vilt', 'Troll', 7 + randint(sp1.niva, sp1.niva + 14), 1),
    monster('En vild', 'Rikard', -5 + randint(sp1.niva, sp1.niva + 2), 1),
    monster('En galen', 'Blottare', 6 + randint(sp1.niva, sp1.niva + 8), 1),
    monster('En kittel', 'fladdermöss', 3 + randint(sp1.niva, sp1.niva + 14), 1)
]

bossmonsteralternativ = [ # möjliga bossar
    monster('Den store och mäktiga fritidsledaren: ', 'Mojje', randint(10, 30), sp1.niva * randint(30,50)),
    monster('Den fruktansvärt (gulliga): ', 'Bleh', randint(5,15), sp1.niva * randint(10,30)),
    monster('"Jag skulle behöva en önskan just nu..."', 'Mortecai', randint(10,20), sp1.niva * randint(20,40)),
    monster('Den', 'den', 1, 1)
]

attackbeskrivning = [f'slår {sp1.namn}', f'sparkar {sp1.namn}', f'klöser {sp1.namn} med tånaglarna', f'biter {sp1.namn}', f'slickar {sp1.namn}', 'sticker {sp1.namn}', 'krossar {sp1.namn}',] #kul beskrivning för hur spelaren attackeras.


starttid = time.time() #startar en timer för spelet


while True: #Hela spelloopen
    sp1.ge_stats()
    rumstyp = ['monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'monsterrum', 'rum med skatter', 'skatterum', 'bossrum', 'bossrum', 'läkerum'] #lista med möjliga rumstyper. rumsantalen öker/sänker oddsen att stöta på vissa rum
    for i in range(len(sp1.inventarie)): #lägger till fällor baserat på hur många föremål spelaren har
        rumstyp.append('fällrum')
    while len(rumstyp) > 3: #tar bort rum tills det bara är tre kvar
        rumstyp.pop(randint(0, len(rumstyp)-1)) 
    dorrbeskrivningar = [] #tom lista för dörrbeskrivningar
    for i in rumstyp:
        if i == 'monsterrum':
            dorrbeskrivningar.append('mörk dörr med blodfläckar...')
        elif i == 'rum med skatter':
            dorrbeskrivningar.append('trädörr med en gyllene ram...')
        elif i == 'skatterum':
            dorrbeskrivningar.append('gyllene dörr med en träram...')
        elif i == 'bossrum':
            dorrbeskrivningar.append('asstor port med en dödskalle på...')
        elif i == 'läkerum':
            dorrbeskrivningar.append('dörr med ett välkomnande ljus bakom...')
        elif i == 'fällrum':
            if 'Teleskop' in [sp1.inventarie]: # en skatt som låter spelaren se fällor
                dorrbeskrivningar.append(f'{sp1.namn} ser en gyllene dörr, men {sp1.namn + plural} teleskop låter dig se en fälla bakom...')
            else:
                falldorr = ['mörk dörr med blodfläckar...', 'trädörr med en gyllene ram...', 'gyllene dörr med en träram...', 'asstor port med en dödskalle på...', 'dörr med ett välkomnande ljus bakom...'] #standardbeskrivningar för att fylla ut listan
                dorrbeskrivningar.append(falldorr[randint(0, len(falldorr)-1)]) #om spelaren inte har teleskopet får de en slumpmässig beskrivning
        else:
            slow('något har gått riktigt fel här... slut på det roliga :/') #errormeddelande som inte bör dyka upp.
    shuffle(dorrbeskrivningar)
    slow(f'{sp1.namn} ser tre dörrar: \n en {dorrbeskrivningar[0]} \n en {dorrbeskrivningar[1]} \n och en {dorrbeskrivningar[2]}\n')

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        
        if val == 'R':
            for i in range(len(sp1.inventarie)):
                print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
        elif val == 'D':
            while True:
                val = input(f'Vilken dörr vill du öppna? \n [1] {dorrbeskrivningar[0]} \n [2] {dorrbeskrivningar[1]} \n [3] {dorrbeskrivningar[2]} \n [4] Avbryt \n ->')
                if val in ['1', '2', '3', '4']:
                    break
                else:
                    slow('Ogiltigt val: välj igen') #om spelaren inte väljer ett giltigt val.
                    continue
            if val in ['1', '2', '3']: #om spelaren väljer att öppna en dörr
                slow(f'{sp1.namn} kliver in i ett {rumstyp[int(val)-1]}\n') #rumstypen avsjöjas för spelaren
                time.sleep(1)
                break

        elif val == 'F': #printar spelarens färdigheter
            print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')

        else:
            continue
        
# RUMSTYPER OCH HÄNDELSER

    # MONSTERRUM

    if rumstyp[int(val)-1] == 'monsterrum':
        sp1.ge_stats() #uppdaterar spelarens stats en funktion
        fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
        slow(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        time.sleep(1)
        slow(f"Den har styrkan {fiende.sty}")
        time.sleep(1)
        slow(f"{sp1.namn}{plural} styrka är {sp1.sty}")
        time.sleep(1)

        while True: #stridssekvensen
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [M]onstret {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}\n')
                elif val == 'M':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')
                else:
                    continue

        if sp1.sty > fiende.sty: #kollar om spelaren vinner
            slow(f'{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n')
            sp1.bas_niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: 
            slow(f'Det var en svår strid, utan segrare. {sp1.namn} tar ingen skada men går inte upp en nivå. \n')
        else: #om selaren varken vinner 
            slow(f'{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade 1 kp. \n')
            sp1.skada += 1

        time.sleep(1)

        slow(f"{sp1.namn} har {sp1.kp - sp1.skada} kp kvar.")
        time.sleep(1)
        slow(f"{sp1.namn} är nivå {sp1.niva}.")
    
    #SKATTKAMMARE, rum att få skatter i

    elif rumstyp[int(val)-1] == 'rum med skatter': 
        foremal_kvalitet = randint(1, 100)
        while True:
            if foremal_kvalitet >= 96:
                if len(k4) > 0:
                    tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
                    k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 81
                    continue
            elif foremal_kvalitet >= 81:
                if len(k3) > 0:
                    tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
                    k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 61
                    continue
            elif foremal_kvalitet > 61:
                if len(k2) > 0:
                    tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
                    k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif len(k1) > 0:
                tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
                k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."', 0)
            break
        mod = 'mod'
        if skatt.mod_ar_mult == True:
            mod = 'mult'
        slow('I skattkammaren finns det:\n')
        time.sleep(1)
        print(f'  {print_skatt(tillvunnet_foremal)}')
        while True:
            val = input('Vill du plocka upp den? J/N ->').upper()
            if val == 'J':
                tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                slow('Skriv in [J]a eller [N]ej')

    # SKATTERUM, rum att betala skatt i

    elif rumstyp[int(val)-1] == 'skatterum':
        slow(f'{sp1.namn} kliver in i en mörk beskattningskammare')
        time.sleep(1)
        slow(f'{sp1.namn} ser en dvärg i andra änden av rummet')
        time.sleep(1)
        slow('"gadd eller kladd"\n\n')
        time.sleep(1)
        for i in range(len(sp1.inventarie)):
                print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}')
        while True:
            val = input('Vad vill du betala i skatt? 1 [S]katt eller 2 [K]P ->').upper()
            if val == 'S' or val == 'K':
                break
            else:
                slow('Du MÅSTE skriva S eller K\n')
                continue 
        if val == 'K':
            sp1.skada += 2
        elif val == 'S':
            avskaffa_skatt(sp1)

    #EN BOSS

    elif rumstyp[int(val)-1] == 'bossrum':
        sp1.ge_stats()
        fiende = bossmonsteralternativ[randint(0, len(bossmonsteralternativ)-1)]
        slow(f'I ett bossrum kommer turer att utkämpas tills spelaren eller bossen är döda, eller spelaren lyckas fly. Spelaren kommer bli slagen upp till bossens sty och spelaren slår upp till sin sty, mellan varje tur kan föremål användas.\n')
        time.sleep(2)
        slow(f'Plötsligt dyker {fiende.genus} {fiende.monstertyp} upp och ger dig en fördärvande blick!\n')
        
        while fiende.kp > 0:
            slow(f'{fiende.monstertyp} gör upp till {fiende.sty} skada!!!\n')
            time.sleep(1)
            slow(f'{fiende.monstertyp} har {fiende.kp} kp\n')
            time.sleep(1)
            while True:
                val = input(f'''Vad vill du göra?
                                Kolla [R]yggsäcken
                                Slå mot [B]ossen {fiende.monstertyp}
                                Kolla [F]ärdigheter 
                                -> ''').upper()
                if val == 'R':
                    for i in range(len(sp1.inventarie)):
                        print(f'{i+1}.{print_skatt(sp1.inventarie[i - 1])}\n')
                elif val == 'B':
                    break
                elif val == 'F':
                    print(f'{sp1.namn + plural} färdigheter:\n  Nivå: {sp1.niva} | KP: {sp1.kp} / {sp1.kp + sp1.skada} | STY: {sp1.sty}\n')
                else:
                    continue


            slag = randint(1, fiende.sty)
            slow(f'{fiende.monstertyp} {attackbeskrivning[randint(0, len(attackbeskrivning)-1)]} och gör {slag} skada!\n')
            sp1.skada += slag
            time.sleep(1)
            slag = randint(1, sp1.sty)
            slow(f'{sp1.namn} slår {fiende.monstertyp} och gör {slag} skada\n')
            fiende.kp -= slag
            sp1.ge_stats()

        slow(f'{sp1.namn} besegrade {fiende.monstertyp}!\n')
        foremal_kvalitet = randint(1,100)
        while True:
            if foremal_kvalitet >= 51:
                if len(k4) > 0:
                    tillvunnet_foremal = k4[randint(0, len(k4) - 1)]
                    k4.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 1
                    continue
            elif foremal_kvalitet >= 1:
                if len(k3) > 0:
                    tillvunnet_foremal = k3[randint(0, len(k3) - 1)]
                    k3.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif foremal_kvalitet > 0:
                if len(k2) > 0:
                    tillvunnet_foremal = k2[randint(0, len(k2) - 1)]
                    k2.remove(tillvunnet_foremal)
                    break
                else:
                    foremal_kvalitet = 0
                    continue
            elif len(k1) > 0:
                tillvunnet_foremal = k1[randint(0, len(k1) - 1)]
                k1.remove(tillvunnet_foremal)
            else:
                tillvunnet_foremal = skatt('Poopfly', -100, -100, 10, '"Wow, den suger verkligen mer än vad jag trodde..."')
            break
        mod = 'mod'
        if skatt.mod_ar_mult == True:
            mod = 'mult'
        slow('I skattkammaren finns det:')
        time.sleep(1)
        slow(f'  {print_skatt(tillvunnet_foremal)}\n')
        while True:
            val = input('\nVill du plocka upp den? J/N ->').upper()
            if val == 'J':
                tilvinna_skatt(sp1, tillvunnet_foremal)
                break
            elif val == 'N':
                break
            else:
                slow('Skriv in [J]a eller [N]ej\n\n')

    # LÄKERUM, spelaren helas

    elif rumstyp[int(val)-1] == 'läkerum': 
        sp1.skada = sp1.skada - randint(1, sp1.kp//2) #spelaren läker mellan 1 och halva sin kp
        if sp1.skada <= 0:
            sp1.skada = 0
        slow(f'{sp1.namn} är nu hel!\n\n')
    
    # FÄLLA, spelaren tar skada
    
    elif rumstyp[int(val)-1] == 'fällrum':
        fallskada = randint(0, sp1.kp//2) # Spelaren kan ta upp till halva sin kp i skada
        if fallskada == 0:
            slow(f'OJ! {sp1.namn} klev in i en FÄLLA men undvek den, ingen skada tagen!\n\n')
        else:
            slow(f'AJ! {sp1.namn} klev in i en FÄLLA och tog {fallskada} skada!\n\n')
            sp1.skada += fallskada