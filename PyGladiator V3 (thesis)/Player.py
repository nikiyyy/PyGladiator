from random import randint
from math import ceil
import Items 
import Nodeclass
import enemyParty
# import Effects 
# import os

class Player():
    race="human"
    name="stranger"
    max_movement_points=5
    movement_point=0
    maxEnergy=50
    curEnergy=maxEnergy
    worldmap=[]
    levelStage=1
    optionSettings=None
    equippedOH=None#Items.shield3 # off hand equipment
    equippedW=Items.weapon1#Items.weapon69 # Main hand equipment
    equippedA=Items.armour3
    stats={"STR":1,"END":1,"DIP":1,"DEX":1,"PER":1,"INT":1}
    skills={"One handed":25,"Two handed":5,"Throwing":5,"Shooting":5,"Blocking":5,"Heavy armour":5,"Medium armour":5,"Light armour":5,"Destruction magic":5,"Restoration magic":5}
    XP=0
    XPlevel=1
    XPcaps=(100,225,350,500,800,1300,1700,2400,3600,5000,10000)
    ability_points=10
    #Items.shield2,Items.potion1,Items.armour2,Items.weapon8,Items.shield2,Items.potion1,Items.armour2,Items.weapon8,Items.shield2,Items.potion1,Items.armour2,Items.weapon8
    Inventory=[Items.potion3]
    # effects=[]#{3:101},{15:101}
    enemiesOnMap=[]
    
    
    def __init__ (self,name,max_movement_points,maxHealth, gameSettings):
        self.name=name
        self.max_movement_points=max_movement_points
        self.movement_point=max_movement_points
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.Y_cord=randint(1,gameSettings.DIMENTIONS-1)
        self.X_cord=randint(1,gameSettings.DIMENTIONS-1)
        self.money=100
        self.optionSettings=gameSettings
        # self.cooldown()
    
    def loadFromFile(self,file):
    
        self.race=file[0][1]
        self.name=file[0][2]
        self.levelStage=file[0][3]
        self.max_movement_points=file[0][4]
        self.maxEnergy=file[0][5]
        self.maxHealth=file[0][6]
        self.curHealth=file[0][7]
        self.XPlevel=file[0][8]
        
        self.equippedOH=file[0][9]
        for i in Items.listOfAllItems:
            if file[0][9] == i.name:
                self.equippedOH=i
                break
        self.equippedW=file[0][10]
        for i in Items.listOfAllItems:
            if file[0][10] == i.name:
                self.equippedW=i
                break
        self.equippedA=file[0][11]
        for i in Items.listOfAllItems:
            if file[0][11] == i.name:
                self.equippedA=i
                break
        
        self.ability_points=file[0][14]
        self.money=file[0][15]
        self.XP=file[0][16]
        NamesInventory=file[0][17].split("/")
        NamesInventory=NamesInventory[1:]
        self.Inventory=[]
        for i in NamesInventory:
            for j in Items.listOfAllItems:
                if i==j.name:
                    self.Inventory.append(j)
        
        statsHolder=file[0][12].split("/")
        statsHolder=statsHolder[1:]
        
        skillHolder=file[0][13].split("/")
        skillHolder=skillHolder[1:]
        
        for i,j in zip(statsHolder,self.stats):
            self.stats[j]=int(i)
            
        for i,j in zip(skillHolder,self.skills):
            self.skills[j]=int(i)
            
        mapHolder = file[0][18].split("/")
        grid = []
        self.enemiesOnMap=[]
        gap = self.optionSettings.WIDTH // self.optionSettings.DIMENTIONS
        count=0 
        for i in range(self.optionSettings.DIMENTIONS):
            
            grid.append([])
            for j in range(self.optionSettings.DIMENTIONS):
                node = Nodeclass.Node(i, j, gap, self.optionSettings.DIMENTIONS)
                
                node.terrain=mapHolder[count][0]
                node.occupied=mapHolder[count][1]
                if node.occupied == "1":
                    print(node.row-1)
                    self.X_cord=node.row
                    self.Y_cord=node.col
                    
                elif node.occupied == "2":
                    EP=enemyParty.EnemyParty(randint(1, self.optionSettings.DIMENTIONS-1), randint(0, self.optionSettings.DIMENTIONS-1),1)
                    EP.startnode=node
                    self.enemiesOnMap.append(EP)
                    
                count+=1
                
                grid[i].append(node)
        self.worldmap = grid
             
            
    def reset(self):#when battle ends it resstes the map and position for the next fight
        self.curHealth=self.maxHealth
    
    
    def atribute_poins(self):#player updates his atribute points or checks his stats
       
        print("XP {}/{}\nLevel {}\nAtribute points {}".format(self.XP,self.XPcaps[self.XPlevel-1],self.XPlevel,self.ability_points))
        
        print("your skills are:")
        for i in self.skills: #prints all skills 
            print(i,Player.skills[i])
            
        print("STATS:\n1. Strenght: {}\n2. Endurance: {}\n3. Deplomacy: {}\n4. Dexterity: ".format(Player.stats["STR"],Player.stats["END"],Player.stats["DIP"],Player.stats["DEX"],Player.stats["PER"],Player.stats["INT"]))
        
        while self.ability_points != 0:# if you have 
            
            print("available points ".format(self.ability_points))
            print("STATS:\n1. Strenght: {}\n2. Endurance: {}\n3. Deplomacy: {}\n4. Dexterity: {}".format(Player.stats["STR"],Player.stats["END"],Player.stats["DIP"],Player.stats["DEX"]))
            izb=input("Whith stat do you wnat to increase?\nInput the corespoding number!")
            
            if izb=='1':#ups a chosen stat
                Player.stats["STR"]+=1
                self.ability_points-=1
                
            elif izb=='2':
                Player.stats["END"]+=1
                self.ability_points-=1
                self.maxHealth+=10
                
            elif izb=='3':
                Player.stats["DIP"]+=1
                self.ability_points-=1
                
            elif izb=='4':
                Player.stats["DEX"]+=1
                self.ability_points-=1
                self.max_movement_points+=1
        lol=input("Input E or e to exit")
    
    def Inventory_manage(self,Called_from):
        while True:
            print("gold: {}\n\nWearing {}\nMain hand {}\nOff hand {}\nhealth {}/{}\n".format(self.money,self.equippedA,self.equippedW,self.equippedOH,self.curHealth,self.maxHealth))
            
            for i in self.Inventory:
                print(i,"/ Value: ",i.value)
            izbor=int(input("\n1.Change armor\n2.Change weapon\n3.Use consumable\n4.Unequipn\n5.Delete item\n6.Exit\nInput the corespoding number or any other number to exit"))
            if izbor==1 :
                try:
                    available=[n for n in self.Inventory if isinstance(n,Items.C_armour)]
                    counter=0
                    for i in available:
                        print(counter,i,"/ Protection: ",i.defence,"/ Value: ",i.value )
                        counter+=1
                    izb_armor=input("Input the corespoding number or any other number to exit\n")
                    if self.equippedA!=None:
                        self.Inventory.append(self.equippedA)
                        self.equippedA=available[int(izb_armor)]
                        del self.Inventory[self.Inventory.index(available[int(izb_armor)])]
                    else:
                        self.equippedA=available[int(izb_armor)]
                        del self.Inventory[self.Inventory.index(available[int(izb_armor)])]
                except:
                    print("error")
                    
            elif izbor==2: 
                available=[n for n in self.Inventory if isinstance(n,Items.M_weapons) or isinstance(n,Items.C_shield) or isinstance(n,Items.R_weapons)]
                counter=0
                for i in available:
                    if isinstance(i,Items.R_weapons) or isinstance(i,Items.M_weapons) :
                        print(counter,i,"/ Power: ",i.damage,"/ Hands to use with:",i.hands,"/ Value: ",i.value)     
                    else: print(counter,i,"/ Defence: ",i.defence,"/ Value: ",i.value)     
                    counter+=1
                izb_weapon=input("Input the corespoding number\n")
                  #2 hands   
                if available[int(izb_weapon)].hands == 2:
                    if self.equippedW != None:
                        self.Inventory.append(self.equippedW)
                    if self.equippedOH != None:
                        self.Inventory.append(self.equippedOH)
                    self.equippedW=available[int(izb_weapon)]
                    self.equippedOH=None
                    del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                    #onehand
                else:   
                    if isinstance(available[int(izb_weapon)],Items.C_shield):
                        if self.equippedW != None and self.equippedW.hands==2:
                            self.Inventory.append(self.equippedW)
                            self.equippedW=None
                            self.equippedOH = available[int(izb_weapon)]
                            del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                        else:
                            if self.equippedOH != None:
                                self.Inventory.append(self.equippedOH)
                            self.equippedOH = available[int(izb_weapon)]
                            del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                    else:
                        izb_hand=input("\nDo you want to equip on main or off hand\n1.Main 2.Off hand")
                        if izb_hand == '1':
                            if self.equippedW != None:
                                self.Inventory.append(self.equippedW)
                            self.equippedW = available[int(izb_weapon)]
                            del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                        elif izb_hand == '2':
                            if self.equippedW != None and self.equippedW.hands == 2:
                                self.Inventory.append(self.equippedW)
                                self.equippedW = None
                                self.equippedOH = available[int(izb_weapon)]
                                del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                            else:
                                if self.equippedOH != None:
                                    self.Inventory.append(self.equippedOH)
                                self.equippedOH = available[int(izb_weapon)]
                                del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
    
            elif izbor==3: 
                available=[n for n in self.Inventory if isinstance(n,Items.C_consumable)]
                counter=0
                for i in available:
                    print(counter,i)                    
                    counter+=1
                izb_consum=input("Input the corespoding number\n")
                available[int(izb_consum)].use(self)
                del self.Inventory[self.Inventory.index(available[int(izb_consum)])]
                    
            elif izbor==4: 
                izb_uniq=input("1. Wearing: {}\n2. weaponMH: {}\n3. weaponOH: {}".format(self.equippedA,self.equippedW,self.equippedOH))
                if izb_uniq == '1':
                    if self.equippedA != None:
                        self.Inventory.append(self.equippedA)
                        self.equippedA = None
                        
                    else: print("nothing to unequip")
                    
                elif izb_uniq == '2':
                    if self.equippedW != None:
                        self.Inventory.append(self.equippedW)
                        self.equippedW = None
                        
                    else: print("nothing to unequip")
                    
                elif izb_uniq == '3':
                    if self.equippedOH != None:
                        self.Inventory.append(self.equippedOH)
                        self.equippedOH = None
                        
                    else: print("nothing to unequip")
                    
            elif izbor == 5:
                counter=0
                for i in self.Inventory:
                    print(counter,i)                    
                    counter+=1
                izb_delete=input("Input the corespoding number\n")
                conformation=input("are you susre you whant to delete {} \n1.Yes \n2.No".format(self.Inventory[int(izb_delete)]))
                if conformation == '1':
                    del self.Inventory[int(izb_delete)]
            elif izbor == 6:
                break
    
    def Dodege_chance(self):#s kakvo si oblechen,desxterity i level i se sravnqva sus hitchance na enemito
        #genirates a dodge chance the be pitted aginst enemie's hit chanse
        if self.equippedA == None:
            hitchanse=randint(7,12)+self.stats["DEX"]
            
        elif self.equippedA.armour_type == 'L' or self.equippedA.armour_type == 'C':
            hitchanse=randint(5,10)+self.stats["DEX"]+randint(0,self.skills["Light armour"]//6)
            
        elif self.equippedA.armour_type == 'M':
            hitchanse=randint(3,7)+self.stats["DEX"]+randint(0,self.skills["Medium armour"]//8)
            
        elif self.equippedA.armour_type == 'H':
            hitchanse=randint(0,5)+self.stats["DEX"]+randint(0,self.skills["Heavy armour"]//10)
            
        return (hitchanse+self.XPlevel)
    
    def Hit_chance(self):#genirates a hit chance to be pitted aginst enemy's dodge and block chance
        hitchanse=randint(1,21)
        
        if self.equippedW != None and isinstance(self.equippedW, Items.R_weapons):#used only if player uses a ranged weapon
            return hitchanse+self.XPlevel+ceil(self.stats["PER"]/2)
        
        else:
            if self.equippedW != None and self.equippedW.damage_type=='P' and hitchanse+5>=20:# used if player has a pearsing weapon, they have a crit bonus
                hitchanse+=5
                
            if hitchanse == 20:#the chance to genirate a crit chach is 1/20 
                return 1000
            
            return hitchanse+self.XPlevel+ceil(self.stats["DEX"]/2)#returns the value
    
    
    def cooldown(self):#used to recet thing like movement points for the next tirn
        print("vleze")
        self.movement_points=self.max_movement_points
        
    def genirate_damage(self): #genirates damage and ups a skill if luky
        
        skillDamage=0# genirates bonus weapon skill damage
            #for 1 hand
        if self.equippedW != None and self.equippedW.hands == 1:
            if isinstance(self.equippedW, Items.M_weapons):
                skillDamage=self.skills["One handed"]//10
            else:
                skillDamage=self.skills["Throwing"]//10
            #for 2 hands
        elif self.equippedW != None and self.equippedW.hands == 2:
            if isinstance(self.equippedW, Items.M_weapons):
                skillDamage=self.skills["Two handed"]//10
            else:
                skillDamage=self.skills["Shooting"]//10
            
            #for off hand
        if self.equippedOH != None:
            if isinstance(self.equippedOH, Items.M_weapons):
                skillDamage=self.skills["One handed"]//10
            elif isinstance(self.equippedOH,Items.R_weapons):
                skillDamage=self.skills["Throwing"]//10
        
        if self.equippedW==None:#if you have nothing equiped you return this value
            return randint(1,4)+self.stats["STR"]
        else: return randint(1,3)+randint(1,self.equippedW.damage)+self.stats["STR"]+skillDamage
        
    def genirate_damage_offhand(self):#used to genirare off hand damage
        if self.equippedOH==None or isinstance(self.equippedOH, Items.C_shield):#if there is no off hand weapon the namage is genirated
            return 0
        
        else: 
            return (randint(1,3)+self.equippedOH.damage+self.stats["STR"])//2
        
    def Block_chance(self):
            if isinstance(self.equippedOH, Items.C_shield):#if player has a shield this is used
                return randint(self.equippedOH.defence//2,self.equippedOH.defence)+randint(0,self.skills["Blocking"]//8)
            
            else: #if player has no shiled this is used
                return randint(0,5)+randint(0,self.skills["Blocking"]//10)
     
    def take_damage(self, enemy, crit = None):#when the player takes damage this is used
        damage=enemy.genirate_damage()#enemy genirates damage
        off_damage=enemy.genirate_damage_offhand()#genirates off hand damage if any
        
        if crit != None:#if the damege is critical the damage is multiplied by 2(determinade by enemy hit chanse)
            damage*=2
            
        if self.equippedA != None and (enemy.equippedW!=None and enemy.equippedOH!=None):
            #diermins if there is a bonus damage based on the armour that player is wearing
            if self.equippedA.armour_type == 'H' and enemy.equippedW.damage_type == 'B':
                print("using a blunt weapon extdadamage")
                damage*=1.25
                
            elif self.equippedA.armour_type == 'H' and enemy.equippedW.damage_type == 'S':
                print("using a sword agains heavy armour")
                damage*=0.75
                
            elif self.equippedA.armour_type == 'L' and enemy.equippedW.damage_type == 'S':
                print("using a sword agains light armour")
                damage*=1.25
                
            if off_damage != 0:
                if self.equippedA.armour_type == 'H' and enemy.equippedOH.damage_type == 'B':
                    print("using a blunt weapon extdadamage")
                    off_damage*=1.25
                    
                elif self.equippedA.armour_type == 'H' and enemy.equippedOH.damage_type == 'S':
                    print("using a sword agains heavy armour")
                    off_damage*=0.75
                    
                elif self.equippedA.armour_type == 'L' and enemy.equippedOH.damage_type == 'S':
                    print("using a sword agains light armour")
                    off_damage*=1.25
                    
                    #armour absorbs some of the damage
            if (damage+off_damage)-self.equippedA.defence//2 <=0:
                print(self.equippedA.name + " absorbes all the damage!")
            else:
                print(self.equippedA.name + " blocks "+ str((damage+off_damage)-self.equippedA.defence//2) + " damage!")
                self.curHealth-=(damage+off_damage)-self.equippedA.defence//2

        else:
            self.curHealth-=(damage+off_damage)*2 
             
        #ima shans da uvelichi nqkoi stat
        increase=randint(0,10)
        if increase == 0 and self.equippedA != None and self.equippedA.armour_type=='L':
            self.skills["Light armour"]+=1
            
        elif increase == 0 and self.equippedA != None and self.equippedA.armour_type=='M':
            self.skills["Medium armour"]+=1
            
        elif  increase == 0 and self.equippedA != None and self.equippedA.armour_type=='H':
            self.skills["Heavy armour"]+=1
            
        if self.equippedOH!= None and isinstance(self.equippedOH, Items.C_shield):
                self.skills["Blocking"]+=1
                        
                
    def compressDictValues(self,toBeComp):#used to compress the skills and stats of the player in to a string that is used to represt starts in a databace
        compressed=""
        for i in list(toBeComp.values()):
            compressed+="/"+str(i)
        return compressed
    
    def compressInventory(self):#used to compress the inventory of th e player into a string usig the item id's
        compressed=""
        for i in self.Inventory:
            compressed+="/"+str(i.name)
        return compressed
    
    def compressWorldmap(self):
        compressed=""
        for i in self.worldmap:
            for j in i:
                compressed+= j.terrain + j.occupied + "/"
        return compressed