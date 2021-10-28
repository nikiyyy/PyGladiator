class Spacialisation():
    spelldict={}#key - name value - energie soust
    def abilitylist():
        pass
    #activates spells


class Rogue(Spacialisation):
    profession="Rogue"
    abilitylist={}
    def menu(self):
        for i in self.abilitylist:
            print(i)

class Warrior(Spacialisation):
    profession="Warrior"
    abilitylist={"test1":15,"test2":20}
    def menu(self,user):
        for i in self.abilitylist:
            print(i)

class Ranger(Spacialisation):
    profession="Ranger"
    abilitylist={"":"","":""}
    def menu(self,user):
        for i in self.abilitylist:
            print(i)

class Mage(Spacialisation):
    profession="Mage"
    abilitylist={}
    def menu(self):
        input("lol")

rogueInst=Rogue()
warriorInst=Warrior()
rangerInst=Ranger()
mageInst=Mage()