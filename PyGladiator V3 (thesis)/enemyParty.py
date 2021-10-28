import Enemies
from random import randint

enemy1 = Enemies.Enemy("enemy1",5)

class EnemyParty :
    pass
    def __init__(self, X, Y, partyDifficulty):
        self.Y_cord=X
        self.X_cord=Y
        self.enemyObjsList=[]
        self.startnode=0
        difrng=0
        if partyDifficulty=="Easy":
            difrng=randint(1,4)
        elif partyDifficulty=="Medium":
            difrng=randint(1,5)
        else: difrng=randint(1,6)
            
        for i in range(difrng):
            self.enemyObjsList.append(Enemies.Enemy("enemy1",5))
        
    