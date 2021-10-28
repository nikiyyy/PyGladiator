from random import randint
import json

class Time():
    timehour=12
    timeday=1
    def incTime(self,imepassed):
        print(imepassed,"hours passes")
        Time.timehour+=imepassed
        if Time.timehour>24:
            ostat=Time.timehour%24
            Time.timehour=0
            Time.timehour=ostat
            #tova e za bankata
            Time.timeday+=1 
            if Player.bankacc > 0:
                Player.bankacc+=Player.bankacc*0.02
            if Player.debt > 0:
                Player.debt+=Player.debt*0.05
    def displayaTime(self):
        if Time.timehour%24==0:
            Time.timeday+=1
            Time.timehour=1-1
            print("its midnight\nCurently the time is 24")
        else: print("Curently the time is:",Time.timehour)
class Createitems():#probvai da napravish crafting sistemata SAMO sus dvoien masiv
    craftResNam_ResPrc=[["Cloth",3],["Leather",6],["Iron",8]]
    brewResNam=[]
    brewResPrc=[]
class Weapons():
    mwepNam=("Fists","Wooden Club","Dagger","Mace","Gladius","Spear","Trident",) # 6
    mwepDam=(0,3,5,7,9,10,12)
    mwepSpd=(100,78,94,68,88,80,76)
    mwepPrc=(0,5,15,35,40,55,75)
    mwepWDT=('B','B','SP','B','SP','P','P')
    rmwepNam=("Sling")
    def givewep(self,caller):
        givenwep=""
        if caller=="Slave":
            givenwep=randint(0,2)
            print(caller," is armed with:",Weapons.mwepNam[givenwep])
            return Weapons.mwepDam[givenwep]
        elif caller=="Gladiator":
            givenwep=randint(2,5)
            print(caller," is armed with:",Weapons.mwepNam[givenwep])
            return Weapons.mwepDam[givenwep]
        elif caller=="Champion":
            givenwep=randint(3,6)
            print(caller," is armed with:",Weapons.mwepNam[givenwep])
            return Weapons.mwepDam[givenwep]
class QuestJornal():  
    checkQuest=["Debt collector I","Debt collector II"]
    allQuest={"Debt collector I":"go to the tavern and convince Pentor to pay his debt to the bank"}  
    myQuest={}
    bankQueStart=[False,False,False,False]
    questcomplete=[False,False,False,False]
class Armor():
    armNam=("Rags","Gladiator Armor","Leather Armor","Linothorax","Scail Armor","Lorica Segmentata","Plate Armor")
    armDef=(0,3,5,7,8,10,14)   #suzdavam "Tupple" vmesto list zashtoto nqma da promenqm tezi promenlivi i programata shte e malko po burza
    armTyp=('Light','Light','Light','Light','Medium','Medium','Heavy')
    armPrc=(0,20,30,50,50,80,150)
    sldNam=("nothing","Small sheild","med sheild","large sheild")
    sldDef=(0,5,10,15)
    sldPrc=(0,30,33,55)
class Consumables():
    drinkNam=("Water","Posca","Wine","Mulsum")
    drinkPrc=(1,2,4,7)
    drinkEff=()
    foodNam=("Bread","\"Meat\" Stew")
    foodPrc=(1,3)
    foodEff=()
    ptnNam=("Minor healing potion","Medium healing potion","Major healing potion","Minor Stamina potion","Medium Stamina potion","Major Stamina potion","Strenght potion")
    ptnPrc=(10,25,50,10,25,50,45)
    ptnEff=('30','60','90','50','100','150','misc')
    ptnType=('H','H','H','S','S','S','misc')
    def useitem(self,user,consumable):# za itemi koito ne vlizat v drugite categorii
        pass
    def usepotion(self,user,consumable):
        #finding the poston
        broiach=0
        while True: #
            if consumable == Consumables.ptnNam[broiach]:
                break
            broiach+=1
        #Drinking the poston
        if user=="Player":
            if Consumables.ptnEff[broiach] == "H":
                if consumable=="Minor healing potion":
                    Player.CurHealth+=30
                elif consumable=="Medium healing potion":
                    Player.CurHealth+=60
                elif consumable=="Major healing potion":
                    Player.CurHealth+=90
            elif Consumables.ptnEff[broiach] == "S":
                if consumable=="Minor Stamina potion":
                    Player.CurStam+=50
                elif consumable=="Medium Stamina potion":
                    Player.CurStam+=100
                elif consumable=="Major Stamina potion":
                    Player.CurStam+=150
    def usefood(self,consumable):
        pass
    def usedrink(self,consumable):
        pass
class Player():
    rasa="Human"
    name="Stranger"
    playerClass="warrior"
    pGender='M'
    stats={"STR":5,"END":5,"DIP":10,"DEX":2,"PER":2,"INT":1}
    deficulty=8
    XP=100
    XPlevel=1
    Xpcap=(0,100,225,350,500,675)
    reputation=1
    curcity="Revia"
    karma=0
    meetbefore=[[False,"Arena Tariner"],[False,"Arena Master"],[False,"Bank Banker"],[False,"Tavern Innceeper"],[False,"Tavern Old man"],[False,"Tavern Stranger"],[False,"Blacksmith"],[False,"Alchemist"],[False,"Pawnshop"]]
    myQuest=[]
    complQuest=[]
    #banka i gold
    gold=120
    debt=0
    bankacc=0
    bankinv=[]
    # kombat
    MaxHealth=stats["END"]*10
    CurHealth=MaxHealth
    MaxStam=100
    CurStam=MaxStam
    #eqipment
    wearNAM=Armor.armNam[1]
    wearDef=Armor.armDef[1]
    mainHNam=Weapons.mwepNam[2]
    mainHDam=Weapons.mwepDam[2]
    offHNam=Weapons.mwepNam[0]
    offHDam=Weapons.mwepDam[0] #kogato eqipna shtit Weapons.mwepDam shte e 0
    offHDef=Armor.armDef[0]
    lnv=["Trident","Minor healing potion","Medium healing potion","large sheild","Linothorax","Plate Armor","Water"]
    def battalleChoise(self): #smqtam da izpolzvam funkciqta po sushtiq nachin kakto se ispolza Choice on drugite vragove classove
        pass
    def dodgechance(self,bonus=0):
        bonus
        if bonus==1:
            dodge=randint(1,20)+(Player.stats["DEX"]+randint(0,Player.stats["PER"]))
            print("bonus versiq")# vremenno!!!
            return dodge
        else:
            dodge=randint(1,20)+(Player.stats["DEX"]+randint(0,Player.stats["PER"]))/2
            return dodge
    def attackchance(self):
        attack=randint(1,20)+(Player.stats["DEX"]+randint(0,Player.stats["PER"]))/2
        return attack
class Slave():
    Maxhealth=30
    Curhealth=Maxhealth
    SMaxStam=60
    SCurStam=SMaxStam
    xpReward=7
    goldReward=3
    reputationReward=4
    dodgeChance=3
    mainH=1
    offH=0
    damage=2
    enInv=[]
    def creatInv(self):
        Slave.enInv=[]#nuliram inentorito
        seedNum=randint(1,10)
        if seedNum>5:
            Slave.enInv.append("Cloth")
        if seedNum>9:
            Slave.enInv.append("Minor healing potion")
        #else:
        #    pass
        print(Slave.enInv)
    def choise(self,randnum=1,bon=0,combatantCurhel=0):
        Sobj=Slave()
        Slave.dodgeChance=3 #tova e tuk zadamoje da nulira defence bonusa
        print("randnum e",randnum)# debug
        if randnum==1 or Slave.SCurStam+10<=0:
            #dobavi if logika za tova dali ima otvara za stamina i ako da, q szpolzvai
            print("The slave gathers his strength")
            Slave.SCurStam+=30
        elif randnum<=8:
            #print(randnum,"DEBUG - vleze v ataka")
            combattack=randint(1,20)
            if combattack>Player.dodgechance(bon):
                #print("DEBUG - vleze v dodgechance")
                if combattack > Player.wearDef+Player.offHDef:
                    print("DEBUG - ",Player.wearDef+Player.offHDef)
                    Sobj.attack()
                else: print("the attack was deflected")
            else:print("you dodged the salve's attack")
        elif randnum ==9:
            Slave.SCurStam+=10
            Sobj.defence()
        else:
            Slave.SCurStam-=5
            Sobj.spacial1()
    def attack(self):
        damdel=Slave.damage+int(Slave.mainH)   #ne pomnq zashto sum dobavi "int(Slave.mainH)"
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))  #sled vreme dobavi player rezistencii...(sled kato sa gotovi)
    def defence(self):
        print("The Slave is preparing for your attack")
        Slave.dodgeChance=6
    def spacial1(self):
        print("Slave throws sand in your eyes!\nYour attack and dodge chance are lowerd for a turn")
        Player.stats["DEX"]-=3
        Player.stats["PER"]-=3
        if Player.stats["DEX"]<=0:  #ne zanm zashto kogato stats padne pod 0 ne moga da vlqva v "fight()" funkciqta
            Player.stats["DEX"]=1
        if Player.stats["PER"]<=0:
            Player.stats["PER"]=1
        print("your dexterity and perception have been lowerd to",Player.stats["DEX"],Player.stats["PER"])
