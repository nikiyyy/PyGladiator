import pygame as pg
import Button
import Database as DB
import Items
import Button
from datetime import datetime


def CRUD_sendToDB(player,savename): #mahni specialisation iloji gameoptions, battlemap, stagelvl
    if player.equippedOH==None and player.equippedW==None and player.equippedA==None:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel,None, None, None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH!=None and player.equippedW==None and player.equippedA==None:
        DB.add_row(savename,player.race,player.name,player.levelStage.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH==None and player.equippedW!=None and player.equippedA==None:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH==None and player.equippedW==None and player.equippedA!=None:
        DB.add_row(savename,player.race,player.name,player.  levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH!=None and player.equippedW!=None and player.equippedA==None:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH!=None and player.equippedW==None and player.equippedA!=None:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    elif player.equippedOH==None and player.equippedW!=None and player.equippedA!=None:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))
    
    else:
        DB.add_row(savename,player.race,player.name,player.levelStage,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),player.compressWorldmap(),datetime.now().strftime("%d.%m.%Y/%R"))#stats, skill, abp, money, XP, inv

saves=["1 save","2 save","3 save","4 save","5 save","6 save","7 save","8 save","9 save"]
loads=["1 load","2 load","3 load","4 load","5 load","6 load","7 load","8 load","9 load"]
dels=["1 delete","2 delete","3 delete","4 delete","5 delete","6 delete","7 delete","8 delete","9 delete"] 

def printBG(player,screen):
    if player.optionSettings.art == True:
        screen.blit(player.optionSettings.BGs[3], (0,0))


