import time
def slow(text, delay=0.03): #tar input i text och sekunder delay
    for char in text:
        print (char, end='', flush=True) #skriver ut et
        time.sleep(delay) #väntar delay sekunder innan nästa tecken
    print()

