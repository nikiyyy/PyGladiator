import pygame as pg
import Button
import Options
import CRUD
import Player as PL
import MapNavigation 
import screens

pg.init()
clock = pg.time.Clock()
fps = 60
# background = pg.image.load("market.png")

#game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
gameSettings = Options.Gameoptions()
# screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Battle')

# start_img = pg.image.load('start_btn.png').convert_alpha()

gameSettings = Options.Gameoptions()
gameSettings.loadfile()
WIN = pg.display.set_mode((gameSettings.WIDTH, gameSettings.WIDTH))
pplayer=PL.Player("human",3,200 ,gameSettings)
pplayer.X_cord=6
        
 
def mainmenu(screen, player):
     
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[4], (0,0))
    newGameButton = Button.button(600, 200 ,150 ,40,"New game",  "Black", screen,40) 
    LoadButton = Button.button(600, 300 ,150 ,40,"Load", "Black", screen,40)
    OptionsButton = Button.button(600, 400 ,150 ,40,"Options",  "Black", screen,40)
    exitButton = Button.button(600, 600 ,150 ,40,"Exit", "Black", screen,40)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif newGameButton.draw_button():
                screens.charcreation(screen, player)
                # MapNavigation.main(screen, player)
                if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[4], (0,0))
            elif LoadButton.draw_button():
                
                while CRUD.CRUD(screen, player, 1):  
                    MapNavigation.main(screen, player)
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[4], (0,0))
                        
            elif OptionsButton.draw_button():
                screens.manage_settings(screen, player.optionSettings)
                if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[4], (0,0))
                
            # elif CreditsButton.draw_button():
            #     screens.creditscreen(screen)
            #     screen.fill((0,0,0))
            #     if player.optionSettings.art == True:
            #             screen.blit(player.optionSettings.BGs[4], (0,0))
                
            elif exitButton.draw_button():
                run = False 
        pg.display.update()
        
        
        

mainmenu(WIN, pplayer)