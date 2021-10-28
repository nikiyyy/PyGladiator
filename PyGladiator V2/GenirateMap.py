from random import randint #izpolzva se za generorane na proizvolni chesla
import os

def genmap(x,y,terain,objpass=None ,caller=None,enemnum=1,enemy=None,enemy2=None,enemy3=None,enemy4=None,enemy5=None):   #caller = 1 - player your || caller = 2 - enemy tirn
    biglist=[]
    cx=objpass.X_cord# cx stava X kodinata na player obekta
    cy=objpass.Y_cord# cy stava Y kodinata na player obekta
    tempx=cx# vremenni promenlivi
    tempy=cy#
    if objpass.combatmap==[]:#tuk vliza samo vednuj v nachaloto na bitka, ako veche naqma generirana karta
        cx=2# dava startova poziciq na igracha
        cy=int(y/2)
        tempx=cx
        tempy=cy
        rowlist=[]
        for i in range(0,x): #generira teren - 0-obsicle 1-free 2-player 3-enemy1
            for j in range(0,y): #Pulni biglist red po red spored rowlist
                if terain==0:
                    rowlist.append('1')
                elif terain==1:
                    if randint(0,(y*x)/5)==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==2:
                    if randint(0,int((y*x)/7))==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==3:
                    if randint(0,int((y*x)/10))==5:
                        rowlist.append('0') 
                    else: 
                        rowlist.append('1')
                elif terain==4:
                    if randint(0,int((y*x)/13))==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==5:
                    if randint(0,int((y*x)/16))==5:
                        rowlist.append('0') 
                    else: 
                        rowlist.append('1')
            biglist.append(rowlist)
            rowlist=[]
        if enemnum>=1: #nasilstveno(override stara poziciq) postavq protivnici
            biglist[int(y/2)][x-2]='3'
            enemy.Y_cord=int(y/2)
            enemy.X_cord=x-2
            if enemnum>=2:
                biglist[int(y/2)+2][x-2]='3'
                enemy2.Y_cord=int(y/2)+2
                enemy2.X_cord=x-2
                if enemnum>=3:
                    biglist[int(y/2)-2][x-2]='3'
                    enemy3.Y_cord=int(y/2)-2
                    enemy3.X_cord=x-2
                    if enemnum>=4:
                        biglist[int(y/2)-4][x-2]='3'
                        enemy4.Y_cord=int(y/2)-4
                        enemy4.X_cord=x-2
                        if enemnum>=5:
                            biglist[int(y/2)+4][x-2]='3'
                            enemy5.Y_cord=int(y/2)+4
                            enemy5.X_cord=x-2
        objpass.combatmap=biglist#veche gotovata karta se zapazva v instance na player obekta 
        
    else: biglist=objpass.combatmap
    
    while True:
        try:#izkarvane na jartata na konzola
            os.system('cls')
            print("movement points "+str(objpass.movement_points))
            print("your health : "+str(objpass.curHealth)+"/"+str(objpass.maxHealth))
            biglist[tempy][tempx]='1'#iztriva starata poziciq
            biglist[cy][cx]='2'
            for i in biglist:#iterira prez vseki eliment i go izpisva na konzola
                print("|")
                for j in i:     # 0 = unavalable , 1 = free , 2 = You , 3 = Enemy
                    if j =='1':
                        print('|__', end = '')
                    elif j =='2':
                        print ('|██',end = '')
                    elif j =='0':
                        print('|▒▒', end = '')
                    elif j =='3':

                        
                        if biglist.index(i)==enemy.Y_cord and i.index(j)==enemy.X_cord:
                            enemy.printme()
                        elif biglist.index(i)==enemy2.Y_cord and i.index(j)==enemy2.X_cord:
                            enemy2.printme()
                        elif biglist.index(i)==enemy3.Y_cord and i.index(j)==enemy3.X_cord:
                            enemy3.printme()
                        elif biglist.index(i)==enemy4.Y_cord and i.index(j)==enemy4.X_cord:
                            enemy4.printme()
                        elif biglist.index(i)==enemy5.Y_cord and i.index(j)==enemy5.X_cord:
                            enemy5.printme()
                        
                        
                            
            print("|",end = '')
            biglist[tempy][tempx]='1'
            biglist[cy][cx]='2'
            tempx=cx
            tempy=cy
            objpass.X_cord=cx
            objpass.Y_cord=cy
            if caller == 1:#ako hoda na igracha, toi shte ima vuzmojnost da se dviji
                inp=input("\nInput a,s,d,w or a combination like as,aw,wd,ds to move in that derection \nInput E or e to leave\n")
                if inp=="s":
                    if biglist[cy+1][cx]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy+=1
                    objpass.movement_points-=1
                elif inp=="w":
                    if biglist[cy-1][cx]!='1' or objpass.movement_points<=0 or cy-1<0 :
                        raise IndexError
                    cy-=1
                    objpass.movement_points-=1
                elif inp=="d":
                    if biglist[cy][cx+1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="a":
                    if biglist[cy][cx-1]!='1' or objpass.movement_points<=0 or cx-1<0:
                        raise IndexError
                    cx-=1
                    objpass.movement_points-=1
                elif inp=="aw" or inp=="wa":
                    if biglist[cy-1][cx-1]!='1' or objpass.movement_points<=0 or cx-1<0 or cx-1<0:
                        raise IndexError
                    cy-=1
                    cx-=1
                    objpass.movement_points-=1
                elif inp=="dw" or inp=="wd":
                    if biglist[cy-1][cx+1]!='1' or objpass.movement_points<=0 or cy-1<0:
                        raise IndexError
                    cy-=1
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="ds" or inp=="sd":
                    if biglist[cy+1][cx+1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy+=1
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="as" or inp=="sa":
                    if biglist[cy+1][cx-1]!='1' or objpass.movement_points<=0 or cx-1<0:
                        raise IndexError
                    cy+=1
                    cx-=1
                    objpass.movement_points-=1
                elif inp =="E" or inp =="e":#"gg" e za prekluchvane na dvijenieto
                    break
                else: print("Invalid Input")
            elif caller == 2:
                print("\nEnemy thinkng:\n")#hoda na privnika
                if enemnum>=1:
                    if enemy.alive==True or enemy.curHealth>0:
                        biglist=enemy.move(biglist,objpass)#vzema kartata updejtva q v svoq chlen funkciq i a vrushta obratno
                    if enemnum>=2:
                        if enemy2.alive==True or enemy2.curHealth>0:
                            biglist=enemy2.move(biglist,objpass)
                        if enemnum>=3:
                            if enemy3.alive==True or enemy3.curHealth>0:
                                biglist=enemy3.move(biglist,objpass)
                            if enemnum>=4:
                                if enemy4.alive==True or enemy4.curHealth>0:
                                    biglist=enemy4.move(biglist,objpass)
                                if enemnum>=5:
                                    if enemy.alive==True or enemy5.curHealth>0:
                                        biglist=enemy5.move(biglist,objpass)
                                       
                objpass.combatmap=biglist
                break
            else:
                break
        except IndexError:
            cx=tempx
            cy=tempy