class Gladiator(): # NE RABOTI
    Maxhealth=70
    Curhealth=Maxhealth
    SMaxStam=100
    SCurStam=SMaxStam
    xpReward=25
    goldReward=15
    reputationReward=10
    dodgeChance=9
    mainH=1
    offH=0
    damage=4
    def choise(self,randnum=1,bon=0):
        Gobj=Gladiator()
        Gladiator.dodgeChance=9 #tova e tuk zadamoje da nulira defence bonusa
        if randnum<1 or Gladiator.SCurStam+10<=0:
            #dobavi if logika za tova dali ima otvara za stamina i ako da, q szpolzvai
            print("The Gladiator gathers his strength")
            Gladiator.SCurStam+=30
        elif randnum<5:
            #print(randnum,"DEBUG - vleze v ataka")
            combattack=randint(1,20)
            if combattack>Player.dodgechance(bon):
                #print("DEBUG - vleze v dodgechance")
                if combattack > Player.wearDef:
                    #print("DEBUG - vleze v wearDef")
                    Gobj.attack()
                else: print("the attack was deflected by your armor")
            else:print("you dodged the Gladiator's attack")
        elif randnum <8:
            Gladiator.SCurStam+=10
            Gobj.defence()
        else: 
            Gladiator.SCurStam-=5
            Gobj.spacial1()
    def attack(self):
        damdel=Gladiator.damage+int(Gladiator.mainH)
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))  #sled vreme dobavi player rezistencii...(sled kato sa gotovi)
    def defence(self):
        print("The Gladiator is preparing for your attack")
        Gladiator.dodgeChance=15
    def spacial1(self):
        print("The Gladiator is pulping up the crowd")  
class Champion():      #ne e testvana
    Maxhealth=100
    Curhealth=Maxhealth
    xpReward=50
    goldReward=30
    reputationReward=25
    dodgeChance=8
    mainH=1
    offH=0
    damage=6
    def choise(self,randnum=1):
        Cobj=Champion()
        Champion.dodgeChance=8 #tova e tuk zadamoje da nulira defence bonusa
        if randnum<5:
            Cobj.attack()
        elif randnum <8:
            Cobj.defence()
        else: Cobj.spacial1()
    def attack(self):
        damdel=Champion.damage+int(Champion.mainH)   
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))  #sled vreme dobavi player rezistencii...(sled kato sa gotovi)
    def defence(self):
        print("The Champion is preparing for your attack")
        Champion.dodgeChance=14
    def spacial1(self):
        print("The Champion is pulping up the crowd")
class Guard():
    Maxhealth=60
    Curhealth=Maxhealth
    xpReward=20
    goldReward=7
    reputationReward=2
    dodgeChance=6
    damage=4
    def choise(self,randnum):
        pass
class Bandit():
    Maxhealth=45
    Curhealth=Maxhealth
    xpReward=14
    goldReward=2
    reputationReward=15
    dodgeChance=5
    damage=4
    def choise(self,randnum):
        pass
class Wolf():
    Maxhealth=20
    Curhealth=Maxhealth
    xpReward=10
    goldReward=5
    reputationReward=5
    dodgeChance=8
    def choise(self,randnum):
        pass
    def attack(self):
        damdel=randint(2,5)#Player.CurHealth+(0.95+(Player.stats[1]/20))
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))
class Bear():
    Maxhealth=70
    Curhealth=Maxhealth
    xpReward=20
    goldReward=13
    reputationReward=12
    dodgeChance=3
    def choise(self,randnum):
        pass
    def attack(self):
        damdel=randint(3,7)#Player.CurHealth+(0.95+(Player.stats[1]/20))
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))
class Lion():
    Maxhealth=60
    Curhealth=Maxhealth
    xpReward=25
    goldReward=30
    reputationReward=25
    dodgeChance=12
    def choise(self,randnum):
        pass
    def attack(self):
        damdel=randint(5,9)#Player.CurHealth+(0.95+(Player.stats[1]/20))
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))
class Basilisk():
    Maxhealth=80
    Curhealth=Maxhealth
    xpReward=80
    goldReward=30
    reputationReward=30
    dodgeChance=7  
    def choise(self,randnum):
        pass
    def attack(self):
        damdel=randint(6,11)#Player.CurHealth+(0.95+(Player.stats[1]/20))
        print("You resive",damdel,"damage!")
        Player.CurHealth-=(damdel-(Player.wearDef/10))
