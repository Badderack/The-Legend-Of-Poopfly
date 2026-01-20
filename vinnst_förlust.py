import text_utils
import time
import skatter
def vinn(spelare):
    #Vinnst men har slut på kp samtidigt
    sluttid = time.time() #stoppar timern

    if spelare.kp - spelare.skada < 1:
        text_utils.slow(f'{spelare.namn} springer ifrån det fasansfulla monstret men det kommer ikapp. {spelare.namn} ser en dörr på glänt i slutet av korridoren... en blå dörr...')
        time.sleep(1)
        text_utils.slow(f'{spelare.namn} ser en pedistal innanför dörren, med något ovanpå...')
        time.sleep(1)
        text_utils.slow(f'...kan det vara poopfly?')
        time.sleep(1)
        text_utils.slow(f'{spelare.namn} hinner presis in i rummet och smäller igen dörren bakom sig... {spelare.namn} plockar upp poopfly och känner en stor glädje i sin själ...')
        time.sleep(1)
        text_utils.slow('PANG', 1)
        text_utils.slow(f'Monstret bakom {spelare.namn} fann en revolver någon måste ha tappat och sköt dig i ryggen igeonm dörren...')
        time.sleep(2)
        text_utils.slow(f'Grattis! Du har vunnit spelet!... men till vilket pris? \n Det tog dig {int(sluttid - spelare.starttid)} sekunder')
        while True: #Liten meny där man kan kolla sina stats och föremål innan man stänger ner spelet
            val = input('Tryck [F] för att kolla dina stats innan du dog, [R] för att kolla rygsäcken eller Tryck [D] för att avsluta spelet').upper()
            if val == 'R': #printar inventroty
                if len(spelare.inventarie) < 1:
                    print('Du har inga föremål')
                for i, skatt in enumerate(spelare.inventarie):
                    print(f'{i+1}.{skatter.print_skatt(skatt)}\n')

            elif val == 'D': #avslutar spelet
                quit('Vinnst??')

            elif val == 'F': #printar spelarens färdigheter
                spelare.print_färdigheter()
            
            quit()

    #Vinnst!

    text_utils.slow(f'{spelare.namn} finner dig framför en blå dörr')
    time.sleep(1)
    text_utils.slow(f'{spelare.namn} har inget annat val än att gå in i dörren')
    time.sleep(1)
    text_utils.slow(f'Kan detta vara det {spelare.namn} har letat efter hela tiden?   \nKan det vara poopfly?\n')
    time.sleep(1)
    text_utils.slow(f'{spelare.namn} öppnar dörren och ser en pedestal...')
    time.sleep(1)
    text_utils.slow(f'{spelare.namn + spelare.plural} haka ramlar ner i marken\n')
    text_utils.slow('Herregud \n', 0.5)
    text_utils.slow('är det där...?\n')
    text_utils.slow('poopfly!?!?!?\n\n')
    
    time.sleep(2)
    while True: #Liten meny där man kan kolla sina stats och föremål innan man stänger ner spelet
        text_utils.slow(f'Grattis! Du har vunnit spelet!\n Det tog dig {int(sluttid - spelare.starttid)} sekunder')
        val = input('Tryck [F] för att kolla dina stats, [R] för att kolla rygsäcken eller Tryck [D] för att avsluta spelet').upper()
        if val == 'R': #printar inventroty
            if len(spelare.inventarie) < 1:
                print('Du har inga föremål')
            for i, skatt in enumerate(spelare.inventarie):
                print(f'{i+1}.{skatter.print_skatt(skatt)}\n')

        elif val == 'D': #avslutar spelet
            quit('Vinnst!!!!!!')

        elif val == 'F': #printar spelarens färdigheter
            spelare.print_färdigheter()

def förlust(spelare, starttid):
    sluttid = time.time() #stoppar timern
    text_utils.slow(f'Du har FÖRLORAT SPELET! \n Det tog dig {int(sluttid - starttid)} sekunder')
    while True: #Liten meny där man kan kolla sina stats och föremål innan man stänger ner spelet
        val = input('Tryck [F] för att kolla dina stats presis innan du dog, [R] för att kolla rygsäcken eller Tryck [D] för att avsluta spelet').upper()
        if val == 'R': #printar inventroty
            if len(spelare.inventarie) < 1:
                print('Du har inga föremål')
            for i, skatt in enumerate(spelare.inventarie):
                print(f'{i+1}.{skatter.print_skatt(skatt)}\n')

        elif val == 'D': #avslutar spelet
            quit('Förlust')

        elif val == 'F': #printar spelarens färdigheter
            spelare.print_färdigheter()