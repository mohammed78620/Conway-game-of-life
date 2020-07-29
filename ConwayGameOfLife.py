import keyboard
from copy import copy, deepcopy
import pygame
import Constants
import sys
import numpy as np
from random import randint
import time 

def get_tile_colour(no):
    tile_color = Constants.YELLOW
    if no == 1:
        tile_color = Constants.BLACK
    return tile_color

def draw_map(surface, T):
    for i in range(len(T)):
        for j in range(len(T[i])):
            myrect = pygame.Rect(i*Constants.BLOCK_WIDTH, j*Constants.BLOCK_HEIGHT, Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT)
            pygame.draw.rect(surface, get_tile_colour(T[i][j]), myrect)

def print_matrix(T):
    for i in range(len(T)):
        print(T[i])
    print()
            


def check_alive_cell(T, i, j):
    count = 0
    rows, cols = Constants.BLOCK_HEIGHT, Constants.BLOCK_WIDTH

    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i

    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            # print(x, " ", y , " --->", T[x][y])
            if ((i == x) and (j == y)):
                count += 0
            elif T[x][y] == 1:
                count += 1    
            
    
                
    # print()
    # print("count is ==",count,"i,j == ",i," ",j)
    # print()
    return count<2 


def check_dead_cell(T, i, j):
    count = 0
    
    rows, cols = Constants.BLOCK_HEIGHT, Constants.BLOCK_WIDTH
    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i

    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            if T[x][y] == 1:
                count += 1
    return count>2 

# T = [[0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,1,0,0,0,1,0,0],
#     [0,0,0,0,0,1,0,0,0,0,0,0],
#     [0,0,0,0,0,1,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,1,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0]]

T = np.zeros((Constants.NUMBER_OF_BLOCKS_HIGH, Constants.NUMBER_OF_BLOCKS_WIDE), dtype=np.int)
# T = np.random.randint(0,2, size=(Constants.NUMBER_OF_BLOCKS_HIGH,Constants.NUMBER_OF_BLOCKS_WIDE))

T[4][6] = 1
T[5][6] = 1
T[6][6] = 1

for i in range(185):
    T[randint(0, len(T)-1)][randint(0, len(T[0])-1)] = 1


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
YELLOW = (200, 200, 20)

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("hello world")
surface.fill(Constants.YELLOW)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.K_e:
            pygame.quit()
            sys.exit()
        draw_map(surface, T)
        pygame.display.update()
        tempT = deepcopy(T)
        # keyboard.wait('space')
        time.sleep(0.5)
        # print_matrix(tempT)
        #check every cell
        for i in range(len(T)):
            for j in range(len(T[i])):
                if T[i][j] == 1:
                    if check_alive_cell(T, i, j):
                        tempT[i][j] = 0
                        print()
                    # print(i,j)
                if T[i][j] == 0:
                    # print(check_dead_cell(tempT, i, j))
                    if check_dead_cell(T, i, j): 
                        tempT[i][j] = 1
        print_matrix(T)
        T = deepcopy(tempT)

        









