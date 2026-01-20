import random
class monster: #strukturen alla monster följer
    def __init__(monster, genus, monstertyp, sty, kp):
        monster.genus = genus
        monster.monstertyp = monstertyp
        monster.sty = sty
        monster.kp = kp
    
    def generera_monster(sp1):
        monsteralternativ = [ #möjliga fiender
            monster('En vild', 'Guldfisk', random.randint(1, 3), 1),
            monster('En vild', 'Goblin', 3 + random.randint(int(sp1.sty-3), int(sp1.sty +3)), 1),
            monster('En vild', 'Häxa', 5 + random.randint(int(sp1.sty-4), int(sp1.sty +2)), 1),
            monster('Ett vilt', 'Troll', 7 + random.randint(3, int(sp1.sty+8)), 1),
            monster('En vild', 'Rikard', 2, 1),
            monster('En galen', 'Blottare', 6 + random.randint(1, int(sp1.sty) + 5), 1),
            monster('En kittel', 'fladdermöss', 3 + random.randint(2, int(sp1.sty)), 1)
        ]
        return monsteralternativ[random.randint(0, len(monsteralternativ)-1)] #Väljer en fiende till just detta rum

    def generera_boss(sp1):
        bossmonsteralternativ = [ # möjliga bossar
            monster('Den store och mäktiga fritidsledaren: ', 'Mojje', random.randint(10, 30), sp1.niva+1 * random.random.randint(30,50)),
            monster('Den fruktansvärt (gulliga): ', 'Bleh', random.randint(5,15), sp1.niva+1 * random.random.randint(10,30)),
            monster('"Jag skulle behöva en önskan just nu..."', 'Mortecai', random.randint(10,20), sp1.niva+1 * random.random.randint(20,40)),
            monster('Den', 'den', 1, 1)
        ]
        return bossmonsteralternativ[random.randint(0, len(bossmonsteralternativ)-1)] #skapar en bossfiende från bossmonsteralternativ