def Buy(shop):
    try:
        if shop=="Tavern":
            while True:
                print("Gold",Player.gold)
                izbor=int(input("food or drink?\n1.Drink\n2.Food\n3.Back\n"))
                if izbor==1:
                    for x in range(0,len(Consumables.drinkNam)):
                        print(x+1,"- Drink:",Consumables.drinkNam[x],"Price:",Consumables.drinkPrc[x])
                    izbor=int(input("enter the coresponding number\n"))
                    if izbor == 1:
                        if Player.gold>=Consumables.drinkPrc[izbor-1]:
                            Player.gold-=Consumables.drinkPrc[izbor-1]
                            Player.lnv.append(Consumables.drinkNam[izbor-1])
                        else: print("No gold, no drink")
                    elif izbor == 2:
                        if Player.gold>=Consumables.drinkPrc[izbor-1]:
                            Player.gold-=Consumables.drinkPrc[izbor-1]
                            Player.lnv.append(Consumables.drinkNam[izbor-1])
                        else: print("No gold, no drink")
                    elif izbor == 3:
                        if Player.gold>=Consumables.drinkPrc[izbor-1]:
                            Player.gold-=Consumables.drinkPrc[izbor-1]
                            Player.lnv.append(Consumables.drinkNam[izbor-1])
                        else: print("No gold, no drink")
                    elif izbor == 4:
                        if Player.gold>=Consumables.drinkPrc[izbor-1]:
                            Player.gold-=Consumables.drinkPrc[izbor-1]
                            Player.lnv.append(Consumables.drinkNam[izbor-1])
                        else: print("No gold, no drink")
                    else: print("Item does no exist\n")
                elif izbor==2:
                    for x in range(0,len(Consumables.foodNam)):
                        print(x+1,". Food:",Consumables.foodNam[x],"Price:",Consumables.foodPrc[x])
                    izbor=int(input("3 - Back\nenter the coresponding number\n"))
                    if izbor == 1:
                        if Player.gold>=Consumables.foodPrc[izbor-1]:
                            Player.gold-=Consumables.foodPrc[izbor-1]
                            Player.lnv.append(Consumables.foodNam[izbor-1])
                        else: print("No gold, no food")     
                    elif izbor == 2:
                        if Player.gold>=Consumables.foodPrc[izbor-1]:
                            Player.gold-=Consumables.foodPrc[izbor-1]
                            Player.lnv.append(Consumables.foodNam[izbor-1])
                        else: print("No gold, no food")       
                elif izbor==3:
                    break
                else: print("Item does no exist\n")
        if shop=="Armor":
            while True:
                print("Gold",Player.gold)
                for x in range(1,len(Armor.armNam)): #ciklira prez vsichki broni
                    print(x,"- Name:",Armor.armNam[x],"Defence:",Armor.armDef[x],"Type:",Armor.armTyp[x],"Price:",Armor.armPrc[x])
                izbor=int(input("7. Back")) 
                if izbor == 1:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold")
                elif izbor == 2:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold")
                elif izbor == 3:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold")
                elif izbor == 4:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold") 
                elif izbor == 5:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold")
                elif izbor == 6:
                    if Player.gold>=Armor.armPrc[izbor]: 
                        Player.gold-=Armor.armPrc[izbor]
                        Player.lnv.append(Armor.armNam[izbor])
                    else: print("Not enough gold")
                elif izbor == 7:
                    break
                else: print("Item does no exist\n")      
        if shop=="Weapons":
                while True:
                    print("Gold",Player.gold)
                    izbor=int(input("\n1. melee weapons\n2. ranged weapons\n3. back"))
                    if izbor==1:
                        for x in range(0,len(Weapons.mwepNam)-1):
                            print(x+1,"- Name:",Weapons.mwepNam[x+1],"Damage:",Weapons.mwepDam[x],"Type:",Weapons.mwepWDT[x],"Speed:",Weapons.mwepSpd[x],"Price:",Weapons.mwepPrc[x])
                        izbor=int(input("7. Back"))
                        if izbor == 1:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")     
                        elif izbor == 2:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")
                        elif izbor == 3:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")
                        elif izbor == 4:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")
                        elif izbor == 5:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")
                        elif izbor == 6:
                            if Player.gold>=Weapons.mwepPrc[izbor]: 
                                Player.gold-=Weapons.mwepPrc[izbor]
                                Player.lnv.append(Weapons.mwepNam[izbor])
                            else: print("Not enough gold")                      
                        elif izbor == 7:break
                        else: print("Item does no exist\n")   
                    elif izbor==2:
                        print("ranged weapons")
                    elif izbor==3:
                        break
                    else: print("\ndon't be an idiot,dude...\n")
                    print("\ndon't be an idiot,dude...\n")
        if shop=="Mage":
            while True:
                print("Gold",Player.gold)
                izbor=int(input(""))
                print("\ndon't be an idiot,dude...\n")
        if shop=="Alchmist":
            while True:
                print("Gold",Player.gold)
                for x in range(0,len(Consumables.ptnNam)):
                    print(x+1,"- Name:",Consumables.ptnNam[x],":Price:",Consumables.ptnPrc[x])
                izbor=int(input("8.Back")) 
                if izbor == 1:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold")     
                elif izbor == 2:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold") 
                elif izbor == 3:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold")
                elif izbor == 4:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold")  
                elif izbor == 5:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold") 
                elif izbor == 6:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold") 
                elif izbor == 7:
                    if Player.gold>=Consumables.ptnPrc[izbor-1]: 
                        Player.gold-=Consumables.ptnPrc[izbor-1]
                        Player.lnv.append(Consumables.ptnNam[izbor-1])
                    else: print("Not enough gold") 
                elif izbor == 8:break
                else:print("Item does no exist\n")   
        if shop=="Pawnshop":
            while True:
                print("Gold",Player.gold)
                izbor=int(input(""))
    except ValueError:
        print("\ndon't be an idiot,dude...\n")
def Sellrp(item4sell,itemcat,itemprc):# funkciq za prodavane i vzemane na cenata na item sprqmo atrebutite na player charackter
    broiach=0
    while True: #
        if item4sell == itemcat[broiach]:
            break
        broiach+=1
    return itemprc[broiach]+(Player.stats["DIP"]*1.5)
def GatArmDef(itemdef):# funkciq za euipvane na broni
    broiach=0
    while True: 
        if itemdef == Armor.armNam[broiach]:
            break
        broiach+=1
    return Armor.armDef[broiach]
def GatSldDef(itemdef):# funkciq za euipvane na broni
    broiach=0
    while True: 
        if itemdef == Armor.sldNam[broiach]:
            break
        broiach+=1
    return Armor.sldDef[broiach]
def GatPtnHel(itemhel):# d
    broiach=0
    while True: 
        if itemhel == Consumables.ptnNam[broiach]:
            break
        broiach+=1
    return Consumables.ptnEff[broiach]
def Gatmainat(itemdef):# funkciq za euipvane na broni
    broiach=0
    while True: 
        if itemdef == Weapons.mwepNam[broiach]:
            break
        broiach+=1
    return Weapons.mwepDam[broiach]
def Sell(shop):
    try:
        if shop=="Armor":
            print("Gold",Player.gold)
            menuto=[]
            menutoizb=[]
            condMet=0
            for x in range(len(Player.lnv)):
                if Player.lnv[x] in Armor.armNam:
                    menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                    menutoizb.append(condMet)# tezi davata lista sa svurzani!
                    condMet+=1
                x+=1
            while True:
                for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                    print(menutoizb[x]+1,menuto[x],Sellrp(menuto[x],Armor.armNam,Armor.armPrc))
                izbor=int(input())
                for x in range(len(menuto)): #proverqvam
                    if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                        Player.lnv.remove(menuto[x])
                        Player.gold+=Sellrp(menuto[x],Armor.armNam,Armor.armPrc)
                break
        elif shop=="Weapons":
            print("Gold",Player.gold)
            menuto=[]
            menutoizb=[]
            condMet=0
            for x in range(len(Player.lnv)):
                if Player.lnv[x] in Weapons.mwepNam:
                    menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                    menutoizb.append(condMet)# tezi davata lista sa svurzani!
                    condMet+=1
                x+=1
            while True:
                for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                    print(menutoizb[x]+1,menuto[x],Sellrp(menuto[x],Weapons.mwepNam,Weapons.mwepPrc))
                izbor=int(input())
                for x in range(len(menuto)): #proverqvam
                    if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                        Player.lnv.remove(menuto[x])
                        Player.gold+=Sellrp(menuto[x],Weapons.mwepNam,Weapons.mwepPrc)
                break
        #if shop=="Weapons":
    except ValueError:
        print("\ndon't be an idiot,dude...\n")   
def BuyOrSell(shop):
    while True:
        try:
            izbor=int(input("\n1. Buy \n2. Sell\n3. Back"))
            if izbor== 1:
                if shop == "Armor":
                    Buy("Armor")
                elif shop == "Weapons":
                    Buy("Weapons")                   
                elif shop == "Mage":
                    Buy("Mage")
                elif shop == "Alchmist":
                    Buy("Alchmist")
                elif shop == "Pawnshop":
                    Buy("Pawnshop")
            elif izbor== 2:
                if shop == "Armor":
                    Sell("Armor")
                elif shop == "Weapons":
                    Sell("Weapons")                  
                elif shop == "Mage":
                    Sell("Mage")
                elif shop == "Alchmist":
                    Sell("Alchmist")
                elif shop == "Pawnshop":
                    Sell("Pawnshop")
            elif izbor== 3:
                break
            else: print("\ndon't be an idiot,dude...\n") 
        except ValueError:
            print("\ndon't be an idiot,dude...\n") 
