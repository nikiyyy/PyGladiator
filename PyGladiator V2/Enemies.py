from random import randint

from math import ceil
import combat
import Items 

class Enemy(): #enemy e baseclass koto se nasledqva ot vsichko protivnici
    
    maxHealth=30
    curHealth=maxHealth
    def __init__(self,name=None):
        self.name=name
        self.gen_inventory
        self.level=1
        self.alive=True
        self.Y_cord=0
        self.X_cord=0
        self.movement_points=2
        self.armor=2
        self.inventory=[]
        self.color=0
        self.equippedW=None
        self.equippedOH=None
        self.equippedA=None
        self.stats={"STR":5,"END":5,"DIP":5,"DEX":5,"PER":5,"INT":5}
        skills={"One handed":5,"Two handed":5,"Throwing":5,"Shooting":5,"Blocking":5,"Heavy armour":5,"Medium armour":5,"Light armour":5,"Destruction magic":5,"Restoration magic":5}
    
    def action(self,karta,pobj):
        choise=randint(0,10)
        if self.curHealth<self.maxHealth/2 and (Items.potion1 in self.inventory or Items.potion2 in self.inventory or Items.potion3 in self.inventory):
            availible=[i for i in self.inventory if isinstance(i,Items.C_consumable)]
            availible[0].use(self)
            del self.inventory[self.inventory.index(availible[0])]
        else:
        
            #damage=0
            combat.Attack(self, pobj)
            #if self.equippedW != None:
                
                #damage=self.genirate_damage()
                #pobj.curHealth-=damage
                #print("ENEMY Deals "+str(damage) +" damage with "+ self.equippedW.name)
                
            #else:
                #pobj.curHealth-=randint(1,5)
                #print("ENEMY ATTACKS! with fists")
                
    def take_damage(self, player, crit = None):
        damage=player.genirate_damage()
        off_damage=player.genirate_damage_offhand()
        print("offhand damage",off_damage)
        if crit != None:
            damage*=2
            
        if self.equippedA != None:

            if player.equippedW==None:
                pass
            elif self.equippedA.armour_type == 'H' and player.equippedW.damage_type == 'B':
                print("using a blunt weapon extdadamage")
                damage*=1.25
            elif self.equippedA.armour_type == 'H' and player.equippedW.damage_type == 'S':
                print("using a sword agains heavy armour")
                damage*=0.75
            elif self.equippedA.armour_type == 'L' and player.equippedW.damage_type == 'S':
                print("using a sword agains light armour")
                damage*=1.25
            if off_damage != 0:
                if self.equippedA.armour_type == 'H' and player.equippedOH.damage_type == 'B':
                    print("using a blunt weapon extdadamage")
                    off_damage*=1.25
                elif self.equippedA.armour_type == 'H' and player.equippedOH.damage_type == 'S':
                    print("using a sword agains heavy armour")
                    off_damage*=0.75
                elif self.equippedA.armour_type == 'L' and player.equippedOH.damage_type == 'S':
                    print("using a sword agains light armour")
                    off_damage*=1.25

            if (damage+off_damage)-self.equippedA.defence//2 <=0:
                print(self.equippedA.name + " absorbes all the damage!")
            else:
                print(self.equippedA.name + " blocks "+ str((damage+off_damage)-self.equippedA.defence//2) + " damage!")
                self.curHealth-=(damage+off_damage)-self.equippedA.defence//2

        ### increase player skills 
            #for main hand
        if player.equippedW != None and player.equippedW.hands == 1:
            if isinstance(player.equippedW, Items.M_weapons):
                player.skills["One handed"]+=1
            else:
                player.skills["Throwing"]+=1
                
        elif player.equippedW != None and player.equippedW.hands == 2:
            if isinstance(player.equippedW, Items.M_weapons):
                player.skills["Two handed"]+=1
            else:
                player.skills["Shooting"]+=1
            
            #for off hand
        if player.equippedOH != None:
            if isinstance(player.equippedOH, Items.M_weapons):
                player.skills["One handed"]+=1
            elif isinstance(player.equippedOH,Items.R_weapons):
                player.skills["Throwing"]+=1
                
        ###
        else:
            self.curHealth-=(damage+off_damage)*2
        if self.curHealth<=0:
            player.combatmap=self.died(player.combatmap)        

    def genirate_damage(self):
        if self.equippedW==None:
            return randint(1,3)+self.stats["STR"]
        else: return randint(1,3)+self.equippedW.damage+self.stats["STR"]
        
    def genirate_damage_offhand(self):
        if self.equippedOH==None or isinstance(self.equippedOH, Items.R_weapons) or isinstance(self.equippedOH, Items.C_shield):
            return 0
        else: return (randint(1,3)+self.equippedOH.damage+self.stats["STR"])//2    
        
    def died(self,karta):
        karta[self.Y_cord][self.X_cord]="1"
        self.movement_points=0    
        self.alive=False
        self.curHealth=0
        return karta
    
    def printme(self):
            print('|▓▓', end = '')


    def gen_inventory(self):
        
        weapon_var=randint(0,5)
        if weapon_var==0: # 2 weapons
            availible=[i for i in Items.Mweapons if i.hands==1]
            
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedW=availible[weapon_var]
            
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedOH=availible[weapon_var]
            
        elif weapon_var==1: # main hand 
            
            availible=[i for i in Items.Mweapons if i.hands==1]
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedW=availible[weapon_var]
            
        elif weapon_var==2: # main hand and shield
            
            availible=[i for i in Items.Mweapons if i.hands==1]
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedW=availible[weapon_var]
            
            weapon_var=randint(0,len(Items.Shield)-1)
            self.inventory.append(Items.Shield[weapon_var])
            self.equippedOH=Items.Shield[weapon_var]
            
        elif weapon_var==3: # 2h weapon
            
            availible=[i for i in Items.Mweapons if i.hands==2]
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedW=availible[weapon_var]
            
        elif weapon_var==4: # 2h ranged weapon
            
            availible=[i for i in Items.Ranged_weapons if i.hands==2]
            weapon_var=randint(0,len(availible)-1)
            self.inventory.append(availible[weapon_var])
            self.equippedW=availible[weapon_var]
            
        else: print("no weapons")
        
        armor_var=randint(0,9)
        self.inventory.append(Items.Armour[armor_var])
        self.equippedA=Items.Armour[armor_var]
        
        if (armor_var+weapon_var)%2==0:
            print("potion detected")
            self.inventory.append(Items.pations[randint(0,len(Items.pations)-1)])

    
    def Dodege_chance(self):#s kakvo si oblechen,desxterity i level i se sravnqva sus hitchance na enemito
        if self.equippedA == None:
            hitchanse=randint(7,12)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'L' or self.equippedA.armour_type == 'C':
            hitchanse=randint(5,10)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'M':
            hitchanse=randint(3,7)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'H':
            hitchanse=randint(0,5)+self.stats["DEX"]
        return (hitchanse+self.level)
    
    def Block_chance(self):
        if isinstance(self.equippedOH, Items.C_shield):
            return randint(self.equippedOH.defence//2,self.equippedOH.defence)
        else: return randint(0,5)
        
    def Hit_chance(self):
        hitchanse=randint(1,21)
        return hitchanse+self.level+ceil(self.stats["DEX"]/2)
    
    def move(self,karta,pobj):#PX,PY
        try:            
            #print("\nDebug\n"+"player X "+str(pobj.X_cord)+" player Y "+str(pobj.Y_cord)+"\n ENEMY X "+str(self.X_cord)+"ENEMY Y "+str(self.Y_cord)+"Debug")
            while self.movement_points>0:
                
                if self.equippedW!=None and isinstance(self.equippedW,Items.R_weapons):
                    self.action(karta,pobj)
                    break
                #diagonalno dvijenie
                if self.Y_cord > pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord-1] == "3" or karta[self.Y_cord-1][self.X_cord-1] == "0":
                        #print("\nobsticleA")
                        if karta[self.Y_cord-1][self.X_cord] == "1" :
                            #print("\nobsticleA1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1" :
                            #print("\nobsticleA2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleA3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord-1] == "2":
                        #print("\nearplayerA")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord-=1
                    self.movement_points-=1
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if  karta[self.Y_cord+1][self.X_cord+1] == "3" or karta[self.Y_cord+1][self.X_cord+1] == "0":
                        #print("\nobsticleB")
                        if karta[self.Y_cord+1][self.X_cord] == "1":
                            #print("\nobsticleB1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord+1] == "1":
                            #print("\nobsticleB2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleB3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord+1][self.X_cord+1] == "2":
                        #print("\nearplayerB")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord > pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord+1] == "3" or karta[self.Y_cord-1][self.X_cord+1] == "0":
                        #print("\nobsticleC")
                        if karta[self.Y_cord-1][self.X_cord] == "1":
                            #print("\nobsticleC1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1":
                            #print("\nobsticleC2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleC3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord+1] == "2":
                        #print("nearplayerC")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord+1][self.X_cord-1] == "3" or karta[self.Y_cord+1][self.X_cord-1] == "0":
                         #print("\nobsticleD")
                         if karta[self.Y_cord+1][self.X_cord] == "1":
                            #print("\nobsticleD1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                         elif karta[self.Y_cord][self.X_cord-1] == "1":
                           #print("\nobsticleD2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                         else:
                            #print("\nobsticleD3")
                            break
                         karta[self.Y_cord][self.X_cord]="3"
                         continue
                    
                    #enqountered player
                    elif karta[self.Y_cord+1][self.X_cord-1] == "2":
                        #print("\nearplayerD")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.X_cord-=1
                    self.movement_points-=1
                 #single axis movement
                elif self.Y_cord > pobj.Y_cord :
                    if karta[self.Y_cord-1][self.X_cord] == "3" or karta[self.Y_cord-1][self.X_cord] == "0":
                        #print("\nobsticleE")
                        if karta[self.Y_cord-1][self.X_cord-1] == "1":
                            #print("\nobsticleE2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            #print("\nobsticleE1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleE3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord] == "2":
                         #print("\nearplayerE")
                         if self.movement_points>0:
                             self.action(karta,pobj)
                         break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.movement_points-=1
                
                
                elif self.Y_cord < pobj.Y_cord :
                    if karta[self.Y_cord+1][self.X_cord] == "3" or karta[self.Y_cord+1][self.X_cord] == "0":
                        #print("\nobsticleF")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            #print("\nobsticleF2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord+1][self.X_cord+1] == "1":
                            #print("\nobsticleF1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleF3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord+1][self.X_cord] == "2":
                        #print("nearplayerF")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.movement_points-=1
                    
                elif self.X_cord > pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord-1] == "3" or karta[self.Y_cord][self.X_cord-1] == "0":
                        #print("\nobsticleG")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            #print("\nobsticleG1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord-1] == "1":
                            #print("\nobsticleG2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleG3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    if karta[self.Y_cord][self.X_cord-1] == "2":
                        #print("\nearplyerG")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.X_cord-=1
                    self.movement_points-=1  
                    
                elif self.X_cord < pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord+1] == "3" or karta[self.Y_cord][self.X_cord+1] == "0":
                        #print("\nobsticleH")
                        if karta[self.Y_cord+1][self.X_cord+1] == "1":
                            #print("\nobsticleH1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            #print("\nobsticleH2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleH3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord][self.X_cord+1] == "2":
                        #print("\nearplayerH")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.X_cord+=1
                    self.movement_points-=1
                else:
                    break
    
                karta[self.Y_cord][self.X_cord]="3"
            if self.alive==True:
                self.movement_points=2
            return karta
        except IndexError:
            return karta
    
class Placeholder(Enemy):
    maxHealth=0
    curHealth=maxHealth
    xp_reward=0
    gold_reward=0

    
class Thug(Enemy):
    maxHealth=50
    curHealth=maxHealth
    xp_reward = randint(10,20)
    gold_reward=randint(2,6)
    
class Bandit(Enemy):
    maxHealth=60
    curHealth=maxHealth
    xp_reward = randint(15,30)
    gold_reward=randint(4,10)
    
class Pit_Fighter(Enemy):
    maxHealth=70
    curHealth=maxHealth
    xp_reward = randint(20,40)
    gold_reward=randint(6,14)
        
class Guard(Enemy):
    maxHealth=80
    curHealth=maxHealth
    xp_reward = randint(30,60)
    gold_reward=randint(8,18)
