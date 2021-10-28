import pygame as pg
clicked = False
class button():
    def __init__(self, x, y, width, height, text, color, screen, textSize):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.screen=screen
        self.textSize = textSize
        
    def draw_button(self):
        
        global clicked
        action = False
        pos = pg.mouse.get_pos()
        button_rect = pg.Rect(self.x, self.y, self.width, self.height) 
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                clicked = True
            elif pg.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
        else:
            if type(self.textSize) == int:
                font = pg.font.SysFont('Monotype Corsiva', self.textSize)
                text = font.render(self.text, True, self.color)
                self.screen.blit(text, (self.x + 30, self.y + 10))
            else:
                self.screen.blit(self.textSize, (self.x, self.y))
                
        return action
    
    def text_setter(self,text):
        self.text=text
        
    def text_getter(self):
        return self.text
     
    def color_setter(self,color):
        self.color=color
        
def Popup(caller, screen):
    if caller == "save" or caller == "delete":
        buttonYes = button(300, 350 ,50 ,50,  "Yes","red",screen, 40)
        buttonNo = button(400, 350 ,50 ,50, "No","red",screen, 40)
    else:
        buttonYes = button(300, 350 ,50 ,50,  "Left","red",screen, 40)
        buttonNo = button(400, 350 ,50 ,50, "Right","red",screen, 40)
    #buttonconf.png
    screen.blit(pg.image.load("buttonconf.png"), (300,300))
    # buttonBG = button(300, 300 ,250 ,150,  "","brown",screen, 40)
    
    # buttonBG.draw_button()
    pg.display.update()
    while True:
        for event in pg.event.get():
            pg.display.update()
            if event.type == pg.QUIT:
                pg.quit()
            elif buttonYes.draw_button():
                print("test2")
                return "Y"
            elif buttonNo.draw_button():
                print("test3")
                return "N"