def Charcreat():

    Player.stats["END"]=1     #nulirame statsovede poneje moje da se explotirat
    Player.stats["DEX"]=1
    Player.stats["DIP"]=1
    Player.stats["STR"]=1
    Player.stats["INT"]=1
    Player.stats["PER"]=1
    abiltyPoints=10  # defeniram tochkite zada moje da gi izpolzvam kato argument v ciklite po-dolu
    
    while abiltyPoints!=0: # isbirame rasa
        while abiltyPoints!=0:
            print(Player.rasa)
            print("\n\n\n\nDwraf- +1 ENDness\nElf- +1 dextirity\nHuman- +1 Diplomacy\nOrc- +1 Strench")
            Player.rasa=input("type the race you wnat to play as: \n")
            Player.rasa.lower()
            if Player.rasa == "dwarf":
                Player.stats["END"]+=1
                break
            elif Player.rasa =="elf":
                Player.stats["DEX"]+=1
                break
            elif Player.rasa =="human":
                Player.stats["DIP"]+=1
                break
            elif Player.rasa =="orc":
                Player.stats["STR"]+=1
                break
            else: print("don't be stupid")
            
        while abiltyPoints!=0: # isbirame class
            Player.playerClass=input("chose a calss: \nWarrior\nMage\nThief\nRanger")
            Player.playerClass.lower()
            if Player.playerClass == "warrior" or Player.playerClass == "mage" or Player.playerClass == "thief" or Player.playerClass == "ranger":
                Player.name=input("what is your name "+Player.rasa)
                while abiltyPoints!=0:
                    print("points to spend" ,abiltyPoints)
                    print("STATS:\n1. Strenght: "+str(Player.stats["STR"]),"\n2. Endurance: "+str(Player.stats["END"]),"3. Deplomacy: "+str(Player.stats["DIP"]))
                    print("\n4. Dexterity: "+str(Player.stats["DEX"]),"\n5. Perception: "+str(Player.stats["PER"]),"6. Inteligence: "+str(Player.stats["INT"]))
                    bla=int(input("Whith stat do you wnat to increase?\nPress the coresponding number!"))
                    if bla==1:
                        Player.stats["STR"]+=1
                        abiltyPoints-=1
                    elif bla==2:
                        Player.stats["END"]+=1
                        abiltyPoints-=1
                    elif bla==3:
                        Player.stats["DIP"]+=1
                        abiltyPoints-=1
                    elif bla==4:
                        Player.stats["DEX"]+=1
                        abiltyPoints-=1
                    elif bla==5:
                        Player.stats["PER"]+=1
                        abiltyPoints-=1
                    elif bla==6:
                        Player.stats["INT"]+=1
                        abiltyPoints-=1
                    
                    else: print("enter the coresponding numer... dumbass...")
                Player.CurHealth=Player.MaxHealth   #tova e taka zada moje kogato pochna igra da ne pochvam sus nachalnite stoinosti
                Startgame()    
            else: print("I didn't quite catch that, could you please repeat?")
    else: print("I didn't quite catch that, could you please repeat?")
    Stmenu()
def playermenu(calledFrom): #calledFrom v zavisemost ot kade e izvikana moje da ne mojesh da izplozvash opredeleni fituri(ne moje da si smenqsh bronqta ako viknwsh funkciqta ot renata)
    while True:
        Pcons=Consumables()
        try:
            izbor=int(input("\n1.Check stats or level up\n2.Change Equpment X\n3.Check Quest log X\n4.Check inventory\n5.Consume potion \n6.Have a Drink \n7.Eat food \n8. Wait\n9.Back"))
            if izbor==1:
                print("\nName:",Player.name,"|Race:",Player.rasa,"|Class:",Player.playerClass)
                print("Gold:",Player.gold,"|Rep:",Player.reputation,"|XP:",Player.XP,"/","NEXT LEVEL")
                print(Player.stats)
                print("Wearing:",Player.wearNAM,"\nArmed with: MH:",Player.mainHNam,"OH:", Player.offHNam )
                if Player.XP>=Player.Xpcap[Player.XPlevel] and calledFrom!="battle": # ph proverka dalisum dignal nivoto. ako bude izvikano po vreme na bitka novite statsove nqma da se zapametqt, poneje v krq na bitkata ima nqkolko promenlivi koito ti mahat vsqkakvi promeni ot player statsa(pemahvat potencialni debuffove)
                    Player.XPlevel+=1
                    print("You, leveled up!")
                    print("STATS:\n1. Strenght: "+str(Player.stats["STR"]),"\n2. Endurance: "+str(Player.stats["END"]),"\n3. Deplomacy: "+str(Player.stats["DIP"]))
                    print("4. Dexterity: "+str(Player.stats["DEX"]),"\n5. Perception: "+str(Player.stats["PER"]),"\n6. Inteligence: "+str(Player.stats["INT"]))
                    bla=int(input("Whith stat do you wnat to increase?\nPress the coresponding number!"))
                    if bla==1:
                        Player.stats["STR"]+=1
                    elif bla==2:
                        Player.stats["END"]+=1
                    elif bla==3:
                        Player.stats["DIP"]+=1
                    elif bla==4:
                        Player.stats["DEX"]+=1
                    elif bla==5:
                        Player.stats["PER"]+=1
                    elif bla==6:
                        Player.stats["INT"]+=1
                else:print(Player.Xpcap[Player.XPlevel]-Player.XP,"xp until next level")
            elif izbor==2:
                izbor=int(input("\n1.Change armor\n2.Change mainhand weapon\n3.Change offhand weapon"))
                if izbor==1 and calledFrom!="battle":
                    menuto=[]
                    menutoizb=[]
                    condMet=0
                    for x in range(len(Player.lnv)):
                        if Player.lnv[x] in Armor.armNam:
                            menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                            menutoizb.append(condMet)# tezi davata lista sa svurzani!
                            condMet+=1
                        x+=1
                    while True:
                        for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                            print(menutoizb[x]+1,menuto[x],)
                        izbor=int(input("if you want to exit press any other number"))
                        for x in range(len(menuto)): #proverqvam
                            if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                                Player.lnv.append(Player.wearNAM)
                                Player.wearDef=GatArmDef(menuto[izbor-1])
                                Player.wearNAM=menuto[izbor-1]
                                Player.lnv.remove(menuto[izbor-1])
                                print(Player.wearDef)
                        break
                elif izbor==2:
                    menuto=[]
                    menutoizb=[]
                    condMet=0
                    for x in range(len(Player.lnv)):
                        if Player.lnv[x] in Weapons.mwepNam:
                            menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                            menutoizb.append(condMet)# tezi davata lista sa svurzani!
                            condMet+=1
                        x+=1
                    while True:
                        for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                            print(menutoizb[x]+1,menuto[x],)
                        izbor=int(input("if you want to exit press any other number"))
                        for x in range(len(menuto)): #proverqvam
                            if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                                Player.lnv.append(Player.mainHNam)
                                Player.mainHDam=Gatmainat(menuto[izbor-1])
                                Player.mainHNam=menuto[izbor-1]
                                Player.lnv.remove(menuto[izbor-1])
                                print(Player.mainHNam)
                        break
                elif izbor==3:
                    menuto=[]
                    menutoizb=[]
                    condMet=0
                    for x in range(len(Player.lnv)):
                        if Player.lnv[x] in Weapons.mwepNam or Player.lnv[x] in Armor.sldNam:
                            menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                            menutoizb.append(condMet)# tezi davata lista sa svurzani!
                            condMet+=1
                        x+=1
                    while True:
                        for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                            print(menutoizb[x]+1,menuto[x],)
                        izbor=int(input("if you want to exit press any other number"))
                        for x in range(len(menuto)): #proverqvam
                            if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                                Player.lnv.append(Player.offHNam)
                                if menuto[izbor-1] in Weapons.mwepNam:
                                    Player.offHDam=Gatmainat(menuto[izbor-1])
                                    Player.offHDef=0 #nuliram tezi zashoto kogato smenq ot offhabd orushie na shtit offhand statsovete ostavat
                                if menuto[izbor-1] in Armor.sldNam:
                                    Player.offHDef=GatSldDef(menuto[izbor-1])
                                    Player.offHDam=0
                                Player.offHNam=menuto[izbor-1]
                                Player.lnv.remove(menuto[izbor-1])
                                print(Player.offHNam)
                        break
            elif izbor==3:
                print(Player.myQuest)
            elif izbor==4:
                print(Player.lnv)
            elif izbor==5:
                menuto=[]
                menutoizb=[]
                condMet=0
                for x in range(len(Player.lnv)):
                    if Player.lnv[x] in Consumables.ptnNam:
                        menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                        menutoizb.append(condMet)# tezi davata lista sa svurzani!
                        condMet+=1
                    x+=1
                while True:
                    for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                        print("\n",menutoizb[x]+1,menuto[x],)
                    izbor=int(input("if you want to exit press any other number"))
                    for x in range(len(menuto)): #proverqvam
                        if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                            Player.lnv.remove(menuto[x])
                            Pcons.usepotion("Player",menuto[x])
                        else:break
                    break
            elif izbor==6 and calledFrom!="battle":
                menuto=[]
                menutoizb=[]
                condMet=0
                for x in range(len(Player.lnv)):
                    if Player.lnv[x] in Consumables.drinkNam:
                        menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                        menutoizb.append(condMet)# tezi davata lista sa svurzani!
                        condMet+=1
                    x+=1
                while True:
                    for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                        print("\n",menutoizb[x]+1,menuto[x],)
                    izbor=int(input("if you want to exit press any other number"))
                    for x in range(len(menuto)): #proverqvam
                        if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                            Player.lnv.remove(menuto[x])
                            Pcons.usedrink(menuto[x])
                        else:break
                    break
            elif izbor==7 and calledFrom!="battle":
                menuto=[]
                menutoizb=[]
                condMet=0
                for x in range(len(Player.lnv)):
                    if Player.lnv[x] in Consumables.foodNam:
                        menuto.append(Player.lnv[x]) #kopram itemite koito vendora iska da kupi v nov list menu
                        menutoizb.append(condMet)# tezi davata lista sa svurzani!
                        condMet+=1
                    x+=1
                while True:
                    for x in range(len(menuto)): #izkrvam na ekrana itemite koito igracha ima a prodavacha iska
                        print("\n",menutoizb[x]+1,menuto[x],)
                    izbor=int(input("if you want to exit press any other number"))
                    for x in range(len(menuto)): #proverqvam
                        if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte prodam suotvetniq item
                            Player.lnv.remove(menuto[x])
                            Pcons.usefood(menuto[x])
                        else:break
                    break
            elif izbor==8 and calledFrom!="battle":
                vrem=Time()
                vrem.displayaTime()
                izbor=int(input("How long do you want to wait?"))
                vrem.incTime(izbor)
                vrem.displayaTime()
                del vrem
            elif izbor==9:
                break
            else: print("You can't acces this right now")
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def Randinc(incNum): #wip
    if incNum >=50:
        if incNum%2 == 0:
            print("bad incounter")
        else: print("good incounter")
