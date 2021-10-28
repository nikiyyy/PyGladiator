import pygame as pg
import Button
import Inventory
# import Menu
import Items
import CRUD
import screens
from random import randint
pg.init()
# background = pg.image.load("market.png")

def deathscreen(player, screen):
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[5], (0,0))   
    newgameButton = Button.button(120, 600 ,150 ,40,"New game", "white", screen, 40) 
    loadButton = Button.button(320, 600 ,150 ,40,"Load game", "white", screen, 40)
    exitButton = Button.button(520, 600 ,150 ,40, "Exit","white",screen, 40)
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[7], (0,0))
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif newgameButton.draw_button():
                #reset player
                screens.charcreation(screen, player)
                return
            elif loadButton.draw_button():
                CRUD.CRUD(screen, player, 1)
                return
            elif exitButton.draw_button():
                pg.quit()
        pg.display.update()
    
     
        
def drawBattleMenu(screen,player,enemies):
    player.optionSettings.myfont = pg.font.SysFont("monospace", 15)
    screen.blit(pg.image.load("sprites/border.png").convert_alpha(), (0, 550))
    screen.blit(player.optionSettings.myfont.render("Player Health: "+str(player.curHealth)+"/"+str(player.maxHealth), 1, (0,0,0)), (300, 600)) 
    
    # inventorybutton = Button.button(40, 570 ,150 ,40, "Inventory" ,"black", screen, 40)
    screen.blit(pg.font.SysFont("Monotype Corsiva", 40).render("Inventory", 1, (0,0,0)), (70, 580)) 
    # spacialAttack = Button.button(40, 630 ,150 ,40, "Mass Attack" ,"black", screen, 40) 
    screen.blit(pg.font.SysFont("Monotype Corsiva", 40).render("Mass Attack", 1, (0,0,0)), (70, 640)) 
    # doNothingButton = Button.button(40, 690 ,150 ,40,"Do nothing", "black", screen, 40) 
    screen.blit(pg.font.SysFont("Monotype Corsiva", 40).render("Do nothing", 1, (0,0,0)), (70, 700)) 
    # runButton = Button.button(40, 750 ,150 ,40,"Run Away", "black", screen, 40) 
    screen.blit(pg.font.SysFont("Monotype Corsiva", 40).render("Run Away", 1, (0,0,0)), (70, 760)) 
    
    if len(enemies) == 1:
        screen.blit(player.optionSettings.myfont.render("Enemy 1: "+str(enemies[0].curHealth)+"/"+str(enemies[0].maxHealth), 1, (0,0,0)), (540, 680)) 
    elif len(enemies) == 2:
        screen.blit(player.optionSettings.myfont.render("Enemy 1: "+str(enemies[0].curHealth)+"/"+str(enemies[0].maxHealth), 1, (0,0,0)), (540, 680)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 2: "+str(enemies[1].curHealth)+"/"+str(enemies[1].maxHealth), 1, (0,0,0)), (600, 720)) 
    elif len(enemies) == 3:
        screen.blit(player.optionSettings.myfont.render("Enemy 1: "+str(enemies[0].curHealth)+"/"+str(enemies[0].maxHealth), 1, (0,0,0)), (540, 680)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 2: "+str(enemies[1].curHealth)+"/"+str(enemies[1].maxHealth), 1, (0,0,0)), (600, 640)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 3: "+str(enemies[2].curHealth)+"/"+str(enemies[2].maxHealth), 1, (0,0,0)), (600, 720)) 
    elif len(enemies) == 4:
        screen.blit(player.optionSettings.myfont.render("Enemy 1: "+str(enemies[0].curHealth)+"/"+str(enemies[0].maxHealth), 1, (0,0,0)), (540, 680)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 2: "+str(enemies[1].curHealth)+"/"+str(enemies[1].maxHealth), 1, (0,0,0)), (600, 640)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 3: "+str(enemies[2].curHealth)+"/"+str(enemies[2].maxHealth), 1, (0,0,0)), (600, 720)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 4: "+str(enemies[3].curHealth)+"/"+str(enemies[3].maxHealth), 1, (0,0,0)), (540, 740)) 
    elif len(enemies) == 5:
        screen.blit(player.optionSettings.myfont.render("Enemy 1: "+str(enemies[0].curHealth)+"/"+str(enemies[0].maxHealth), 1, (0,0,0)), (540, 680)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 2: "+str(enemies[1].curHealth)+"/"+str(enemies[1].maxHealth), 1, (0,0,0)), (600, 720)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 3: "+str(enemies[2].curHealth)+"/"+str(enemies[2].maxHealth), 1, (0,0,0)), (600, 640)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 4: "+str(enemies[3].curHealth)+"/"+str(enemies[3].maxHealth), 1, (0,0,0)), (540, 740)) 
        screen.blit(player.optionSettings.myfont.render("Enemy 5: "+str(enemies[4].curHealth)+"/"+str(enemies[4].maxHealth), 1, (0,0,0)), (540, 600)) 
        
    
