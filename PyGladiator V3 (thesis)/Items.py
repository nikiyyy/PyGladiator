class item():

    def __init__ (self,ID,name,value,weight):
        self.ID=ID
        self.name=name
        self.value=value
        self.weight=weight
        
    def __str__(self):
        return self.name
    
    def returnName(self):
        return self.name
    
class M_weapons(item):
    #false - blunt    true - pearce 3 slash
    def __init__ (self,ID,name,damage_type,value,weight,damage,hands,atributes=None):
        super().__init__(ID,name,value,weight)
        self.damage_type=damage_type
        self.damage=damage
        self.hands=hands
        self.atributes=atributes
    
    def __str__(self):
        return " Gold {} | DMG:{} | TYPE:{} | {}".format(self.value, self.damage, self.damage_type, self.name)

        
class R_weapons(item):  
    ismagic=False #F normal, True staff
    def __init__ (self,ID,name,damage_type,value,weight,damage,hands,accuracy):
        super().__init__(ID,name,value,weight)
        self.damage_type=damage_type
        self.damage=damage  
        self.hands=hands
        self.accuracy=accuracy
        
    def __str__(self):
        return " Gold {} | DMG:{} | TYPE:{} | {}".format(self.value, self.damage, self.damage_type, self.name)
    
class C_armour(item):
                    #ligh - L medium - M Heavy - H
    def __init__ (self,ID,name,value,weight,armour_type,defence,atributes=None):
        super().__init__(ID,name,value,weight)
        self.defence=defence
        self.armour_type=armour_type
        self.atributes=atributes
        
    def __str__(self):
        return " Gold {} | DEF:{} | TYPE:{} | {}".format(self.value, self.defence, self.armour_type, self.name)
        
class C_shield(item):
    hands=1
    def __init__ (self,ID,name,value,weight,defence,size):
        super().__init__(ID,name,value,weight)
        self.defence=defence
        self.size=size
        
    def __str__(self):
        return " Gold {} | DEF:{} | TYPE:Shield | {}".format(self.value, self.defence, self.name)

class C_consumable(item):
    ComType='F' #F - food D - Drink S- stamina H Health
    def __init__ (self,ID,name,value,weight,ComType,modifier):
        super().__init__(ID,name,value,weight)
        self.ComType=ComType
        self.modifier=modifier#by how much a stat is going to be increased
        
    def __str__(self):
        return " Gold {} | DEF: +{} | TYPE:{} | {}".format(self.value, self.modifier, self.ComType, self.name)
        
    def use(self,user):
        if self.ComType=='F':
            user.curHealth+=self.modifier
        elif self.ComType=='D':
            user.curEnergy+=self.modifier
        elif self.ComType=='H':
            user.curHealth+=self.modifier
            print("healthmof", self.modifier )
        elif self.ComType=='E':
            user.curEnergy+=self.modifier

        
        
    
                    #ID,name,damage_type,value,weight,damage,hands):
weapon1=M_weapons(101,"Club",'B',3,1,4,1)
weapon2=M_weapons(102,"Dagger",'P',10,1,4,1)
weapon3=M_weapons(103,"Handaxe",'S',15,2,6,1)
weapon4=M_weapons(104,"Short Sword",'P',20,2,6,1)
weapon5=M_weapons(105,"Mace",'B',25,3,6,1)
weapon6=M_weapons(106,"Bastard Sword",'P',25,3,10,1)
weapon7=M_weapons(107,"Spear",'P',25,3,8,2)
weapon8=M_weapons(108,"Battle Axe",'S',35,5,12,2)
weapon9=M_weapons(109,"Great Sword",'S',35,5,12,2)
weapon10=M_weapons(110,"War Hammer",'B',35,5,12,2)


weapon69=M_weapons(500,"Nuke",'B',35,5,500,1)

Mweapons=(weapon1,weapon2,weapon3,weapon4,weapon5,weapon6,weapon7,weapon8,weapon9,weapon10)

    #ID,name,value,weight,type,defence 
armour1=C_armour(201,"Common Clothes",10,1,'L',1)
armour2=C_armour(202,"Noble Clothes",100,1,'L',1)
armour3=C_armour(203,"Hide",10,5,'L',3)
armour4=C_armour(204,"Padded",25,3,'L',3)
armour5=C_armour(205,"Leather",35,4,'L',5)
armour6=C_armour(206,"Studded Leather",45,5,'L',7)
armour7=C_armour(207,"Chain Mail",60,8,'M',9)
armour8=C_armour(208,"Scale Mail",75,9,'M',11)
armour9=C_armour(209,"Splint Mail",100,13,'H',15)
armour10=C_armour(210,"Plate",130,20,'H',20)

Armour=(armour1,armour2,armour3,armour4,armour5,armour6,armour7,armour8,armour9,armour10)
#(self,ID,name,value,weight,defence,size):
shield1=C_shield(301,"Buckler",20,2,3,'S')
shield2=C_shield(302,"Round Shield",15,5,6,'M')
shield3=C_shield(303,"Heater",20,7,8,'M')
shield4=C_shield(304,"kittle",25,8,10,'L')
shield5=C_shield(305,"Tower Shield",30,12,12,'L')

Shield=(shield1,shield2,shield3,shield4,shield5)

#ID,name,damage_type,value,weight,damage,hands,acuracy
R_weapon1=R_weapons(401,"hunting bow","P",4,5,5,2,25)
R_weapon2=R_weapons(402,"long bow","P",6,7,15,2,18)
R_weapon3=R_weapons(403,"Sling","S",3,1,2,2,10)
R_weapon4=R_weapons(404,"Javelin","P",3,1,2,1,10)

Ranged_weapons=(R_weapon1,R_weapon2,R_weapon3,R_weapon4)

potion1=C_consumable(501,"Small Health Potion",20,1,"H",30)
potion2=C_consumable(502,"Medium Health Potion",40,1,"H",60)
potion3=C_consumable(503,"Large Health Potion",60,1,"H",90)

pations=(potion1,potion2,potion3)

Food1=C_consumable(502,"bread",1,1,"F",5)
Food2=C_consumable(502,"apple",1,1,"F",7)
Food3=C_consumable(502,"cheese",2,1,"F",10)

foods=(Food1,Food2,Food3)
#hitchanse se generira dinamichno na momenta spored nivoto na igracha ,protivika, urujieto

listOfAllItems=[weapon69]
listOfAllItems.extend(Mweapons)
listOfAllItems.extend(Armour)
listOfAllItems.extend(Shield)
listOfAllItems.extend(Ranged_weapons)
listOfAllItems.extend(pations)
listOfAllItems.extend(foods)