def fight(oponnet,numcomb=1): #wip numcomb e bori kombatants WIP soon...
    Pobj=Player() # suzdavam player obekt zada moga da izpolzvam funkciite ot class Player
    endVar=Player.stats["END"]
    perVar=Player.stats["PER"]
    if oponnet=="Slave":
        combatant=Slave()
        wepforcom=Weapons()#weapons objeckt
        Slave.mainH=wepforcom.givewep(oponnet)#v zavisimost koj izvikva funkciqta dava razlichno neshto
        combatant.creatInv()
    elif oponnet=="Gladiator":
        combatant=Gladiator
        wepforcom=Weapons()
        Gladiator.mainH=wepforcom.givewep(oponnet)
    elif oponnet=="Champion":
        combatant=Champion
        wepforcom=Weapons()
        Champion.mainH=wepforcom.givewep(oponnet)
    elif oponnet=="Bandit":
        combatant=Bandit
        wepforcom=Weapons()
        Bandit.mainH=wepforcom.givewep(oponnet)
    elif oponnet=="Guard":
        combatant=Guard()
        wepforcom=Weapons()
        Guard.mainH=wepforcom.givewep(oponnet)
    elif oponnet=="Wolf":
        combatant=Wolf()
    elif oponnet=="Bear":
        combatant=Bear()
    elif oponnet=="Lion":
        combatant=Lion()
    elif oponnet=="Basilisk":
        combatant=Basilisk()
    else: print("ne stava")
    win=False
    print("you are fighting against an "+oponnet)
    while win==False:
        try:
            #print("distance between you and oponent:")
            print("\nYour Health:"+str(Player.CurHealth)+"/"+str(Player.MaxHealth)+"\nYour Stamina:"+str(Player.CurStam)+"/"+str(Player.MaxStam))
            print("\n1.Attack\n2.Defend\n3.Do nothing\n4.Use item\n5.Run away\n")
            izbor=int(input("Enemy Health:"+str(combatant.Curhealth)+"/"+str(combatant.Maxhealth)+"\nEnemy Stamina:"+str(Slave.SCurStam)+"/"+str(Slave.SMaxStam)))#"\n1. Close the distance\n2. Widen the distance\n3."
            if izbor==1:
                bonus=0
                playerattack=randint(1,20)
                if Player.CurStam<=0:
                    print("you Try to attack, but youre too tired")
                    Player.CurStam+=20
                else:
                    Player.CurStam-=10
                    if Pobj.attackchance() > combatant.dodgeChance:
                        if playerattack>1:# placeholder! -combatant armor
                            combatant.Curhealth-=(Player.mainHDam+(Player.stats["STR"]/2))+(Player.offHDam/2)
                            if combatant.Curhealth<=0:
                                try:
                                    combatant.Curhealth=0
                                    print("\n\n\nEnemy Health:"+str(combatant.Curhealth)+"/"+str(combatant.Maxhealth),"\nyou win!")
                                    print("You gain: XP -",combatant.xpReward,"\nGold -", combatant.goldReward,"\nRepuation -",combatant.reputationReward)
                                    Player.XP+=combatant.xpReward
                                    Player.gold+=combatant.goldReward # nagradi
                                    Player.reputation+=combatant.reputationReward
                                    Player.stats["END"]=endVar # sted kato si supulnil atakata, ako si bil debuffnat statsovete ti se vrushtat
                                    Player.stats["PER"]=perVar
                                    Player.lnv.append(combatant.enInv)
                                    izbor=int(input("to exit press any key"))
                                    break
                                except ValueError:
                                    print("exit")
                                    break
                    else: print("Attack failed to connect!!")
            elif izbor==2:
                bonus=1 #kogato izvikam defence bonus stava 1 i vikam razlichna versiq na "dodgechance()"
            elif izbor==3:
                Player.CurStam+=30
                bonus=0
                print("you... do nothing???")
            elif izbor==4:
                bonus=0
                playermenu("battle")
            elif izbor==5:
                break
            else: print("\ndon't be an idiot,dude...\n")
            Player.stats["END"]=endVar # sted kato si supulnil atakata, ako si bil debuffnat statsovete ti se vrushtat
            Player.stats["PER"]=perVar
            psevdoIzbor=randint(1,10)#tova e nachen protivnicite da mogat da piqt otvari za shevot i da si propusnat reda(ako imat v inventara si) ako argumenta v if statementa ne e izpulnen, vraga shte vleze choise
            if psevdoIzbor==1 and combatant.Curhealth<combatant.Maxhealth and "Minor healing potion" in combatant.enInv:
                for x in range(len(combatant.enInv)):# otvara kod
                    if combatant.enInv[x-1] in Consumables.ptnNam:
                        print(oponnet,"uses",combatant.enInv[x-1])
                        combatant.Curhealth+=int(GatPtnHel(combatant.enInv[x-1]))
                        combatant.enInv.remove(combatant.enInv[x-1])
            else:#ako vraga ne izpie otvara shte atakuva
                combatant.SCurStam-=10 
                combatant.choise(psevdoIzbor,bonus,combatant.Curhealth)
                bonus=0
            if Player.CurHealth <=0:
                print("you lost")
                break
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def Market():
    if Time.timehour>=6 and Time.timehour<=21:
        while True:
            print("You arrive at the market ")
            try:
                izbor=int(input("1. Blacksmith\n2. Alchmist\n3. Pawnshop\n4. docks\n5.Slave market \n6. Exit"))
                if izbor == 1:
                    while True:
                        try:
                            if Player.meetbefore[6][0] is False: #proverka dali predi si govoril sus choveka
                                print("vleze")
                                Player.meetbefore[6][0]=True
                            else:print("\nYou are greeted by the long nosed a receptionist")
                            izbor=int(input("\n1. Armor \n2. Weapons\n3 Use forge\n4. Back"))
                            if izbor== 1:
                                BuyOrSell("Armor")
                            elif izbor== 2:
                                BuyOrSell("Weapons")
                            elif izbor== 3:
                                print("forge")
                            elif izbor== 4:
                                break
                            else: print("\ndon't be an idiot,dude...\n") 
                        except ValueError:
                            print("\ndon't be an idiot,dude...\n") 
                elif izbor == 2:
                    if Player.meetbefore[7][0] is False: #proverka dali predi si govoril sus choveka
                        print("vleze")
                        Player.meetbefore[7][0]=True
                    else:print("\nYou are greeted by the long nosed a receptionist")
                    BuyOrSell("Alchmist")
                elif izbor == 3:
                    if Player.meetbefore[8][0] is False: #proverka dali predi si govoril sus choveka
                        print("vleze")
                        Player.meetbefore[8][0]=True
                    else:print("\nYou are greeted by the long nosed a receptionist")
                    BuyOrSell("Pawnshop")
                elif izbor == 4:
                    print("docks")
                    docks()
                elif izbor == 5:
                    print("slave marcet")
                elif izbor == 6:
                    break
                else: print("don't be an idiot,dude...")
            except ValueError:
                print("\ndon't be an idiot,dude...\n")    
    else: print("The market is closed for the night,Please come in the morning")
