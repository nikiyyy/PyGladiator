# import Options
# import math
import pygame
from random import randint
from queue import PriorityQueue
# import Player as PL
import enemyParty
import combat
import Inventory
import Progression
import Nodeclass
# from Menu import cityMenu
import screens


##################################


##################################
##temporary

 ##


        
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw, grid, enemy, player, screen): 
    lastpos=[]
    while current in came_from:
        current = came_from[current]
        current.make_path()
        lastpos.append(current) #putq do igracha
    for i in grid:
        for j in i:
            if j.occupied=="2":
                try:
                    if grid[lastpos[-2].row][lastpos[-2].col].occupied != "2":
                        grid[lastpos[-2].row][lastpos[-2].col].occupied="2"
                        enemy.startnode=grid[lastpos[-2].row][lastpos[-2].col]
                        grid[lastpos[-1].row][lastpos[-1].col].occupied="0" #mahane na starata poziciq
                    
                except IndexError:
                    if combat.stratcombat(screen, player, enemy.enemyObjsList) == False:
                        enemy.startnode=None
                        grid[lastpos[0].row][lastpos[0].col].occupied="0"
                    pass
                    

def algorithm(draw, grid, start, end, enemy, player, screen):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}
    
    
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
# 				print("gg1")
		current = open_set.get()[2]
		open_set_hash.remove(current)
# 		print(current)
		if current == end:

			reconstruct_path(came_from, end, draw, grid, enemy, player, screen)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1
# 			print("gg1")
			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

# 		draw()   # ne mi trqbva

		if current != start:
			current.make_closed()

	return False
# 1 - opein terrain 
# 2 - barrier

#player.gameSettings.WIDTH, player..DIMENTIONS
def make_grid(player):
    player.enemiesOnMap=[]
    grid = []
    gap = player.optionSettings.WIDTH // player.optionSettings.DIMENTIONS
    for i in range(player.optionSettings.DIMENTIONS):
        grid.append([])
        for j in range(player.optionSettings.DIMENTIONS):
            node = Nodeclass.Node(i, j, gap, player.optionSettings.DIMENTIONS)
            node.terrain="0"
            if randint(0,3) == 0:
                # node.make_barrier()#obsolite
                node.terrain="1"
            grid[i].append(node)
            
    grid[player.X_cord][player.Y_cord].make_start() 
    grid[player.X_cord][player.Y_cord].occupied = "1"
    grid[player.X_cord][player.Y_cord].terrain = "0"
    
    for i in range(player.levelStage+1):#
        EP=enemyParty.EnemyParty(randint(1, player.optionSettings.DIMENTIONS-1), randint(0, player.optionSettings.DIMENTIONS-1), player.optionSettings.difficulty)
        while grid[EP.X_cord][EP.Y_cord].terrain == "1":
            EP=enemyParty.EnemyParty(randint(1, player.optionSettings.DIMENTIONS-1), randint(0, player.optionSettings.DIMENTIONS-1),player.optionSettings.difficulty)
        grid[EP.X_cord][EP.Y_cord].occupied = "2"
        EP.startnode=grid[EP.X_cord][EP.Y_cord]
        player.enemiesOnMap.append(EP)
    
        
    grid[randint(1, player.optionSettings.DIMENTIONS-1)][randint(1, player.optionSettings.DIMENTIONS-1)].terrain = "3"
    grid[randint(1, player.optionSettings.DIMENTIONS-1)][randint(1, player.optionSettings.DIMENTIONS-1)].terrain = "2"
    
    grid[player.optionSettings.DIMENTIONS-1][player.optionSettings.DIMENTIONS-1].make_end()
    return grid


def draw_grid(win, player):
    #gap = width // rows
    gap =player.optionSettings.WIDTH // player.optionSettings.DIMENTIONS
    for i in range(player.optionSettings.DIMENTIONS):
        pygame.draw.line(win, Nodeclass.BLACK, (0, i * gap), (player.optionSettings.WIDTH, i * gap))
        for j in range(player.optionSettings.DIMENTIONS):
            pygame.draw.line(win, Nodeclass.BLACK, (j * gap, 0), (j * gap, player.optionSettings.WIDTH))
        
def draw(win, player):
    win.fill(Nodeclass.WHITE)
    for row in player.worldmap:
        for node in row:
            node.draw(win)
            

    draw_grid(win, player)
    pygame.display.update()


# def get_clicked_pos(pos, rows, width):
#     gap = width // rows
#     y, x = pos

#     row = y // gap
#     col = x // gap

#     return row, col    
        
def checkForValidroute(draw, grid, start, end, enemy, player, screen):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}
    
    
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		current = open_set.get()[2]
		open_set_hash.remove(current)
		if current == end:

			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1
			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		if current != start:
			current.make_closed()

	return False

