#from random import randint #izpolzva se za generorane na proizvolni chesla
import os
import GenirateMap as GM
import Enemies as EN
import Items
#import Player as PL        



def Attack(obj1, obj2):
    hitchanse=obj1.Hit_chance()
    dodgechance=obj2.Dodege_chance()
    blockchanse=obj2.Block_chance()
    #print("{} rolls hitchanse {}".format(obj1.name,hitchanse))
    #print(obj2.name + " rolls dodgechance " + str(dodgechance))
    #print(obj2.name + " rolls blockchance " + str(blockchanse))
    if hitchanse == 1000:
        obj2.take_damage(obj1,"crit")
    elif hitchanse>=dodgechance:
        if hitchanse>=blockchanse:
            obj2.take_damage(obj1)
            print("Hit!")
        else: print("Block!")
    else: print("Miss!")


#kogato ima bitka se izvikva funciqta Combat(), tq e pulna sus argumenti koito imat defaltni stoinoti kogato ne se izpolzvat
def Combat(player,combNum,emem1type,enemNam1=None,emem2type=None,enemNam2=None,emem3type=None,enemNam3=None,emem4type=None,enemNam4=None,emem5type=None,enemNam5=None):
#combNum e broq na opunentite za tzi butka
#emem1type priema za argument tipa protivnik
#enemNam1 se izpolzva samo ako protivnika ima specialno ime
    player.reset()
    #paceholder obekti za protivnicite 
    enem1=EN.Placeholder("ph")
    enem2=EN.Placeholder("ph")
    enem3=EN.Placeholder("ph")
    enem4=EN.Placeholder("ph")
    enem5=EN.Placeholder("ph")
    
    tirn=0
    
    #tuk se izbira tipa i imeto na opunenta
    if emem1type == "Thug":
        enem1=EN.Thug(enemNam1)
    elif emem1type == "Bandit":
        enem1=EN.Bandit(enemNam1)
    elif emem1type == "Pit_Fighter":
        enem1=EN.Pit_Fighter(enemNam1)
    # 
    if enem1.name==None: 
        enem1.name=emem1type
    enem1.gen_inventory()

    if combNum>1:
        if emem2type == "Thug":
            enem2=EN.Thug()
        elif emem2type == "Bandit":
            enem2=EN.Bandit()
        elif emem2type == "Pit_Fighter":
            enem2=EN.Pit_Fighter() 
        enem2.name=emem2type 
        enem2.gen_inventory()
        # 
        if enem2.name==None: 
            enem2.name=emem2type  
#
    if combNum>2:
        if emem3type == "Thug":
            enem3=EN.Thug()
        elif emem3type == "Bandit":
            enem3=EN.Bandit()
        elif emem3type == "Pit_Fighter":
            enem3=EN.Pit_Fighter() 
        enem3.name=emem3type 
        enem3.gen_inventory()
        # 
        if enem3.name==None: 
            enem3.name=emem3type
#
    if combNum>3:
        if emem4type == "Thug":
            enem4=EN.Thug()
        elif emem4type == "Bandit":
            enem4=EN.Bandit()
        elif emem4type == "Pit_Fighter":
            enem4=EN.Pit_Fighter() 
        enem4.name=emem4type 
        enem4.gen_inventory()
        # 
        if enem4.name==None: 
            enem4.name=emem4type
