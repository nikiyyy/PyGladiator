import pygame as pg
import Button
import Items

def Inventory_manage_selectObj(player,buttonlist,buttonNumber):
    for i in player.Inventory:
        if i.__str__() == buttonlist[buttonNumber].text_getter()[2:]:
            print(i)
            return i 
    return ""

def Inventory_manage(screen, player):
    if player.optionSettings.art == True:
            screen.blit(player.optionSettings.BGs[3], (0,0))



    
    lowerLimit=0
    upperLimit=10
    select=""
    while True:
        buttonUp = Button.button(550, 40 ,250 ,40, "up","black", screen ,40)
        buttonDown = Button.button(550, 600 ,250 ,40, "down","black",screen , 40) 
        
        button1 = Button.button(350, 100 ,450 ,40, "1","black",screen , 15) 
        button2 = Button.button(350, 150 ,450 ,40, "2","black",screen , 15) 
        button3 = Button.button(350, 200 ,450 ,40, "3","black",screen , 15) 
        button4 = Button.button(350, 250 ,450 ,40, "4","black",screen , 15) 
        button5 = Button.button(350, 300 ,450 ,40, "5","black",screen , 15) 
        button6 = Button.button(350, 350 ,450 ,40, "6","black",screen , 15)
        button7 = Button.button(350, 400 ,450 ,40, "7","black",screen , 15)
        button8 = Button.button(350, 450 ,450 ,40, "8","black",screen , 15)
        button9 = Button.button(350, 500 ,450 ,40, "9","black",screen , 15)
        button10 = Button.button(350, 550 ,450 ,40, "10","black",screen , 15)
        
        buttonUse = Button.button(150, 600 ,100 ,70, "Use","black",screen , 40)
        buttonDelete = Button.button(300, 600 ,100 ,70, "Delete","black",screen , 40)
        buttonExit = Button.button(450, 600 ,100 ,70, "Exit","black",screen , 40)
        
        buttonEquippedA = Button.button(200, 70 ,100 ,70, player.equippedA.__str__() ,"black",screen ,  40)
        buttonEquippedRH = Button.button(200, 160 ,100 ,70, player.equippedA.__str__() ,"black",screen ,  40)
        buttonEquippedLH = Button.button(200, 240 ,100 ,70, player.equippedA.__str__() ,"black",screen ,  40)
        
        if player.equippedA != None:
            buttonEquippedA = Button.button(200, 70 ,100 ,70, player.equippedA.returnName() ,"black",screen ,  40)
        else: buttonEquippedA = Button.button(200, 70 ,100 ,70, player.equippedA.__str__() ,"black",screen ,  40)
        
        if player.equippedW != None:
            buttonEquippedRH = Button.button(200, 160 ,100 ,70, player.equippedW.returnName(),"black",screen ,  40)
        else: buttonEquippedRH = Button.button(200, 160 ,100 ,70, player.equippedW.__str__() ,"black",screen ,  40)
        
        if player.equippedOH != None:
            buttonEquippedLH = Button.button(200, 250 ,100 ,70, player.equippedOH.returnName(),"black",screen ,  40)
        else: buttonEquippedLH = Button.button(200, 250 ,100 ,70, player.equippedOH.__str__() ,"black",screen ,  40)
        
        list10=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10]
        index=0
        for i in player.Inventory:
            if index<9:
                list10[index].text_setter(str(index)+" "+i.__str__())
                index+=1
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_i: #and test == True:
                    return
            if event.type == pg.QUIT:
                pg.quit()
            elif buttonUp.draw_button():
                # screen.fill((0,0,0))
                if lowerLimit>0:
                    lowerLimit-=1
                    upperLimit-=1
                    index=0   
                    for i in player.Inventory[lowerLimit:upperLimit]:
                        if index<9:
                            list10[index].text_setter(str(index)+" Gold: "+i.value-player.stats["DIP"]+"| "+i.__str__())
                            index+=1
                        pg.display.update()
                        # screen.fill((0,0,0))
                        
            elif buttonDown.draw_button():
                # screen.fill((0,0,0))
                if upperLimit<len(player.Inventory):
                    lowerLimit+=1
                    upperLimit+=1
                    index=0      
                    for i in player.Inventory[lowerLimit:upperLimit]:
                        if index<9:
                            list10[index].text_setter(str(index)+" Gold: "+i.value-player.stats["DIP"]+"| "+i.__str__())
                            index+=1
                    pg.display.update()
                    # screen.fill((0,0,0))
                
            if button1.draw_button():
                select = Inventory_manage_selectObj(player, list10,0)

            if button2.draw_button():
                select = Inventory_manage_selectObj(player,list10,1)
                        
            if button3.draw_button():
                select = Inventory_manage_selectObj(player, list10,2)
                
            if button4.draw_button():
                select = Inventory_manage_selectObj(player, list10,3)
                
            if button5.draw_button():
                select = Inventory_manage_selectObj(player, list10,4)
                
            if button6.draw_button():
                select = Inventory_manage_selectObj(player, list10,5)
                
            if button7.draw_button():
                select = Inventory_manage_selectObj(player, list10,6)
                
            if button8.draw_button():
                select = Inventory_manage_selectObj(player, list10,7)
                
            if button9.draw_button():
                select = Inventory_manage_selectObj(player, list10,8)
                
            if button10.draw_button():
                select = Inventory_manage_selectObj(player, list10,9)
                
            if buttonEquippedA.draw_button():
                if player.equippedA != None:
                    player.Inventory.append(player.equippedA)
                    player.equippedA=None
                    buttonEquippedA.text_setter("None")
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                        
            if buttonEquippedRH.draw_button():
                if player.equippedW != None:
                    player.Inventory.append(player.equippedW)
                    player.equippedW=None
                    buttonEquippedRH.text_setter("None")
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                        
            if buttonEquippedLH.draw_button():
                if player.equippedOH != None:
                    player.Inventory.append(player.equippedOH)
                    player.equippedOH=None
                    buttonEquippedLH.text_setter("None")
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                
            if buttonExit.draw_button():
                # screen.fill((0,0,0))
                return
            if buttonUse.draw_button():
                print(select, type(select))
                if isinstance(select,Items.C_armour):
                    if player.equippedA!=None:
                        player.Inventory.append(player.equippedA)
                        player.equippedA=select
                        del player.Inventory[player.Inventory.index(select)]
                    else:
                        player.equippedA=select
                        del player.Inventory[player.Inventory.index(select)]
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                    index=0
                    for i in player.Inventory:
                        if index<9:
                            list10[index].text_setter(str(index)+" "+i.__str__())
                            index+=1
                elif isinstance(select,Items.M_weapons) or isinstance(select,Items.R_weapons):
                    if select.hands == 1:
                        if Button.Popup("inv",screen) == "Y":
                            if player.equippedW!=None:
                                player.Inventory.append(player.equippedW)
                                player.equippedW=select
                                del player.Inventory[player.Inventory.index(select)]
                            else:
                                player.equippedW=select
                                del player.Inventory[player.Inventory.index(select)]
                        else:
                            if player.equippedOH!=None:
                                player.Inventory.append(player.equippedOH)
                                player.equippedOH=select
                                del player.Inventory[player.Inventory.index(select)]
                            else:
                                player.equippedOH=select
                                del player.Inventory[player.Inventory.index(select)]
                    
                    else:
                        if player.equippedOH!=None:
                            player.Inventory.append(player.equippedOH)
                            player.equippedOH=None
                            
                        if player.equippedW!=None:
                            player.Inventory.append(player.equippedW)
                            player.equippedW=select
                            del player.Inventory[player.Inventory.index(select)]
                        else:
                            player.equippedW=select
                            del player.Inventory[player.Inventory.index(select)]
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                        
                    index=0
                    for i in player.Inventory:
                        if index<9:
                            list10[index].text_setter(str(index)+" "+i.__str__())
                            index+=1
                            
                elif isinstance(select,Items.C_shield):
                    if player.equippedW.hands == 2:
                        player.Inventory.append(player.equippedW)
                        player.equippedW=None
                        
                    if player.equippedOH!=None:
                        player.Inventory.append(player.equippedOH)
                        player.equippedOH=select
                        del player.Inventory[player.Inventory.index(select)]
                    else:
                        player.equippedOH=select
                        del player.Inventory[player.Inventory.index(select)]
                    if player.optionSettings.art == True:
                        screen.blit(player.optionSettings.BGs[3], (0,0))
                    index=0
                    for i in player.Inventory:
                        if index<9:
                            list10[index].text_setter(str(index)+" "+i.__str__())
                            index+=1
                elif isinstance(select,Items.C_consumable):
                    select.use(player)
                    del player.Inventory[player.Inventory.index(select)]
                    
                index=0   
                for i in player.Inventory[lowerLimit:upperLimit]:
                    if index<9:
                        list10[index].text_setter(str(index)+" "+i.__str__())
                        index+=1
                    pg.display.update()
            
            if buttonDelete.draw_button():
                if select!="":
                    if Button.Popup("inv",screen) == "Y": # ArithmeticErrorscreen
                        del player.Inventory[player.Inventory.index(select)]
                # screen.fill((0,0,0))
        if player.equippedA != None:
            buttonEquippedA.text_setter(player.equippedA.returnName())
        else: player.equippedA.__str__()
        
        if player.equippedW != None:
            buttonEquippedRH.text_setter(player.equippedW.returnName())
        else: player.equippedW.__str__()
        
        if player.equippedOH != None:
            buttonEquippedRH.text_setter(player.equippedOH.returnName())
        else: player.equippedOH.__str__()
            
        index=0
        for i in player.Inventory:
            if index<9:
                list10[index].text_setter(str(index)+" "+i.__str__())
                index+=1
                
        pg.display.update()