def CRUD(screen, player, access):
    #shows how saved games
    index=1
    for i in DB.view():
        print(int(i[0]))
        
    printBG(player,screen)
    

    crud_choise="load"
    background = Button.button(0, 0 ,800 ,700, "UP","black",screen ,40)
    
    for i in DB.view():
        # print(type(i[0])
        saves[int(i[0])-1]=i[0]
        loads[int(i[0])-1]=i[0]
        dels[int(i[0])-1]=i[0]
    #ima po-umni nachini da se napravi tova
    # print(len(DB.view()))
        
    save1 = Button.button(70, 85 ,180 ,140,  saves[0],"black",screen ,40)
    save2 = Button.button(295, 85 ,180 ,140, saves[1],"black",screen ,40)
    save3 = Button.button(520, 85 ,180 ,140, saves[2],"black",screen ,40)
    save4 = Button.button(70, 265 ,180 ,140, saves[3],"black",screen ,40)
    save5 = Button.button(295, 265 ,180 ,140, saves[4],"black",screen ,40)
    save6 = Button.button(520, 265 ,180 ,140, saves[5],"black",screen ,40)
    save7 = Button.button(70, 445 ,180 ,140, saves[6],"black",screen ,40)
    save8 = Button.button(295, 445 ,180 ,140, saves[7],"black",screen ,40)
    save9 = Button.button(520, 445 ,180 ,140, saves[8],"black",screen ,40)
    
    savesOBJ=[save1,save2,save3,save4,save5,save6,save7,save8,save9]
    
    load1 = Button.button(70, 85 ,180 ,140, loads[0],"black",screen ,40)
    load2 = Button.button(295, 85 ,180 ,140, loads[1],"black",screen ,40)
    load3 = Button.button(520, 85 ,180 ,140, loads[2],"black",screen ,40)
    load4 = Button.button(70, 265 ,180 ,140, loads[3],"black",screen ,40)
    load5 = Button.button(295, 265 ,180 ,140, loads[4],"black",screen ,40)
    load6 = Button.button(520, 265 ,180 ,140, loads[5],"black",screen ,40)
    load7 = Button.button(70, 445 ,180 ,140, loads[6],"black",screen ,40)
    load8 = Button.button(295, 445 ,180 ,140, loads[7],"black",screen ,40)
    load9 = Button.button(520, 445 ,180 ,140, loads[8],"black",screen ,40)
    
    loadOBJ = [load1,load2,load3,load4,load5,load6,load7,load8,load9]
    
    delete1 = Button.button(70, 85 ,180 ,140, dels[0],"black",screen ,40)
    delete2 = Button.button(295, 85 ,180 ,140, dels[1],"black",screen ,40)
    delete3 = Button.button(520, 85 ,180 ,140, dels[2],"black",screen ,40)
    delete4 = Button.button(70, 265 ,180 ,140, dels[3],"black",screen ,40)
    delete5 = Button.button(295, 265 ,180 ,140, dels[4],"black",screen ,40)
    delete6 = Button.button(520, 265 ,180 ,140, dels[5],"black",screen ,40)
    delete7 = Button.button(70, 445 ,180 ,140, dels[6],"black",screen ,40)
    delete8 = Button.button(295, 445 ,180 ,140, dels[7],"black",screen ,40)
    delete9 = Button.button(520, 445 ,180 ,140, dels[8],"black",screen ,40)
    
    deleteOBJ = [delete1,delete2,delete3,delete4,delete5,delete6,delete7,delete8,delete9]
    
    save = Button.button(100, 600 ,100 ,70, "save","black",screen ,40)
    load = Button.button(250, 600 ,100 ,70, "load","black",screen ,40)
    delete = Button.button(400, 600 ,100 ,70, "delete","black",screen ,40)
    backtomemu = Button.button(550, 600 ,100 ,70, "exit","black",screen ,40)
    background.draw_button()
    
    

    while True:
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                pg.quit()
            elif access==2 and save.draw_button():
                printBG(player,screen)
                crud_choise="save"

            elif load.draw_button():
                printBG(player,screen)
                crud_choise="load"

            elif delete.draw_button():
                printBG(player,screen)
                crud_choise="delete"

            elif backtomemu.draw_button():
                screen.fill((0,0,0))
                
                return False

            if crud_choise=="save":
                if  save1.draw_button():
                    if DB.load("1") != None and len(DB.load("1")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[0].text_setter("1")
                            loadOBJ[0].text_setter("1")
                            deleteOBJ[0].text_setter("1")
                            DB.delete("1")
                            CRUD_sendToDB(player,"1")
                            saves[0]="1"
                            loads[0]="1"
                            dels[0]="1"
                        
                    else:
                        savesOBJ[0].text_setter("1")
                        loadOBJ[0].text_setter("1")
                        deleteOBJ[0].text_setter("1")
                        DB.delete("1")
                        CRUD_sendToDB(player,"1")
                        saves[0]="1"
                        loads[0]="1"
                        dels[0]="1"
                    printBG(player,screen)

                elif save2.draw_button():
                    if len(DB.load("2")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[1].text_setter("2")
                            loadOBJ[1].text_setter("2")
                            deleteOBJ[1].text_setter("2")
                            DB.delete("2")
                            CRUD_sendToDB(player,"2")
                            saves[1]="2"
                            loads[1]="2"
                            dels[1]="2"
                    else:
                        savesOBJ[1].text_setter("2")
                        loadOBJ[1].text_setter("2")
                        deleteOBJ[1].text_setter("2")
                        DB.delete("2")
                        CRUD_sendToDB(player,"2")
                        saves[1]="2"
                        loads[1]="2"
                        dels[1]="2"                        
                    printBG(player,screen)
                    
                elif save3.draw_button():
                    if len(DB.load("3")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[2].text_setter("3")
                            loadOBJ[2].text_setter("3")
                            deleteOBJ[2].text_setter("3")
                            DB.delete("3")
                            CRUD_sendToDB(player,"3")
                            saves[2]="3"
                            loads[2]="3"
                            dels[2]="3"
                        
                    else:
                        savesOBJ[2].text_setter("3")
                        loadOBJ[2].text_setter("3")
                        deleteOBJ[2].text_setter("3")
                        DB.delete("3")
                        CRUD_sendToDB(player,"3")
                        saves[2]="3"
                        loads[2]="3"
                        dels[2]="3"
                    printBG(player,screen)
                    
                elif save4.draw_button():
                    if len(DB.load("4")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[3].text_setter("4")
                            loadOBJ[3].text_setter("4")
                            deleteOBJ[3].text_setter("4")
                            DB.delete("4")
                            CRUD_sendToDB(player,"4")
                            saves[3]="4"
                            loads[3]="4"
                            dels[3]="4"
                        
                    else:
                        savesOBJ[3].text_setter("4")
                        loadOBJ[3].text_setter("4")
                        deleteOBJ[3].text_setter("4")
                        DB.delete("4")
                        CRUD_sendToDB(player,"4")
                        saves[3]="4"
                        loads[3]="4"
                        dels[3]="4"
                    printBG(player,screen)
                    
                elif save5.draw_button():
                    if len(DB.load("5")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[4].text_setter("5")
                            loadOBJ[4].text_setter("5")
                            deleteOBJ[4].text_setter("5")
                            DB.delete("5")
                            CRUD_sendToDB(player,"5")
                            saves[4]="5"
                            loads[4]="5"
                            dels[4]="5"
                        
                    else:
                        savesOBJ[4].text_setter("5")
                        loadOBJ[4].text_setter("5")
                        deleteOBJ[4].text_setter("5")
                        DB.delete("5")
                        CRUD_sendToDB(player,"5")
                        saves[4]="5"
                        loads[4]="5"
                        dels[4]="5"
                    printBG(player,screen)
                    
                elif save6.draw_button():
                    if len(DB.load("6")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[5].text_setter("6")
                            loadOBJ[5].text_setter("6")
                            deleteOBJ[5].text_setter("6")
                            DB.delete("6")
                            CRUD_sendToDB(player,"6")
                            saves[5]="6"
                            loads[5]="6"
                            dels[5]="6"
                        
                    else:
                        savesOBJ[5].text_setter("6")
                        loadOBJ[5].text_setter("6")
                        deleteOBJ[5].text_setter("6")
                        DB.delete("6")
                        CRUD_sendToDB(player,"6")
                        saves[5]="6"
                        loads[5]="6"
                        dels[5]="6"
                    printBG(player,screen)
                    
                elif save7.draw_button():
                    if len(DB.load("7")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[6].text_setter("7")
                            loadOBJ[6].text_setter("7")
                            deleteOBJ[6].text_setter("7")
                            DB.delete("7")
                            CRUD_sendToDB(player,"7")
                            saves[6]="7"
                            loads[6]="7"
                            dels[6]="7"
                        
                    else:
                        savesOBJ[6].text_setter("7")
                        loadOBJ[6].text_setter("7")
                        deleteOBJ[6].text_setter("7")
                        DB.delete("7")
                        CRUD_sendToDB(player,"7")
                        saves[6]="7"
                        loads[6]="7"
                        dels[6]="7"
                    printBG(player,screen)
                    
                elif save8.draw_button():
                    if len(DB.load("8")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[7].text_setter("8")
                            loadOBJ[7].text_setter("8")
                            deleteOBJ[7].text_setter("8")
                            DB.delete("8")
                            CRUD_sendToDB(player,"8")
                            saves[7]="8"
                            loads[7]="8"
                            dels[7]="8"
                        
                    else:
                        savesOBJ[7].text_setter("8")
                        loadOBJ[7].text_setter("8")
                        deleteOBJ[7].text_setter("8")
                        DB.delete("8")
                        CRUD_sendToDB(player,"8")
                        saves[7]="8"
                        loads[7]="8"
                        dels[7]="8"
                    printBG(player,screen)
                    
                elif save9.draw_button():
                    if len(DB.load("8")) > 0:
                        if Button.Popup("save", screen) == "Y":
                            savesOBJ[8].text_setter("9")
                            loadOBJ[8].text_setter("9")
                            deleteOBJ[8].text_setter("9")
                            DB.delete("9")
                            CRUD_sendToDB(player,"9")
                            saves[8]="9"
                            loads[8]="9"
                            dels[8]="9"
                        
                    else:
                        savesOBJ[8].text_setter("9")
                        loadOBJ[8].text_setter("9")
                        deleteOBJ[8].text_setter("9")
                        DB.delete("9")
                        CRUD_sendToDB(player,"9")
                        saves[8]="9"
                        loads[8]="9"
                        dels[8]="9"
                    printBG(player,screen)
                    printBG(player,screen)
                

            elif crud_choise=="load":
                if  load1.draw_button():
                    try:
                        player.loadFromFile(DB.load("1"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                    
                elif load2.draw_button():
                    try:
                        player.loadFromFile(DB.load("2"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                    
                elif load3.draw_button():
                    try:
                        player.loadFromFile(DB.load("3"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load4.draw_button():
                    try:
                        player.loadFromFile(DB.load("4"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load5.draw_button():
                    try:
                        player.loadFromFile(DB.load("5"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load6.draw_button():
                    try:
                        player.loadFromFile(DB.load("6"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load7.draw_button():
                    try:
                        player.loadFromFile(DB.load("7"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load8.draw_button():
                    try:
                        player.loadFromFile(DB.load("8"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
                elif load9.draw_button():
                    try:
                        player.loadFromFile(DB.load("9"))
                    except:
                        print("no such file")
                    screen.fill((0,0,0))
                    return True
                
            elif crud_choise=="delete":
            
                if  delete1.draw_button():
                    
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("1")
                        saves[0]="1 save"
                        loads[0]="1 load"
                        dels[0]="1 delete"
                        
                        savesOBJ[0].text_setter("1 save")
                        loadOBJ[0].text_setter("1 load")
                        deleteOBJ[0].text_setter("1 delete")
                        
                        printBG(player,screen)
                elif delete2.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("2")
                        saves[1]="2 save"
                        loads[1]="2 load"
                        dels[1]="2 delete"
                        
                        savesOBJ[1].text_setter("2 save")
                        loadOBJ[1].text_setter("2 load")
                        deleteOBJ[1].text_setter("2 delete")
                        
                        printBG(player,screen)
                elif delete3.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("3")
                        saves[2]="3 save"
                        loads[2]="3 load"
                        dels[2]="3 delete"
                        
                        savesOBJ[2].text_setter("3 save")
                        loadOBJ[2].text_setter("3 load")
                        deleteOBJ[2].text_setter("3 delete")
                        
                        printBG(player,screen)
                elif delete4.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("4")
                        saves[3]="4 save"
                        loads[3]="4 load"
                        dels[3]="4 delete"
                        
                        savesOBJ[3].text_setter("4 save")
                        loadOBJ[3].text_setter("4 load")
                        deleteOBJ[3].text_setter("4 delete")
                        
                        printBG(player,screen)
                elif delete5.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("5")
                        saves[4]="5 save"
                        loads[4]="5 load"
                        dels[4]="5 delete"
                        
                        savesOBJ[4].text_setter("5 save")
                        loadOBJ[4].text_setter("5 load")
                        deleteOBJ[4].text_setter("5 delete")
                        
                        printBG(player,screen)
                elif delete6.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("6")
                        saves[5]="6 save"
                        loads[5]="6 load"
                        dels[5]="6 delete"
                        
                        savesOBJ[5].text_setter("6 save")
                        loadOBJ[5].text_setter("6 load")
                        deleteOBJ[5].text_setter("6 delete")
                        printBG(player,screen)
                elif delete7.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("7")
                        saves[6]="7 save"
                        loads[6]="7 load"
                        dels[6]="7 delete"
                        
                        savesOBJ[6].text_setter("7 save")
                        loadOBJ[6].text_setter("7 load")
                        deleteOBJ[6].text_setter("7 delete")
                        
                        printBG(player,screen)
                elif delete8.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("8")
                        saves[7]="8 save"
                        loads[7]="8 load"
                        dels[7]="8 delete"
                        
                        savesOBJ[7].text_setter("8 save")
                        loadOBJ[7].text_setter("8 load")
                        deleteOBJ[7].text_setter("8 delete")
                        
                        printBG(player,screen)
                elif delete9.draw_button():
                    if Button.Popup("delete", screen) == "Y": 
                        DB.delete("9")
                        saves[8]="9 save"
                        loads[8]="9 load"
                        dels[8]="9 delete"
                        
                        savesOBJ[8].text_setter("9 save")
                        loadOBJ[8].text_setter("9 load")
                        deleteOBJ[8].text_setter("9 delete")
                        printBG(player,screen)
                pg.display.update()
        pg.display.update()