def rumors(rumNum,callloc):
    if rumNum==1:
        print("rom1")
    elif rumNum==2:
        print("rom2")
    elif rumNum==3:
        print("rom3")
    elif rumNum==4:
        print("rom4")
    elif rumNum==5:
        print("rom5")
    elif rumNum==6:
        print("rom6")
    elif rumNum==7:
        print("rom7")
    elif rumNum==8:
        print("rom8")
    elif rumNum==9:
        print("rom9")
    elif rumNum==10:
        print("rom10")
def Tavern():
    vrem=Time()
    print("You enter the Tarvern.You are immediately hit with the smell of bodely fluids,cheap booze.")
    while True:
        try:
            print("There is a mysterious hooded stranger in the corner of the inn. An old man is sitting alone near the stairs.the inn keeper is sitting behind the counter")
            if QuestJornal.bankQueStart[0]==True and QuestJornal.questcomplete[0] != True:
                print("0. Talk to Pento")
            izbor=int(input("1. Inn Keeper\n2. Old man\n3. Misterious stranger\n4. Leave tavern"))
            #bank quest number 1
            if izbor==0 and QuestJornal.bankQueStart[0]==True and QuestJornal.questcomplete[0] != True:
                print("You aproach Pento,he is a scrawny looking man,who is sitting alone on a table.\nPento - *rises his head* What do you want?")
                izbor=int(input("1. I'm here about the debth you own to the bank\n2 Sorry, wrong table"))
                if izbor==1:
                    while True:
                        print("Pento - look here, do you think i give a shit about the bank?I owe money to far more dangerous people, some of witch are part of The Syndicatus.Those fart sniffers at the bank will eventualy get their money.I just need some more time to pay some more inportant people")
                        izbor=int(input("\n1.[STR 5 needed]Grab him by the neck.\n2.[DIP 4 needed]Is this how you repay your loans?\n3.[PER 4 needed]Threaten him\n4.How did you endup in this situation?\n5.What is \"The Syndicatus\"\n6.This isn't over yet!"))
                        if izbor==1 and Player.stats["STR"]>=5:
                            print("You - Listen here you filthy rat!You better have the gold by the end of the week or else you will wish that The Syndicatus got their hands on you first!")
                            print("Due to your hands around Pento's neck, he is unable to speak, but starts to nod frantically.\nYou throw him on the ground and leave his table")
                            QuestJornal.questcomplete[0] = True
                            Player.karma-=25
                            break
                        elif izbor==2 and Player.stats["DIP"]>=4:
                            print("look at yourself.Is this how you pay your debths?Sitting in the tarvern, drinking up the money you have left.Get yourself together,this failed venture isn't going to stop you!What are you waiting for?Work hard, pay your debths,Start again and succeed")
                            print("Pento - You're right! I'm going to have your money next week! *leaves the thable and runs out of the tavern* ")
                            QuestJornal.questcomplete[0] = True
                            Player.karma+=15
                            break
                        elif izbor==3 and Player.stats["PER"]>=4:
                            print("You - I can't help but notice you have a wedding band...it would be a shame if something were to happen to to your family...")
                            print("Pento'eyes widen in horror\nPento - Please don't! I swear i'll have the monay next week.just don't do anything brash\nYou leave the tapble with a smug smlie on your face")
                            QuestJornal.questcomplete[0] = True
                            Player.karma-=5
                            break
                        elif izbor==4:
                            print("Pento - long story short, after the birth of my 3rd child I decited to move up in the social ladder.I took out a few loans to buy 2 new ships and fire crews,but a siries of unforionite events lead to the loss of the ships.One was set on fire druing the night and the other sank at sea... with no survivours")
                        elif izbor==5:
                            print("Pento - The Syndicatus are a group of influential cutthroat Merchants, Senators, Landowners and Gangsters, all working together to maximise their profits.Empiror Aurelius has been trying crack down on them but to no avail")
                        elif izbor==6:
                            break
                elif izbor==2:
                    pass
                
            elif izbor==1:
                while True:
                    if Player.meetbefore[3][0] is False: #proverka dali predi si govoril sus choveka
                        print("vleze")
                        Player.meetbefore[3][0]=True
                    else:print("\nYou are greeted by a shady receptionist")
                    print("Inn keeper: if you want a room that will be 4 gold for the night, we also serve food and drinks... and rumors of the right price...*winks and wispers*5 gold")
                    izbor=int(input("\n1.buy room for the night(-4 gold)\n2.Check menu\n3.Ask for rumors(-5 gold)\n4.Back"))
                    if izbor==1:
                        if Player.gold>=4:
                            Player.CurHealth=Player.MaxHealth
                            Player.gold-=4
                            vrem.incTime(8)
                            vrem.displayaTime()
                        else: print("Inn keeper:No gold,No room")
                    elif izbor==2:
                        Buy("Tavern")
                    elif izbor==3:
                        Player.gold-=5
                        rumors(randint(1,10),"Tavern")
                    elif izbor==4:
                        break
                Player.CurHealth=Player.MaxHealth
            elif izbor==2:
                if Player.meetbefore[4][0] is False: #proverka dali predi si govoril sus choveka
                    print("vleze")
                    Player.meetbefore[4][0]=True
                else:print("\nYou are greeted by the a shady receptionist")
                print("old man WIP")
            elif izbor==3:
                if Player.meetbefore[5][0] is False: #proverka dali predi si govoril sus choveka
                    print("vleze")
                    Player.meetbefore[5][0]=True
                else:print("\nYou are greeted by the a shady receptionist")
                print("stranger WIP")
            elif izbor==4:
                break
            else: print("\ndon't be an idiot,dude...\n")   
        except ValueError:
            print("\ndon't be an idiot,dude...\n")     
