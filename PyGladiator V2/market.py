import Items 
import os

class shop():
    #special inventory items sold by player for 24 hours
    #reputation with player
    #

  def  __init__(self):
      self.boughtItems=[]
  
  def menu(self,player):
      try:
          while True:
              os.system('cls')
              print("gold",player.money)
              izbor=input("1. buy \n2. sell \n3.exit\nEnter the coresponding number")
              if izbor=="1":
                  availible=[]
                  index=0
                  availible.extend(Items.Mweapons)
                  availible.extend(Items.Armour)
                  availible.extend(Items.pations)
                  availible.extend(Items.Shield)
                  for i in availible:
                      if i.value-player.stats["DIP"]<=0:
                          print(index,i,1)
                      else:
                          print(index,i,i.value-player.stats["DIP"])
                      index+=1
                  buy=input("Enter the coresponding number\nInput E to exit")   
                  if availible[int(buy)].value-player.stats["DIP"]<=0:
                      if player.money>=1:
                          player.money-=1
                          player.Inventory.append(availible[int(buy)])
                      else:
                          print("not enough gold")
                  else:
                      if player.money>=availible[int(buy)].value-player.stats["DIP"]:
                          player.money-=availible[int(buy)].value-player.stats["DIP"]
                          player.Inventory.append(availible[int(buy)])
                      else:
                          print("not enough gold")
                  
              elif izbor=="2":
                  index=0
                  print(player.money,"money")
                  for i in player.Inventory:
                      print(index,i,i.value//2)
                      index+=1
                  sell=input("Enter the coresponding number\nInput E to exit")
                  player.money+=player.Inventory[int(sell)].value//2
                  #add to special items
                  self.boughtItems.append(player.Inventory[int(sell)])
                  del player.Inventory[int(sell)]
                  
              elif izbor=="3":
                  break
      except:  
          print("invalid input")
geniral_goods=shop()