#
    if combNum>4:
        if emem5type == "Thug":
            enem5=EN.Thug()
        elif emem5type == "Bandit":
            enem5=EN.Bandit()
        elif emem5type == "Pit_Fighter":
            enem5=EN.Pit_Fighter() 
        enem5.name=emem5type 
        enem5.gen_inventory()
        #
        if enem5.name==None: 
            enem5.name=emem5type
       
    #opredelq cveta na vseki protivnik
    izbor_sur=0#exit 
    while enem1.curHealth>0 or enem2.curHealth>0 or enem3.curHealth>0 or enem4.curHealth>0 or enem5.curHealth>0:
        if izbor_sur==1:
            break

        while enem1.curHealth>0 or enem2.curHealth>0 or enem3.curHealth>0 or enem4.curHealth>0 or enem5.curHealth>0:# player's turn
            
            
            if player.curHealth<=0:
                izbor_sur=1
                break
            while True:
                try:    #izkarva atrebutite na protivnicite
                    GM.genmap(15,15,5,objpass=player,enemnum=combNum,caller=0,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
                    print("Tirn number: {}".format(tirn))
                    
                    if enem1.curHealth>0:
                        print('1- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem1.name,enem1.curHealth,enem1.maxHealth,enem1.equippedA.name,enem1.equippedW,enem1.equippedOH))
                    if combNum>1:
                        if enem2.curHealth>0:
                            print('2- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem2.name,enem2.curHealth,enem2.maxHealth,enem2.equippedA.name,enem2.equippedW,enem2.equippedOH))
                        if combNum>2:
                            if enem3.curHealth>0:
                                print('3- Enemy: {} - Health: {}/{} - wearing - {} -  mainhand - {} offhand - {}'.format(enem3.name,enem3.curHealth,enem3.maxHealth,enem3.equippedA.name,enem3.equippedW,enem3.equippedOH))
                            if combNum>3:
                                if enem4.curHealth>0:
                                    print('4- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem4.name,enem4.curHealth,enem4.maxHealth,enem4.equippedA.name,enem4.equippedW,enem4.equippedOH))
                                if combNum>4:
                                    if enem5.curHealth>0:
                                        print('5- Enemy: {} - Health: {}/{} - wearing - {} -  mainhand - {} offhand - {}'.format(enem5.name,enem5.curHealth,enem5.maxHealth,enem5.equippedA.name,enem5.equippedW,enem5.equippedOH))
                                 
                                    
                    #menu selector
                    print("\nYour Health : {}/{}".format(player.curHealth,player.maxHealth))
                        
                    izbor=int(input("\n1 - Move \n2 - Attack\n3 - Use item\n4 - End tirn\n5 - Surrender\nInput the coresponding number\n"))
                    if izbor == 1:#move - generira karta v nachaloto na bitkata 
                        GM.genmap(15,15,5,objpass=player,enemnum=combNum,caller=1,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
                    #(X,Y,Grubost na terena (5MAX),tekuchtata karta se zapamenqva v classa na igracha,broi vragove, kogato caller e 1 genmap e povikana ot igracha kogato e 0 e povikana ot protivnik, podavam enemy obektite)
                    elif izbor == 2: #igracha si izbira koi da atakuva
                        if enem1.curHealth>0 and (player.am_i_touching(enem1,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            print('1- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem1.name,enem1.curHealth,enem1.maxHealth,enem1.equippedA.name,enem1.equippedW,enem1.equippedOH))
                        if combNum>1:
                            if enem2.curHealth>0 and (player.am_i_touching(enem2,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                                print('2- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem2.name,enem2.curHealth,enem2.maxHealth,enem2.equippedA.name,enem2.equippedW,enem2.equippedOH))
                            if combNum>2:
                                if enem3.curHealth>0 and (player.am_i_touching(enem3,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                                     print('3- Enemy: {} - Health: {}/{} - wearing - {} -  mainhand - {} offhand - {}'.format(enem3.name,enem3.curHealth,enem3.maxHealth,enem3.equippedA.name,enem3.equippedW,enem3.equippedOH))
                                if combNum>3:
                                    if enem4.curHealth>0 and (player.am_i_touching(enem4,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                                        print('4- Enemy: {} - Health: {}/{} - wearing - {} - mainhand - {} offhand - {}'.format(enem4.name,enem4.curHealth,enem4.maxHealth,enem4.equippedA.name,enem4.equippedW,enem4.equippedOH))
                                    if combNum>4:
                                        if enem5.curHealth>0 and (player.am_i_touching(enem5,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                                            print('5- Enemy: {} - Health: {}/{} - wearing - {} -  mainhand - {} offhand - {}'.format(enem5.name,enem5.curHealth,enem5.maxHealth,enem5.equippedA.name,enem5.equippedW,enem5.equippedOH))
                            
                        izbor_Atk=int(input("6. Back"))
                        
                        if izbor_Atk==1 and enem1.curHealth>0 and (player.am_i_touching(enem1,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            Attack(player, enem1)
                            break
                        elif izbor_Atk==1 and enem1.curHealth<=0: print("target unavalable")
                        if izbor_Atk==2 and enem2.curHealth>0 and (player.am_i_touching(enem2,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            Attack(player, enem2)
                            break
                        elif izbor_Atk==2 and enem2.curHealth<=0: print("target unavalable")
                        if izbor_Atk==3 and enem3.curHealth>0 and (player.am_i_touching(enem3,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            Attack(player, enem3)
                            break
                        elif izbor_Atk==3 and enem3.curHealth<=0: print("target unavalable")
                        if izbor_Atk==4 and enem4.curHealth>0 and (player.am_i_touching(enem4,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            Attack(player, enem4)
                            break
                        elif izbor_Atk==4 and enem4.curHealth<=0: print("target unavalable")
                        if izbor_Atk==5 and enem5.curHealth>0 and (player.am_i_touching(enem5,player.combatmap) or (player.equippedW!=None and isinstance(player.equippedW,Items.R_weapons))):
                            Attack(player, enem5)
                            break
                        elif izbor_Atk==5 and enem5.curHealth<=0: print("target unavalable")
                        if izbor_Atk==6:
                            pass
                    elif izbor == 3:
                        player.Inventory_manage("menu")
                    elif izbor == 4:
                        break
                        print("Your tirn ends")
                    elif izbor == 5:
                        izbor_sur=int(input("Are you sure you want to surrender?\1 - yes\2 - no"))
                        if izbor_sur==1:
                            return 
                except ValueError:
                    print("Invalid Input")
            os.system('cls')        
            print("enemy tirn\n")
            tirn+=1
            player.cooldown()#refreshva cooldowns na player
            if enem1!=None:
                GM.genmap(15,15,5,objpass=player,caller=2,enemnum=combNum,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5) 
                #protivnicite pravqt hod
    os.system('cls') 
    if player.curHealth>0:
        player.get_xp((enem1.xp_reward+enem2.xp_reward+enem3.xp_reward+enem4.xp_reward+enem5.xp_reward))
        player.get_gold((enem1.gold_reward+enem2.gold_reward+enem3.gold_reward+enem4.gold_reward+enem5.gold_reward))
        player.spoils_of_war(enem1,enem2,enem3,enem4,enem5)
    else:
        lol=input(print("you were Defeated!\ninput E to exit! "))