def Arena():
    try:
        if Time.timehour>=8 and Time.timehour<=21:
            while True:
                izbor=int(input("\n1.Go to training groundsn X\n2.Talk to arena mastern\n3.Exit"))
                if izbor==1:# train, learn, talk, quest
                    while True:
                        if Player.meetbefore[0][0] is False: #proverka dali predi si govoril sus choveka
                            print("vleze")
                            Player.meetbefore[0][0]=True
                        else:print("ne vleze")
                        izbor=int(input("\n1.Train (-6 gold) \n2.Talk to Trainer X \n3.Back"))
                        if izbor==1: #train
                            Player.gold-=6
                            vrem=Time()
                            vrem.incTime(3)
                            vrem.displayaTime
                            xpincr=randint(2,8)
                            Player.XP+=xpincr
                            print("3 hours pass...\n You gain",xpincr,"XP points")
                            if Player.CurStam<150:
                                Player.CurStam+=1
                                print("Your stamina increaces by:",1)
                        elif izbor==2: #talk with trainer and quest
                            print("Trainer")
                            izbor=int(input(""))
                            if izbor==1:
                                pass
                        elif izbor==3: #exit
                            break
                elif izbor==2: #fight, career, bet on fight
                    while True:
                        if Player.meetbefore[1][0] is False: #proverka dali predi si govoril sus choveka
                            print("vleze")
                            Player.meetbefore[1][0]=True
                        else:print("ne vleze")
                        izbor=int(input("\n1.Fight in your rank\n2.Choose a fight\n3.Bet on a fight\n4.Talk to Arena master \n5.Back"))
                        if izbor==1: 
                            if Player.reputation<50:
                                fight("Slave")
                        elif izbor==2: 
                            izbor=int(input("\n1. Slave"))
                            if izbor==1:
                                fight("Slave")
                        elif izbor==3: 
                            print("bet")
                        elif izbor==4: 
                            print("talk")
                        elif izbor==5: 
                            break
                elif izbor==3:
                    break
                else: print("The Arena is closed for the night, in opens at 8 am.")
        else: 
            print("The Arena is closed for the night, in opens at 8 am.")
            izbor=int(input("Do you want to try and sneak in?\n1.Leave.\n2.Sneak in"))
            if izbor==1:
                print("")
            elif izbor==2:
                print("")
    except ValueError:
        print("\nbanker - *sigh* thats not how it works\n")
def Bank():
    if Time.timehour>=8 and Time.timehour<=21:
        if Player.meetbefore[2][0] is False: #proverka dali predi si govoril sus choveka
            print("vleze")
            Player.meetbefore[2][0]=True
        else:print("\nYou are greeted by the a shady receptionist")
        while True:
            try:
                print("Player money:",Player.gold,"   Player debt:",Player.debt,"   Account Balance:",Player.bankacc ,"\nItems in vault",Player.bankinv)
                print("\n1. Take ot loan X\n2. Repay a loan X\n3. Withdraw\n4. Deposit\n5. Talk to Banker\n6. Exit")
                izbor=int(input("what's it gonna be friend?"))
                if izbor == 1:
                    print("Every day the debt increases by 0.5%")
                    if Player.debt > 0:
                        print("banker - \"Reapay the old debt first, you good for nothing deadbeat!!!\"")
                    else:
                        izbor=int(input("banker - *smiles and rubs his hads* \"how much do you whana witdraw\""))
                        if izbor>= Player.gold*2:
                            print("banker - Thats too much money than you know that to do with")
                        else:
                            print("banker - if you dont return the money with intrest, youre gonna have a bad time")
                            Player.debt+=izbor
                            Player.gold+=izbor
                elif izbor == 2:
                    izbor=int(input("banker - lets see what the cat dragged in!\nHow much are you going to pay"))
                    if izbor >= Player.debt:
                        Player.gold-=Player.debt
                        Player.debt=0
                    else:
                        Player.debt-=izbor
                        Player.gold-=izbor
                elif izbor == 3:
                    print("banker - \nWhat! you whnat to withdraw?We take 2% of your gold withdraw")
                    izbor=int(input("1. Withdraw gold \n2. Withdraw item  \n3. Back"))
                    if izbor == 1:
                        izbor=int(input("banker - how much gold do you whana withdraw?"))
                        if izbor==Player.bankacc: #ako player iztegli celq gold taksata za transactiona shte se vzeme ot bankovata smetka
                            print("banker - All of it!?!")
                            izbor-=izbor*0.02
                            Player.gold+=izbor
                            Player.bankacc=0
                        elif izbor+(izbor*0.02)>Player.bankacc:
                            print("banker - You don't have the money",izbor/0.02)
                        else:
                            Player.gold+=izbor
                            Player.bankacc-=(izbor+izbor*0.02)
                    elif izbor == 2:
                        print(Player.bankinv)
                        menuto=[]
                        menutoizb=[]
                        condMet=0
                        for x in range(len(Player.bankinv)):
                            menuto.append(Player.bankinv[x]) #kopram vsick itemi
                            menutoizb.append(condMet)# tezi davata lista sa svurzani!
                            condMet+=1
                            x+=1
                        while True:
                            for x in range(len(menuto)): #izkrvam na ekrana v intentorito mi
                                print(menutoizb[x]+1,menuto[x],)
                            izbor=int(input("if you want to exit press any other number"))
                            for x in range(len(Player.bankinv)): #proverqvam
                                if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte vkaram suotvetniq item
                                    Player.bankinv.remove(menuto[x])
                                    Player.lnv.append(menuto[x])
                            break
                    else:
                        pass
                elif izbor == 4:
                    print("Every day your money stays in the bank, your gold increases 0.2%.\nOh, and one more thing.*The banker rubs his hands and smiles smugly* There's a small 2% fee that will be held for your deposit ")
                    izbor=int(input("1. Deposit Gold\n2. Deposit Item\n3. Back"))
                    if izbor == 1:
                        izbor=int(input("banker - how much gold do you whana deposit"))
                        if izbor>Player.gold:
                            print("banker - You don't have enaugh money")
                        else:
                            Player.gold-=izbor
                            izbor-=izbor*0.02
                            Player.bankacc=izbor
                    elif izbor == 2:
                        print(Player.bankinv)
                        menuto=[]
                        menutoizb=[]
                        condMet=0
                        for x in range(len(Player.lnv)):
                            menuto.append(Player.lnv[x]) #kopram vsick itemi
                            menutoizb.append(condMet)# tezi davata lista sa svurzani!
                            condMet+=1
                            x+=1
                        while True:
                            for x in range(len(menuto)): #izkrvam na ekrana v intentorito mi
                                print(menutoizb[x]+1,menuto[x],)
                            izbor=int(input("if you want to exit press any other number"))
                            for x in range(len(menuto)): #proverqvam
                                if izbor==menutoizb[x]+1: # ako inptua sushtestvuva kato opciq, shte shte vkaram suotvetniq item
                                    Player.bankinv.append(menuto[x])
                                    Player.lnv.remove(menuto[x])
                            break
                    elif izbor == 3:
                        pass
                elif izbor == 5:
                    print("The banker - yes, what do you whant?")
                    izbor=int(input("\n1.let's tack about work\n2.Can you tell me about yourself?\n3.what can you think about the current state of the empire?\n4.What do you think about the city?\n5 Back."))
                    if izbor ==1:
                        #quest 1
                        if "Debt collector I" not in Player.myQuest:
                            print("The banker - yes... is suppose we have e job for you.We are currently in need of some muscle.There are a few people late on their payments, we can't just call the guards ,because thay technicly haven't done anything wrong, they just need some motevation *the banker smirks*.Consider yourself a free lancer of sort,we want you to convince them that it's in their best interst to hurry up with the paymets and collect any the money if they have it on hand")
                            izbor=int(input("The banker - for this first person we will pay you 75 gold.\n1 Accept \n2 Refuse"))
                            if izbor ==1:
                                print("The banker - excellent!") #
                                Player.myQuest.append(QuestJornal.checkQuest[0])
                                print("your first target in an 38 year old human man named Pentor,his occupation is a fisher.He took out a verry large sum of money to buy new ships and hire people to work .A series of missfortiones caused the failur of the of his venture.Now all he does is drink in the tavern, convince him to that it's in his best intrest to get off his ass and get beack to work... oh and dont hurt him too bad *the banker smiles starts filling up peper work*")
                                QuestJornal.bankQueStart[0]=True #ako tova 1 se otkluchvat specialni opci za izlunqvane na questa kato pokazvane na npc
                            elif izbor ==2:
                                print("The banker - *the banker frown and says* well, if you cahange your mind you now where to find us")
                        elif QuestJornal.questcomplete[0] == True and QuestJornal.bankQueStart[0] == True:
                            print("The banker - great job,heres your pay.\nCome see me again if you're looking for work ")
                            Player.gold+=75
                            Player.XP+=20
                            Player.complQuest.append(QuestJornal.checkQuest[0])
                            QuestJornal.bankQueStart[0]=False
                        else:print("The banker - you still haven't taken care of Pento")
                        #quest 2
                        if "Debt collector I" in Player.complQuest:
                            izbor=int(input("The banker - back for more eh? *The banker smiles*.This time the job pays 100 if you get the convince the offender to pay up"))
                            if izbor ==1:
                                print("The banker - This time your job involves a bit more risk.You'll be \"convincing\" a gladiator.He is an young Half-orc named Lucky Mutt.The Mutt was an ex-slave that managed to win his freedom through fighting, that explanes the name.He took out a bet so he could get better equipment and profecional training,but all he's doine in drink, fuck whores and do drugs, we suspect he's planing to leave town without paying.the sum of money he took is trivial,If you can't reason with him make him an exaple for others,about why you shoud never cross the bank.") #
                                Player.myQuest.append(QuestJornal.checkQuest[1])
                            elif izbor ==2:
                                print("The banker - come see me if you reconsider")
                        #quest 3
                        if "Debt collector II" in Player.complQuest:
                            izbor=int(input("The banker - "))
                            if izbor ==1:
                                print("The banker - exelent!") #
                            elif izbor ==2:
                                print("The ")
                        #quest 4
                        if "Debt collector III" in Player.complQuest:
                            izbor=int(input("The banker - "))
                            if izbor ==1:
                                print("The banker - exelent!") #
                            elif izbor ==2:
                                print("The ")
                    elif izbor ==2:
                        pass
                    elif izbor ==3:
                        pass
                    elif izbor ==4:
                        pass
                    elif izbor ==5:
                        pass
                elif izbor == 6:
                    break
                else: print("\n(((banker))) - *sigh* thats not how it works goy\n")
            except ValueError:
                print("\n(((banker))) - *sigh* thats not how it works goy\n")
    else: print("The Bank is closed.Please come in the morning")