def main(WIN, player):#winCondition(player, screen)
    if player.levelStage == 50:
        screens.winCondition(player, WIN)
        
    
    player.reset()
    player.worldmap=make_grid(player)# creates the grid for the player
    player.movement_point=5 #testing
    #########
    row=0
    #########
    for i in player.worldmap:
        for j in i:
            if j.occupied=="1":
                startalg=j
                
    for i in player.worldmap:
        for j in i:
            if j.terrain == "2":
                endalg=j
    ######### check for possibile game           
    while checkForValidroute(lambda: draw(WIN, player), player.worldmap, startalg, endalg, i, player, WIN) == True:
        player.worldmap=make_grid(player)
    #########
    for i in player.worldmap: #
        for j in i:
            if j.is_start():
                start=j
            elif j.is_end():
                end=j
                
    run = True
    while run:
        draw(WIN, player) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # breakme = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #and start and end:
                            
                    player.movement_point=5
                    if event.key == pygame.K_SPACE and start and end:
                        for row in player.worldmap:
                            for spot in row:
                                spot.update_neighbors(player.worldmap)
                                   
                        for i in player.worldmap:
                            for j in i:
                                if j.occupied=="1":
                                    algEnd=j

                        for i in player.enemiesOnMap:
                            # print("jk")
                            if i.startnode != None:
                                algorithm(lambda: draw(WIN, player), player.worldmap, i.startnode, algEnd, i, player, WIN)
                            else: continue
                if event.key == pygame.K_w:
                    if player.worldmap[player.X_cord][player.Y_cord-1].terrain != "1" and player.worldmap[player.X_cord][player.Y_cord-1].occupied != "2" and player.movement_point>0 and player.Y_cord-1>=0:
                        player.worldmap[player.X_cord][player.Y_cord].occupied="0"
                        player.Y_cord-=1
                        player.worldmap[player.X_cord][player.Y_cord].occupied="1"
                        player.movement_point-=1
                        if player.worldmap[player.X_cord][player.Y_cord].terrain == "3":
                            screens.cityMenu(WIN, player)
                        elif player.worldmap[player.X_cord][player.Y_cord].terrain == "2":
                            player.levelStage+=1
                            return
          
                if event.key == pygame.K_a:
                    if player.worldmap[player.X_cord-1][player.Y_cord].terrain != "1" and player.worldmap[player.X_cord-1][player.Y_cord].occupied != "2"and player.movement_point>0 and player.X_cord-1>=0:
                        player.worldmap[player.X_cord][player.Y_cord].occupied="0"
                        player.X_cord-=1
                        player.worldmap[player.X_cord][player.Y_cord].occupied="1"
                        player.movement_point-=1
                        if player.worldmap[player.X_cord][player.Y_cord].terrain == "3":
                            screens.cityMenu(WIN, player)
                        elif player.worldmap[player.X_cord][player.Y_cord].terrain == "2":
                            player.levelStage+=1
                            return
                try:
                    if event.key == pygame.K_s:
                        if player.worldmap[player.X_cord][player.Y_cord+1].terrain != "1" and player.worldmap[player.X_cord][player.Y_cord+1].occupied != "2" and player.movement_point>0:
                            player.worldmap[player.X_cord][player.Y_cord].occupied="0"
                            player.Y_cord+=1
                            player.worldmap[player.X_cord][player.Y_cord].occupied="1"
                            player.movement_point-=1
                            if player.worldmap[player.X_cord][player.Y_cord].terrain == "3":
                                screens.cityMenu(WIN, player)
                            elif player.worldmap[player.X_cord][player.Y_cord].terrain == "2":
                                player.levelStage+=1
                                return
                            
                    if event.key == pygame.K_d:
                        if player.worldmap[player.X_cord+1][player.Y_cord].terrain != "1" and player.worldmap[player.X_cord+1][player.Y_cord].occupied != "2" and player.movement_point>0:
                            player.worldmap[player.X_cord][player.Y_cord].occupied="0"
                            player.X_cord+=1
                            player.worldmap[player.X_cord][player.Y_cord].occupied="1"
                            player.movement_point-=1
                            if player.worldmap[player.X_cord][player.Y_cord].terrain == "3":
                                screens.cityMenu(WIN, player)
                                
                            elif player.worldmap[player.X_cord][player.Y_cord].terrain == "2":
                                player.levelStage+=1
                                return
                                
                except IndexError:
                    pass
                if event.key == pygame.K_m:
                    screens.menuNavMap(WIN, player)
                    
                
                if event.key == pygame.K_p:
                    Progression.progress(WIN, player)
                
                if event.key == pygame.K_i:
                    Inventory.Inventory_manage(WIN, player)
                    
                if event.key == pygame.K_b: #debug generate map
                    screens.mainmenu(WIN, player)
                    
                    
                #player.worldmap[player.X_cord][player.Y_cord].am_i_touching(player.worldmap)
                # if player.worldmap[player.X_cord][player.Y_cord].NextLVL() == True:
                #     return
                
                if player.movement_point==0:
                    if player.optionSettings.difficulty == "Easy":
                        player.movement_point=2
                    elif player.optionSettings.difficulty == "Medium" or player.optionSettings.difficulty == "Hard" :
                        player.movement_point=1
                    for row in player.worldmap:
                        for spot in row:
                            spot.update_neighbors(player.worldmap)
                               
                    for i in player.worldmap:
                        for j in i:
                            if j.occupied=="1":
                                algEnd=j

                    for i in player.enemiesOnMap:
                       if i.startnode != None:
                           algorithm(lambda: draw(WIN, player), player.worldmap, i.startnode, algEnd, i, player, WIN)
                       else: continue
                        
    pygame.quit()
    

# while True:  
#     main(WIN)