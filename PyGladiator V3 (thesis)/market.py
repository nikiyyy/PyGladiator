import pygame as pg
import Button
import Items

def printBG(screen, player):
    if player.optionSettings.art == True:
            screen.blit(player.optionSettings.BGs[8], (0,0))
            
    myfont = pg.font.SysFont("Monotype Corsiva", 30)
    screen.blit(myfont.render("Player gold: "+str(player.money), 1, (0,0,0)), (100, 100))

def Trade_selectObj(buttonlist,buttonNumber):
    availible=[]
    availible.extend(Items.Mweapons)
    availible.extend(Items.Armour)
    availible.extend(Items.pations)
    availible.extend(Items.Shield)
    for i in availible:
        if i.__str__() == buttonlist[buttonNumber].text_getter()[2:]:
            print(i)
            return i 
    return ""


def Inventory_manage_selectObj(player,buttonlist,buttonNumber):
    for i in player.Inventory:
        if i.__str__() == buttonlist[buttonNumber].text_getter()[2:]:
            print(i)
            return i 
    return ""

def marketa(screen, player):
    buttonUp = Button.button(550, 40 ,250 ,40, "up","White", screen ,40)
    buttonDown = Button.button(550, 600 ,250 ,40, "down","White", screen ,40)
    screen.fill((0,0,0))
    printBG(screen, player)
    
    button1 = Button.button(350, 100 ,450 ,40, "1","Black", screen ,20)
    button2 = Button.button(350, 150 ,450 ,40, "2","Black", screen ,20)
    button3 = Button.button(350, 200 ,450 ,40, "3","Black", screen ,20)
    button4 = Button.button(350, 250 ,450 ,40, "4","Black", screen ,20)
    button5 = Button.button(350, 300 ,450 ,40, "5","Black", screen ,20)
    button6 = Button.button(350, 350 ,450 ,40, "6","Black", screen ,20)
    button7 = Button.button(350, 400 ,450 ,40, "7","Black", screen ,20)
    button8 = Button.button(350, 450 ,450 ,40, "8","Black", screen ,20)
    button9 = Button.button(350, 500 ,450 ,40, "9","Black", screen ,20)
    button10 = Button.button(350, 550 ,450 ,40, "10","Black", screen ,20)
    
    buttonTrade = Button.button(50, 600 ,100 ,70, "confirm","white", screen ,40)
    buttonBuy = Button.button(200, 600 ,100 ,70, "Buy","white", screen ,40)
    buttonSell = Button.button(50, 700 ,100 ,70, "Sell","white", screen ,40)
    buttonExit = Button.button(200, 700 ,100 ,70, "Exit","white", screen ,40)
    
    list10=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10]
    
    availible=[]
    availible.extend(Items.Mweapons)
    availible.extend(Items.Armour)
    availible.extend(Items.pations)
    availible.extend(Items.Shield)

    lowerLimit=0
    upperLimit=10
    select=""
    index=0
    flag="Buy"
    for i in availible[lowerLimit:upperLimit]:
        if index<=9:
            list10[index].text_setter(str(index)+i.__str__())
            index+=1
    while True:

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                printBG(screen, player)
                pg.quit()
            elif buttonExit.draw_button():
                return
            
            elif buttonBuy.draw_button():
                pg.display.update()
                printBG(screen, player)
                index=0
                flag="Buy"
                for i in availible[lowerLimit:upperLimit]:
                    if index<9:
                        list10[index].text_setter(str(index)+" "+i.__str__())
                        index+=1
                
            elif buttonSell.draw_button():
                
                printBG(screen, player)
                index=0
                flag="Sell"
                #nulirane
                for i in list10:
                    i.text_setter("")
                #populirane
                for i in player.Inventory[lowerLimit:upperLimit]:
                    if index<9:
                        list10[index].text_setter(str(index)+" "+i.__str__())
                        index+=1
                
                    
            elif buttonTrade.draw_button():
                if flag == "Sell":
                    player.money+=player.Inventory[player.Inventory.index(select)].value
                    del player.Inventory[player.Inventory.index(select)]
                    index=0
                    printBG(screen, player)
                    #nulirane
                    for i in list10:
                        i.text_setter("")
                    #populirane
                    for i in player.Inventory[lowerLimit:upperLimit]:
                        if index<9:
                            list10[index].text_setter(str(index)+" "+i.__str__())
                            index+=1
                            
                            
                elif flag == "Buy":
                    if player.money>=availible[availible.index(select)].value:
                        player.money-=availible[availible.index(select)].value
                        player.Inventory.append(availible[availible.index(select)])
                    else:
                        print("insiuffcint funds")
            elif buttonUp.draw_button():
                printBG(screen, player)
                if lowerLimit>0:
                    lowerLimit-=1
                    upperLimit-=1
                if flag == "Buy":    
                    index=0   
                    for i in availible[lowerLimit:upperLimit]:
                        if index<9:
                            list10[index].text_setter(str(index)+i.__str__())
                            index+=1
                        pg.display.update()
                        printBG(screen, player)
                else:
                    index=0   
                    for i in player.Inventory[lowerLimit:upperLimit]:
                        if index<9:
                            list10[index].text_setter(str(index)+i.__str__())
                            index+=1
                        pg.display.update()
                        printBG(screen, player)
                
                
            elif buttonDown.draw_button():
                printBG(screen, player)
                if flag == "Sell":
                    if upperLimit<len(player.Inventory):
                        lowerLimit+=1
                        upperLimit+=1
                        index=0      
                        for i in player.Inventory[lowerLimit:upperLimit]:
                            if index<9:
                                list10[index].text_setter(str(index)+i.__str__())
                                index+=1
                        pg.display.update()
                        printBG(screen, player)
                else:
                    if upperLimit<len(availible):
                        lowerLimit+=1
                        upperLimit+=1
                        index=0      
                        for i in availible[lowerLimit:upperLimit]:
                            if index<9:
                                list10[index].text_setter(str(index)+i.__str__())
                                index+=1
                        pg.display.update()
                        printBG(screen, player)

                        
            if button1.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,0)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,0)
                    
            if button2.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,1)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,1)
                    
            if button3.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,2)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,2)
                
            if button4.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,3)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,3)
                
            if button5.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,4)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,4)
                
            if button6.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,5)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,5)
                
            if button7.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,6)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,6)
                
            if button8.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,7)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,7)
                
            if button9.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,8)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,8)
                
            if button10.draw_button():
                if flag == "Sell":
                    select = Inventory_manage_selectObj(player,list10,9)
                elif flag == "Buy":             
                    select = Trade_selectObj(list10,9)
        pg.display.update()