def docks():
    while True:
        try:
            print("you go in the docks")
            izbor=int(input("1.paceholder tradingcompany hedquartes \n2.Sea urchin Tavern\n3.go fishing\n4.buy fresh fish\n5. city light house\n6. back "))
            if izbor ==1:
                print("") #
            elif izbor ==2:
                print("")
            elif izbor ==3:
                print("")
            elif izbor ==4:
                print("")
            elif izbor ==5:
                print("")  
            elif izbor ==6:
                break 
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def outside():
    while True:
        try:
            print("you go otside")
            izbor=int(input("1.stables\n2.guard outpost\n3.graveyard\n4.forest\n5. "))
            if izbor ==1:
                print("") 
            elif izbor ==2:
                print("")
            elif izbor ==3:
                print("")
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def Igmenu():	     # wip dictionery
    while True:
        try:
            print("press 1 to resume game\npress 2 to Load save\npress 3 to save game\npress 4 for Game info\npress 5 to Exit game")
            izbor=int(input("please enter choise: "))
            if izbor == 1:
                break
            elif izbor == 2:
                fName=input("\nPlesease enter the name of the file you want to open(you ad the file extention): ")
                readfile=open(fName,'r')
                fcontent=readfile.readlines()
                Player.rasa=fcontent[0]
                Player.name=fcontent[1]
                Player.playerClass=fcontent[2]
                Player.stats["STR"]=int(fcontent[3])
                Player.stats["END"]=int(fcontent[4])
                Player.stats["DIP"]=int(fcontent[5])
                Player.stats["DEX"]=int(fcontent[6])
                Player.reputation=int(fcontent[7])
                Player.curcity=fcontent[8]
                Player.gold=int(fcontent[9])
                Player.MaxHealth=int(fcontent[10])
                Player.CurHealth=int(fcontent[11])
                Player.wearing=fcontent[12]
                Player.mainH=fcontent[13]
                Player.lnv[:]=[] #emptying inventory list
                for t in range(0, len(fcontent)-14): 
                    print(t)
                    Player.lnv.append(fcontent[t+14])
                readfile.close()
            elif izbor == 3:
                fName=input("\ncriate save file name(you ad the file extention): ")
                savefile=open(fName,'w')
                savefile.write(Player.rasa+"\n"+Player.name+"\n"+Player.playerClass+"\n"+str(Player.stats["STR"])+"\n"+str(Player.stats["END"])+"\n"+str(Player.stats["DIP"])+"\n"+str(Player.stats["DEX"])+"\n"+str(Player.reputation)+"\n"+Player.curcity+"\n"+str(Player.gold)+"\n"+str(Player.MaxHealth)+"\n"+str(Player.CurHealth)+"\n"+Player.wearing+"\n"+Player.mainH+"\n")
                for x in range(0,len(Player.lnv)):
                    savefile.write(Player.lnv[x]+"\n")
                savefile.close()
            else:
                print("\ndon't be an idiot,dude...\n")
            print("\n"*10)
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def Stmenu(): #first meno(up on start up)   wip dictionery
    while 1<2:
        try:
            print("press 1 to Start a new game\npress 2 to Load save\npress 3 for Game info\npress 4 to Exit")
            izbor=int(input("please enter choise: "))
            if izbor == 1:
                Charcreat()
                break
            elif izbor == 2:
                fName=input("\nPlesease enter the name of the file you want to open(you ad the file extention): ")
                readfile=open(fName,'r')
                fcontent=readfile.readlines()
                Player.rasa=fcontent[0]
                Player.name=fcontent[1]
                Player.playerClass=fcontent[2]
                Player.stats["STR"]=int(fcontent[3])
                Player.stats["END"]=int(fcontent[4])
                Player.stats["DIP"]=int(fcontent[5])
                Player.stats["DEX"]=int(fcontent[6])
                Player.reputation=int(fcontent[7])
                Player.curcity=fcontent[8]
                Player.gold=int(fcontent[9])
                Player.MaxHealth=int(fcontent[10])
                Player.CurHealth=int(fcontent[11])
                Player.wearing=fcontent[12]
                Player.mainH=fcontent[13]
                Player.lnv[:]=[] #emptying inventory list
                for t in range(0, len(fcontent)-14): 
                    print(t)
                    Player.lnv.append(fcontent[t+14])
                readfile.close()
                Startgame()
            elif izbor == 3:
                print("\nwip")
                print("3\n\n\n")
            elif izbor == 4:
                break
            else:
                print("\ndon't be an idiot,dude...\n.")
            print("\n"*10)
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
def Startgame():
    print("\nYou start your adventure in the city of "+Player.curcity+"...")
    vrem=Time()
    while True:
        try:
            vrem.displayaTime()
            print("what do you do?\n1. go in arena\n2. go to Trade district\n3. go to tavern\n4. go to Bank \n5. go to cytadel X\n6.  roam the streats \n7. go ouyside the city walls \n8. charmenu \n9.ingame menu")
            izbor=int(input("please enter choise: "))
            if izbor == 1:
                vrem.incTime(1)#uvelichavam vremeto s 1
                Randinc(randint(1,100))
                Arena()
            elif izbor == 2:
                vrem.incTime(1)
                Randinc(randint(1,100))
                Market()
            elif izbor == 3:
                vrem.incTime(1)
                Randinc(randint(1,100))
                Tavern()
            elif izbor == 4:
                vrem.incTime(1)
                Randinc(randint(1,100))
                Bank()
            elif izbor == 5:
                vrem.incTime(1)
                print("\nwip palace")
                Randinc(randint(1,100))
            elif izbor == 6:
                vrem.incTime(1)
                print("\nwip streets")
                Randinc(randint(1,100))
                Randinc(randint(1,100))
            elif izbor == 7:
                vrem.incTime(1)
                Randinc(randint(1,100))
                outside()
            elif izbor == 8:
                playermenu("mainhub")
            elif izbor == 9:
                Igmenu()
            else:
                print("\ndon't be an idiot,dude...\n")
            print("\n")
        except ValueError:
            print("\ndon't be an idiot,dude...\n")
Stmenu()
Startgame()
#Igmenu()
print("\nkonq vleze v rqkata\n"+Player.rasa+" "+Player.name+" "+Player.playerClass)

