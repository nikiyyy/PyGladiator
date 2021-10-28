import combat as comb
import Player as PL
import Database as DB
import market
from datetime import datetime
import tkinter as tk
from PIL import ImageTk
import os

player=PL.Player("human",3,200)



def main():   
    try:    
        while True:
            os.system('cls')
            izbor=input("\n1.Fight\n2.Open inventory\n3.Player progress\n4.Shop\n5.Save game\n6.Load game \n7.Delete saved game\n8.Exit\nInput the coresponding number")
            if izbor == "1":
                os.system('cls')
                fight=input("Fight against \n1. One opponent\n2. Two opponents\n3. Three opponents\n4. Four opponents\n5. Five oponents \n6. Cancel Battle")
                if fight == "1":
                    comb.Combat(player,1,"Pit_Fighter",enemNam1="Gladiator") 
                elif fight == "2":
                    comb.Combat(player,2,"Thug",emem2type="Bandit") 
                elif fight == "3":
                    comb.Combat(player,3,"Thug",emem2type="Bandit",emem3type="Bandit") 
                elif fight == "4":
                    comb.Combat(player,4,"Thug",emem2type="Bandit",emem3type="Bandit",emem4type="Bandit")  
                elif fight == "5":
                    comb.Combat(player,5,"Thug",emem2type="Bandit",emem3type="Pit_Fighter",emem4type="Pit_Fighter",emem5type="Pit_Fighter")             
                player.reset()
            elif izbor == "2":
                player.Inventory_manage("menu")
            elif izbor == "3":
                player.atribute_poins()
            elif izbor == "4":
                market.geniral_goods.menu(player)
            elif izbor == "5":
                savename = input("chose a save name")
                
                if player.equippedOH==None and player.equippedW==None and player.equippedA==None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel,None, None, None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH!=None and player.equippedW==None and player.equippedA==None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH==None and player.equippedW!=None and player.equippedA==None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH==None and player.equippedW==None and player.equippedA!=None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH!=None and player.equippedW!=None and player.equippedA==None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH!=None and player.equippedW==None and player.equippedA!=None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                elif player.equippedOH==None and player.equippedW!=None and player.equippedA!=None:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
                
                else:
                    DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))#stats, skill, abp, money, XP, inv
            
            elif izbor == "6":
                try:
                    DB.view()
                    loald = input("chose a save name to load")
                    player.loadFromFile(DB.load(loald))
                except:
                    print("error")
            elif izbor == "7":
                DB.view()
                loald = input("chose a save name to Delete")
                DB.delete(loald)
            elif izbor == "8":
                print("end game")   
                break
            else:print("invalid input")
    except:
        print("invalid input")
        main()

def newgame():
    root.destroy()
    player.char_create()
    print("you look ready for battle. Fight!")
    main()
    
    
def loadsave():
    try:
        root.destroy()
        DB.view()
        loald = input("\nInput a save name to load: ")
        player.loadFromFile(DB.load(loald))
        main()
    except:
        print("ivalid input")
        DB.view()
        loald = input("chose a save name to load")
        player.loadFromFile(DB.load(loald))
        main()
    
def end():
        root.destroy()
        
root=tk.Tk()

root.title("Py Gladiator")
root.iconbitmap('coli.ico')#C:\\Users\\Kolio\\Desktop\\coli.ico
root.resizable(width=False, height=False) 
C = tk.Canvas(root, height=480, width=360)
filename = ImageTk.PhotoImage(file = 'background.jpg')#C:\\Users\\Kolio\\Desktop\\background.jpg
background_label = tk.Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()



button1 = tk.Button(root, text="New game", fg="Black",bg='#941212', width = 12,command=newgame)
button1.place(x=50,y=175)

button2 = tk.Button(root, text="Load game", fg="Black",bg='#941212', width = 12,command=loadsave)
button2.place(x=50,y=225)

button3 = tk.Button(root, text="Exit", fg="Black",bg='#941212', width = 12,command=end)
button3.place(x=50,y=275)

root.mainloop()