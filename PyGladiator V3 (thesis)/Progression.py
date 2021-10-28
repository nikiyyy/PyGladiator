import pygame as pg
import Button


def progress(screen, player):
    if player.optionSettings.art == True:
            screen.blit(player.optionSettings.BGs[3], (0,0))
    backtomemu = Button.button(550, 600 ,100 ,50, "exit","black",screen,40)
        
    Strenght = Button.button(150, 150 ,70 ,30, str(player.stats["STR"]),"black",screen, 40)
    Endurance = Button.button(150, 200 ,70 ,30, str(player.stats["END"]),"black",screen, 40)
    Diplomacy = Button.button(150, 250 ,70 ,30, str(player.stats["DIP"]),"black",screen, 40)
    Dexterity =  Button.button(150, 300 ,70 ,30, str(player.stats["DEX"]),"black",screen, 40)
    
    StrenghtP = Button.button(80, 155 ,50 ,50, "STR +","red",screen,27)
    EnduranceP = Button.button(80, 205 ,50 ,50, "END +","red",screen,27)
    DiplomacyP = Button.button(80, 255 ,50 ,50, "DIP +","red",screen,27)
    DexterityP = Button.button(80, 305 ,50 ,50, "DEX +","red",screen,27)

    
    while True:
        screen.blit(player.optionSettings.myfont.render("Ability points: "+str(player.ability_points), 1, (255,255,255)), (80, 100))
        
        #xp self.XP,self.XPcaps[self.XPlevel-1],self.XPlevel Player.skills[i]
        screen.blit(player.optionSettings.myfont.render("Stage level: "+str(player.levelStage), 1, (0,0,0)), (230, 100))
        screen.blit(player.optionSettings.myfont.render("Player XP: "+str(player.XP)+" / "+str(player.XPcaps[player.XPlevel-1]), 1, (255,255,255)), (350, 100))
        screen.blit(player.optionSettings.myfont.render("Player level: "+str(player.XPlevel), 1, (0,0,0)), (530, 100))
        screen.blit(player.optionSettings.myfont.render("One handed - "+str(player.skills["One handed"]), 1, (0,0,0)), (550, 150))
        screen.blit(player.optionSettings.myfont.render("Two handed - "+str(player.skills["Two handed"]), 1, (0,0,0)), (550, 190))
        screen.blit(player.optionSettings.myfont.render("Throwing - "+str(player.skills["Throwing"]), 1, (0,0,0)), (550, 230))
        screen.blit(player.optionSettings.myfont.render("Shooting - "+str(player.skills["Shooting"]), 1, (0,0,0)), (550, 270))
        screen.blit(player.optionSettings.myfont.render("Blocking - "+str(player.skills["Blocking"]), 1, (0,0,0)), (550, 310))
        screen.blit(player.optionSettings.myfont.render("Heavy armour - "+str(player.skills["Heavy armour"]), 1, (0,0,0)), (550, 350))
        screen.blit(player.optionSettings.myfont.render("Medium armour - "+str(player.skills["Medium armour"]), 1, (0,0,0)), (550, 390))
        screen.blit(player.optionSettings.myfont.render("Light armour - "+str(player.skills["Light armour"]), 1, (0,0,0)), (550, 430))
        
        for event in pg.event.get():
        
            Strenght.text_setter(str(player.stats["STR"]))
            Endurance.text_setter(str(player.stats["END"]))
            Diplomacy.text_setter(str(player.stats["DIP"]))
            Dexterity.text_setter(str(player.stats["DEX"]))
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p: #and test == True:
                    return
            if event.type == pg.QUIT:
                pg.quit()
            elif backtomemu.draw_button():
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
                return
            elif StrenghtP.draw_button():
                if player.ability_points > 0:
                    player.stats["STR"]+=1
                    player.ability_points-=1
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
            elif EnduranceP.draw_button():
                if player.ability_points > 0:
                    player.stats["END"]+=1
                    player.ability_points-=1
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
            elif DiplomacyP.draw_button():
                if player.ability_points > 0:
                    player.stats["DIP"]+=1
                    player.ability_points-=1
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
            elif DexterityP.draw_button():
                if player.ability_points > 0:
                    player.stats["DEX"]+=1
                    player.ability_points-=1
                if player.optionSettings.art == True:
                    screen.blit(player.optionSettings.BGs[3], (0,0))
            elif Strenght.draw_button():
                pass
            elif Endurance.draw_button():
                pass
            elif Diplomacy.draw_button():
                pass
            elif Dexterity.draw_button():
                pass
        pg.display.update()