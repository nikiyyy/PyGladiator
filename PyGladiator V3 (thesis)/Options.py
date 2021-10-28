import pygame 
class Gameoptions():
    
    def __init__(self, file=None ):
        self.WIDTH = 800
        self.DIMENTIONS = 50
        #self.sq_size = self.width // self.diemention
        self.art = True
        self.volume = 0
        self.sound = 0
        self.difficulty = "Easy"
        self.BGs = [pygame.image.load("BG/test1.png"),pygame.image.load("BG/test2.png"),pygame.image.load("BG/test3.png"),pygame.image.load("BG/options.png"),pygame.image.load("BG/mainmenu.png"),pygame.image.load("BG/battle.png"),pygame.image.load("BG/castle.png"),pygame.image.load("BG/youdiedPH.jpg"),pygame.image.load("BG/market.png"),pygame.image.load("BG/wincond.png"),pygame.image.load("BG/credits.png")]
        self.myfont = pygame.font.SysFont("Monotype Corsiva", 20)
        
    def createfile(self):
        with open('ini.txt', 'w') as f:
            f.write(str(self.art)+"/"+str(self.volume)+"/"+str(self.sound)+"/"+str(self.difficulty))
            
    def loadfile(self):
        try:
            with open('ini.txt') as f:
                fileContent=f.readlines()
                holdoptions=fileContent[0].split("/")
                print(type(holdoptions[0]))
                if holdoptions[0] == "True":
                    self.art = True
                else: self.art = False
                # self.volume = int(holdoptions[1])
                # self.sound = int(holdoptions[2])
                self.difficulty = holdoptions[3]
        except:
            with open('ini.txt', 'w') as f:
                f.write(str(self.art)+"/"+str(self.volume)+"/"+str(self.sound)+"/"+str(self.difficulty))
            