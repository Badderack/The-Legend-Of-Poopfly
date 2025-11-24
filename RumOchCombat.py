from random import randint
import time

fnamn = ['Isak', 'Pelle', 'Ludvig', 'Anton', 'Lizi', 'Edmund', 'Bertholowmew']
enamn = ['den fördärvade', 'Bajs', 'McMillen', 'Döden', 'O´ Moriah', 'Kall']

class karaktar:
    def __init__(karaktar, namn, kp, sty, niva, inventarie):
        karaktar.namn = namn
        karaktar.kp = kp
        karaktar.sty = sty
        karaktar.niva = niva
        karaktar.inventarie = inventarie

tempkp = randint(1, 5)
tempsty = randint(5, 15)//tempkp

sp1 = karaktar(f"{fnamn[randint(0, len(fnamn)-1)]} {enamn[randint(0, len(enamn)-1)]}", tempkp, tempsty, 0, [])
print(sp1.namn)
print('KP:', sp1.kp)
print('STY', sp1.sty)

if sp1.namn[-1] == 's': # Kollar om spelarens namn slutar på s, och följer gramatikregler för plural
    plural = ""
else:
    plural = "s"

class monster: #strukturen alla monster följer
    def __init__(monster, genus, monstertyp, sty):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty

monsteralternativ = [ #möjliga fiender
    monster('En vild', 'Guldfisk', 2),
    monster('En vild', 'Goblin', 4),
    monster('En vild', 'Häxa', 6),
    monster('Ett vilt', 'Troll', 8),
    monster('En vild', 'Rikard', 10),
]



while True: #Hela spelloopen
    rumstyp = ['monsterrum', 'skattkammare', 'skatterum', 'bossrum', 'Läkerum']
    while len(rumstyp) > 3:
        rumstyp.pop(randint(0, len(rumstyp)-1))
    print(f"{sp1.namn} ser tre dörrar {rumstyp}.")

    while True: #meny innan strid
        val = input('''Vad vill du göra?
                    Kolla [R]yggsäcken
                    Öppna en [D]örr
                    Kolla [F]ärdigheter 
                    -> ''').upper()
        
        if val == 'R':
            for i in range(len(sp1.inventarie)):
                print(f'{i+1}. {sp1.inventarie[i - 1].namn} | Kvalitet: {sp1.inventarie[i - 1].kvalitet}\n{sp1.inventarie[i - 1].beskrivning}\nKP')
        elif val == 'D': #Val för att öppna dörrar

            while True:
                vald_dorr = input(f'vilken dörr vill du öppna? \n [1] {rumstyp[0]} \n [2] {rumstyp[1]} \n [3] {rumstyp[2]} \n [4] Avbryt \n ->')
                if vald_dorr in ['1', '2', '3', '4']:
                    break
                else:
                    print('ogiltigt val, välj igen')
            break

        elif vald_dorr in ['1', '2', '3']:   
            print(f'{sp1.namn} kliver in i ett {rumstyp[int(vald_dorr)-1]}')
            break
        elif vald_dorr == '4':
            continue
            

        elif val == 'F':
            print('F')
        else:
            continue
    
        print('Här kommer rumsinnehåll i form av en funktion tror jag :)\n\n') 

        fiende = monsteralternativ[randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum
        print(f"{fiende.genus} {fiende.monstertyp} dyker upp!")
        print(f"Den har styrkan {fiende.sty}")
        print(f"{sp1.namn}{plural} styrka är {sp1.sty}")

        time.sleep(0.5)

        (input("här kommer du få fatta beslut, men inte riktigt än :/ (skriv något och tryck enter) \n\n"))


        if sp1.sty > fiende.sty: #kollar vem som vinner
            print(f"{sp1.namn} besegrade {fiende.monstertyp} och gick upp en nivå! \n\n")
            sp1.niva += 1 #sp1 går upp en nivå
        elif sp1.sty == fiende.sty: 
            print(f"Det var en svår strid, utan wiener. Du tar ingen skada men går inte upp en nivå. \n\n")
        else:
            print(f"{sp1.namn} blev besegrad av {fiende.monstertyp} och förlorade 1 kp. \n\n")
            sp1.kp -= 1

        time.sleep(0.5)

        print(f"{sp1.namn} har {sp1.kp} kp kvar.")
        print(f"{sp1.namn} är nivå {sp1.niva}.")
        print(f"{sp1.namn} har styrketalet {sp1.sty}.")
    else:
        print('inte implementerat än \n\n')
        continue