def attack(obj1, obj2):
    hitchanse=obj1.Hit_chance()
    dodgechance=obj2.Dodege_chance()
    blockchanse=obj2.Block_chance()
    # print("{} rolls hitchanse {}".format(obj1.name,hitchanse))
    # print(obj2.name + " rolls dodgechance " + str(dodgechance))
    # print(obj2.name + " rolls blockchance " + str(blockchanse))
    # if hitchanse == 1000:
    #     print("Crit!")
    #     obj2.curHealth-=20
    if hitchanse>=dodgechance:
        if hitchanse>=blockchanse:
            obj2.take_damage(obj1)
            print("Hit!")
        else: print("Block!")
    else: print("Miss!")
    
def specialAttack(obj1, obj2):
    obj2.curHealth-=randint(0,3)+obj1.XPlevel

    

def stratcombat(screen,player,enemies):
    
    
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[5], (0,0))   
    if len(enemies) >= 1:
        enemy1 = Button.button(540, 220 ,100 ,100, "{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
    if len(enemies) >= 2:
        enemy2 = Button.button(600, 100 ,100 ,100, "{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
    if len(enemies) >= 3:
        enemy3 = Button.button(600, 340 ,100 ,100, "{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
    if len(enemies) >= 4:
        enemy4 = Button.button(540, 20 ,100 ,100, "{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha())
    if len(enemies) >= 5:
        enemy5 = Button.button(540, 460 ,100 ,100, "{} - {}/{}".format(enemies[4].name,enemies[4].curHealth,enemies[4].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
    
    # screen.blit(myfont.render(str(player.curHealth)+"/"+str(player.maxHealth), 1, (255,255,255)), (40, 260))
    playerbutton = Button.button(20, 260 ,100 ,100, "{} - {}/{}".format(player.name,player.curHealth,player.maxHealth),"red", screen, pg.image.load('sprites/Idle.png').convert_alpha()) 
    
    inventorybutton = Button.button(40, 570 ,150 ,40, "Inventory" ,"black", screen, 40)
    spacialAttack = Button.button(40, 630 ,150 ,40, "Mass Attack" ,"black", screen, 40) 
    doNothingButton = Button.button(40, 690 ,150 ,40,"Do nothing", "black", screen, 40) 
    runButton = Button.button(40, 750 ,150 ,40,"Run Away", "black", screen, 40) 
    run = True
    while run:
        if len(enemies) >= 1:
            if enemies[0].curHealth > 0 :
                enemy1 = Button.button(540, 260 ,100 ,100, "{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
            else: 
                enemy1 = Button.button(540, 260 ,100 ,100, "{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth),"red", screen, pg.image.load('sprites/deadenemy.png').convert_alpha()) 
        
        if len(enemies) >= 2:
            if enemies[1].curHealth > 0 :
                enemy2 = Button.button(600, 140 ,100 ,100, "{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha())
            else: 
                enemy2 = Button.button(600, 140 ,100 ,100, "{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth),"red", screen, pg.image.load('sprites/deadenemy.png').convert_alpha()) 
            
        if len(enemies) >= 3:
            if enemies[2].curHealth > 0 :
                enemy3 = Button.button(600, 380 ,100 ,100, "{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
            else: 
                enemy3 = Button.button(600, 380 ,100 ,100, "{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth),"red", screen, pg.image.load('sprites/deadenemy.png').convert_alpha())  
        if len(enemies) >= 4:
            if enemies[3].curHealth > 0 :
                enemy4 = Button.button(540, 20 ,100 ,100, "{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha())
            else: 
                enemy4 = Button.button(540, 20 ,100 ,100, "{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth),"red", screen, pg.image.load('sprites/deadenemy.png').convert_alpha())  

        if len(enemies) >= 5:
            if enemies[4].curHealth > 0 :
                enemy5 = Button.button(540, 500 ,100 ,100, "{} - {}/{}".format(enemies[4].name,enemies[4].curHealth,enemies[4].maxHealth),"red", screen, pg.image.load('sprites/enidle.png').convert_alpha()) 
            else: 
                enemy5 = Button.button(540, 500 ,100 ,100, "{} - {}/{}".format(enemies[4].name,enemies[4].curHealth,enemies[4].maxHealth),"red", screen, pg.image.load('sprites/deadenemy.png').convert_alpha())   
        
        # screen.blit(player.optionSettings.BGs[5], (0,0))
        drawBattleMenu(screen, player, enemies)
        # enemy1.draw_button()
        # enemy2.draw_button()
        # drawBattleMenu(screen, player, enemies)
            
        if player.curHealth <= 0:
            return True

        elif len(enemies) == 1 and enemies[0].curHealth <= 0:
            player.money+=enemies[0].rewardGold()
            player.XP+=enemies[0].rewardXP()
            
            return False
        elif len(enemies) == 2 and enemies[0].curHealth + enemies[1].curHealth <= 0:
            for i in enemies:
                player.money+=i.rewardGold()
                player.XP+=i.rewardXP()
            return False
        elif len(enemies) == 3 and enemies[0].curHealth + enemies[1].curHealth + enemies[2].curHealth <= 0:
            for i in enemies:
                player.money+=i.rewardGold()
                player.XP+=i.rewardXP()
            return False
        elif len(enemies) == 4 and enemies[0].curHealth + enemies[1].curHealth + enemies[2].curHealth + enemies[3].curHealth <= 0:
            for i in enemies:
                player.money+=i.rewardGold()
                player.XP+=i.rewardXP()
            return False
        elif len(enemies) == 5 and enemies[0].curHealth + enemies[1].curHealth + enemies[2].curHealth + enemies[3].curHealth + enemies[4].curHealth <= 0:
            for i in enemies:
                player.money+=i.rewardGold()
                player.XP+=i.rewardXP()
            return False
        
    # 	#draw panel
    # 	draw_panel()
        enemytirn= False
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if len(enemies) >= 1 and enemy1.draw_button():
                enemytirn=True
                attack(player, enemies[0])
                
                if player.equippedW != None and isinstance(player.equippedW,Items.M_weapons) and randint(0,2)==0: # retaliation
                    attack(enemies[0], player)
                #attack(enemy1)
            elif len(enemies) >= 2 and enemy2.draw_button():
                # enemies[1].curHealth-=10
                enemy2.text_setter("{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth))
                enemytirn=True
                attack(player, enemies[1])
                if player.equippedW != None and isinstance(player.equippedW,Items.M_weapons) and randint(0,2)==0: # retaliation
                    print("m weapons")
                    attack(enemies[1], player)
            elif len(enemies) >= 3 and enemy3.draw_button():
                # enemies[2].curHealth-=10
                enemy3.text_setter("{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth))
                enemytirn=True
                attack(player, enemies[2])
                if player.equippedW != None and isinstance(player.equippedW,Items.M_weapons) and randint(0,2)==0: # retaliation
                    print("m weapons")
                    attack(enemies[2], player)
            elif len(enemies) >= 4 and enemy4.draw_button():
                # enemies[3].curHealth-=10
                enemy4.text_setter("{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth))
                enemytirn=True
                attack(player, enemies[3])
                if player.equippedW != None and isinstance(player.equippedW,Items.M_weapons) and randint(0,2)==0: # retaliation
                    print("m weapons")
                    attack(enemies[3], player)
            elif len(enemies) >= 5 and enemy5.draw_button():
                # enemies[4].curHealth-=10
                enemy5.text_setter("{} - {}/{}".format(enemies[4].name,enemies[4].curHealth,enemies[4].maxHealth))
                enemytirn=True
                attack(player, enemies[4])
                if player.equippedW != None and isinstance(player.equippedW,Items.M_weapons) and randint(0,2)==0: # retaliation
                    print("m weapons")
                    attack(enemies[4], player)
            elif playerbutton.draw_button():
                pass
            elif inventorybutton.draw_button():
                Inventory.Inventory_manage(screen, player)
                playerbutton.text_setter("{} - {}/{}".format(player.name,player.curHealth,player.maxHealth))
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[5], (0,0))  
            elif spacialAttack.draw_button():
                
                
                if len(enemies) == 1:
                    specialAttack(player, enemies[0])
                    enemy1.text_setter("{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth))
                    
                elif len(enemies) == 2:
                    specialAttack(player, enemies[0])
                    enemy1.text_setter("{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth))
                    specialAttack(player, enemies[1])
                    enemy2.text_setter("{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth))
                    
                elif len(enemies) == 3:
                    specialAttack(player, enemies[0])
                    enemy1.text_setter("{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth))
                    specialAttack(player, enemies[1])
                    enemy2.text_setter("{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth))
                    specialAttack(player, enemies[2])
                    enemy3.text_setter("{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth))
                elif len(enemies) == 4:
                    specialAttack(player, enemies[0])
                    enemy1.text_setter("{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth))
                    specialAttack(player, enemies[1])
                    enemy2.text_setter("{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth))
                    specialAttack(player, enemies[2])
                    enemy3.text_setter("{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth))
                    specialAttack(player, enemies[3])
                    enemy4.text_setter("{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth))
                elif len(enemies) == 5:
                    specialAttack(player, enemies[0])
                    enemy1.text_setter("{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth))
                    specialAttack(player, enemies[1])
                    enemy2.text_setter("{} - {}/{}".format(enemies[1].name,enemies[1].curHealth,enemies[1].maxHealth))
                    specialAttack(player, enemies[2])
                    enemy3.text_setter("{} - {}/{}".format(enemies[2].name,enemies[2].curHealth,enemies[2].maxHealth))
                    specialAttack(player, enemies[3])
                    enemy4.text_setter("{} - {}/{}".format(enemies[3].name,enemies[3].curHealth,enemies[3].maxHealth))
                    specialAttack(player, enemies[4])
                    enemy5.text_setter("{} - {}/{}".format(enemies[4].name,enemies[4].curHealth,enemies[4].maxHealth))
                enemytirn=True
                
            elif runButton.draw_button():
                #nqkakvi procenti
                if player.stats["DEX"] + randint(0,10) >= 10:
                    return True
                else: enemytirn=True
            elif doNothingButton.draw_button():
                enemytirn=True
            
                
            
        # #enemy tirn
        # if enemies[0].curHealth<=0:
        #     print("yoooooooooo")
        #     enemy1 = Button.button(540, 260 ,100 ,100, "{} - {}/{}".format(enemies[0].name,enemies[0].curHealth,enemies[0].maxHealth),"red", screen, pg.image.load('deadenemy.png').convert_alpha())
        #     enemy1.draw_button()
            
        if enemytirn == True:
            screen.blit(player.optionSettings.BGs[5], (0,0))
            for i in enemies:
                if i.curHealth>0:
                    attack(i , player)
                    # player.curHealth-=10
                    playerbutton.text_setter("{} - {}/{}".format(player.name,player.curHealth,player.maxHealth))
                if player.curHealth<=0:
                    deathscreen(player, screen)
                    return 
        # screen.blit(myfont.render(str(player.curHealth)+"/"+str(player.maxHealth), 1, (255,255,255)), (40, 260))
        pg.display.update()
        
        
    
    pg.quit()
