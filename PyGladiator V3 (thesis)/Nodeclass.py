import pygame

RED = (255, 0, 0) #
GREEN = (0, 255, 0) #
BLUE = (0, 0, 255) #
YELLOW = (255, 255, 0) #
WHITE = (255, 255, 255) #
BLACK = (0, 0, 0) #
PURPLE = (128, 0, 128) #
ORANGE = (255, 165 ,0) #
GREY = (128, 128, 128) #
TURQUOISE = (64, 224, 208) #
# 3 layers
#train
#actors
#navogation (colors)
class Node:
    def __init__(self, row, col, width, total_rows):
        self.terrain = "0"
        self.occupied = "0"
        self.neighbors = []
        self.row = row    
        self.col = col  
        self.color = WHITE # relace with navigation
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE
    
    def make_start(self):
        self.color = ORANGE
        
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def draw(self, win):

        if self.terrain == "1":
            # pygame.Surface.blit( win,pygame.image.load("tile.png").convert_alpha(), (self.x, self.y, self.width, self.width))
            pygame.draw.rect(win, "#286036", (self.x, self.y, self.width, self.width))
        elif self.terrain == "2":
            pygame.Surface.blit( win,pygame.image.load("sprites/crown.png").convert_alpha(), (self.x, self.y, self.width, self.width))
        elif self.terrain == "0":
            pygame.draw.rect(win, "#2c9646", (self.x, self.y, self.width, self.width))
        elif self.terrain == "3":
            pygame.Surface.blit( win,pygame.image.load("sprites/castle.png").convert_alpha(), (self.x, self.y, self.width, self.width))
        #draw actors
        if self.occupied == "1":
            pygame.draw.circle(win, ORANGE, (self.x+7, self.y+7), self.width/2)
        elif self.occupied == "2":
            pygame.draw.circle(win, RED, (self.x+7, self.y+7), self.width/2)
        # else: pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

            
    def update_neighbors(self, grid): #4testing
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].terrain == "1": # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].terrain == "1": # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].terrain == "1": # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].terrain == "1": # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
        
    def __lt__(self, other):
        return False