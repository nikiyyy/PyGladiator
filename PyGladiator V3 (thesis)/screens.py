import pygame as pg
import Button
# import Options
import CRUD
# import Player as PL
import MapNavigation 
import market
import screens
import Inventory
import Progression

# background = pg.image.load("market.png")

def winCondition(player, screen):
    screen.fill((0,0,0))
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[9], (0,0))   
    newgameButton = Button.button(120, 600 ,150 ,40,"New game", "white", screen ,40)
    loadButton = Button.button(320, 600 ,150 ,40,"Load game", "white", screen ,40)
    exitButton = Button.button(520, 600 ,150 ,40, "Exit","white",screen ,40)
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[9], (0,0))
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif newgameButton.draw_button():
                #reset player
                charcreation(screen, player)
            elif loadButton.draw_button():
                CRUD.CRUD(screen, player, 1)
            elif exitButton.draw_button():
                return
        pg.display.update()

def deathscreen(player, screen):
    screen.fill((0,0,0))
    newgameButton = Button.button(300, 100 ,150 ,40,"New game","white",screen ,40)
    loadButton = Button.button(300, 200 ,150 ,40,"Load game","white",screen ,40)
    exitButton = Button.button(300, 300 ,50 ,50, "Exit","white",screen ,40)
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[7], (0,0))
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif newgameButton.draw_button():
                charcreation(screen, player)
            elif loadButton.draw_button():
                CRUD.CRUD(screen, player, 1)
            elif exitButton.draw_button():
                return
        pg.display.update()
        
def creditscreen(screen, OptionsObj):
    screen.fill((0,0,0))
    if OptionsObj.art == True:
        screen.blit(OptionsObj.BGs[10], (0,0))
    exitButton = Button.button(350, 650 ,150 ,50, "Exit","black",screen ,40)
    
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif exitButton.draw_button():
                return
                
        pg.display.update()


def manage_settings(screen, OptionsObj):
    screen.fill((0,0,0))
    if OptionsObj.art == True:
        screen.blit(OptionsObj.BGs[3], (0,0))
    graphicsButton = Button.button(300, 100 ,150 ,40,"Art - "+str(OptionsObj.art), "black",screen ,40)
    DifficultyButton = Button.button(300, 200 ,150 ,40,"Difficulty "+OptionsObj.difficulty,"black",screen ,40)
    exitButton = Button.button(300, 400 ,150 ,40,"Exit", "black",screen ,40)
    CreditsButton = Button.button(300, 300 ,150 ,40,"Credits", "black",screen ,40)

    
    run = True
    while run:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif graphicsButton.draw_button():
                if OptionsObj.art == True:
                    screen.blit(OptionsObj.BGs[3], (0,0))  
                    
                if OptionsObj.art == True:
                    OptionsObj.art = False
                    graphicsButton.text_setter("Art -"+str(OptionsObj.art))
                else: 
                    OptionsObj.art = True
                    graphicsButton.text_setter("Art -"+str(OptionsObj.art))
                    
                if OptionsObj.art == True:
                    screen.blit(OptionsObj.BGs[3], (0,0))  
                    
            elif DifficultyButton.draw_button():
                    if OptionsObj.difficulty == "Easy":
                        OptionsObj.difficulty = "Medium"
                        DifficultyButton.text_setter("Difficulty Medium")
                        
                    elif OptionsObj.difficulty == "Medium":
                        OptionsObj.difficulty = "Hard"
                        DifficultyButton.text_setter("Difficulty Hard")
                        
                    elif OptionsObj.difficulty == "Hard":
                        OptionsObj.difficulty = "Easy"
                        DifficultyButton.text_setter("Difficulty Easy")
                        
                    if OptionsObj.art == True:
                        screen.blit(OptionsObj.BGs[3], (0,0))   
            elif CreditsButton.draw_button():
                screens.creditscreen(screen, OptionsObj)
                if OptionsObj.art == True:
                    screen.blit(OptionsObj.BGs[3], (0,0))
                    
            elif exitButton.draw_button():
                OptionsObj.createfile()
                return
        pg.display.update()
        
def charcreation(screen, player):
    
    screen.fill((0,0,0))
    prologuenum=0
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[prologuenum], (0,0))
    nextButton = Button.button(550, 700 ,150 ,40,"Next","black",screen ,40)
    prevButton = Button.button(150, 700 ,150 ,40,"Previous","black",screen ,40)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif nextButton.draw_button():
                prologuenum+=1
                if player.optionSettings.art == True and prologuenum!=3:
                    screen.blit(player.optionSettings.BGs[prologuenum], (0,0))
        
                if prologuenum==3: 
                    while True:
                        MapNavigation.main(screen, player)
                    
            elif prevButton.draw_button():
                if prologuenum<=0:
                    continue
                prologuenum-=1
        pg.display.update()
        
def menuNavMap(screen, player):
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[3], (0,0))
    optionsButton = Button.button(300, 200 ,150 ,40,"Options", "black",screen ,40)
    loadButton = Button.button(300, 300 ,150 ,40,"Load", "black",screen ,40)
    runButton = Button.button(300, 400 ,150 ,40,"Return", "black",screen ,40)
    
    run = True
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif optionsButton.draw_button():
                manage_settings(screen, player.optionSettings)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
                
            elif loadButton.draw_button():
                CRUD.CRUD(screen, player,2)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
                    
            elif runButton.draw_button():
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m: #and test == True:
                    return
                
                
        pg.display.update()

def cityMenu(screen, player):
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[6], (0,0))
    marketButton = Button.button(600, 300 ,150 ,40,"Market", "black",screen ,40)
    inventoryButton = Button.button(600, 400 ,150 ,40,"Inventory", "black",screen ,40)
    progressionButton = Button.button(600, 500 ,150 ,40,"Progression", "black",screen ,40)
    exitButton = Button.button(600, 700 ,150 ,40,"Exit city", "black",screen ,40)
    
    run = True
    while run:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False 
            elif marketButton.draw_button():
                market.marketa(screen, player)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[6], (0,0))
            elif inventoryButton.draw_button():
                Inventory.Inventory_manage(screen, player)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[6], (0,0))
            elif progressionButton.draw_button():
                Progression.progress(screen, player)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[6], (0,0))
            elif exitButton.draw_button():
                return
        pg.display.update()
        