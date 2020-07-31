import keyboard
import pygame
import Constants
import sys
import numpy as np
from random import randint
import time 

def copy(T):
    tTemp = np.zeros((Constants.NUMBER_OF_BLOCKS_HIGH, Constants.NUMBER_OF_BLOCKS_WIDE), dtype=np.int)
    for i in range(len(T)):
        for j in range(len(T[i])):
            tTemp[i][j] = T[i][j]
    return tTemp



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
    rows, cols = Constants.NUMBER_OF_BLOCKS_HIGH, Constants.NUMBER_OF_BLOCKS_WIDE

    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i

    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            if ((i == x) and (j == y)):
                count += 0
            elif T[x][y] == 1:
                count += 1    
    return count<2 or count>3


def check_dead_cell(T, i, j):
    count = 0
    
    rows, cols = Constants.NUMBER_OF_BLOCKS_HIGH, Constants.NUMBER_OF_BLOCKS_WIDE
    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i

    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            if ((i == x) and (j == y)):
                count += 0
            if T[x][y] == 1:
                count += 1
    return ((count>2) and (count<4))
    
if __name__ == "__main__":
    #set the grid size
    rows = int(input("Enter how many rows: "))
    cols = int(input("Enter how many columns: "))

    Constants.NUMBER_OF_BLOCKS_HIGH = rows
    Constants.NUMBER_OF_BLOCKS_WIDE = cols

    Constants.BLOCK_HEIGHT = round(Constants.SCREEN_HEIGHT/Constants.NUMBER_OF_BLOCKS_HIGH)
    Constants.BLOCK_WIDTH = round(Constants.SCREEN_WIDTH/Constants.NUMBER_OF_BLOCKS_WIDE)

    T = np.zeros((Constants.NUMBER_OF_BLOCKS_HIGH, Constants.NUMBER_OF_BLOCKS_WIDE), dtype=np.int)

    for i in range(int((Constants.NUMBER_OF_BLOCKS_HIGH*Constants.NUMBER_OF_BLOCKS_WIDE)/3)):
        T[randint(0, len(T)-1)][randint(0, len(T[0])-1)] = 1


    pygame.init()
    surface = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    pygame.display.set_caption("conway game of life")
    surface.fill(Constants.YELLOW)
    tempT = copy(T)
    while True:
        pygame.event.pump()
        if keyboard.is_pressed('q'):
            pygame.quit()
            sys.exit()
        draw_map(surface, T)
        pygame.display.update()
        print_matrix(tempT)
        #check every cell
        for i in range(len(T)):
            for j in range(len(T[i])):
                if T[i][j] == 1:
                    if check_alive_cell(T, i, j):
                        tempT[i][j] = 0
                else:
                    if check_dead_cell(T, i, j): 
                        tempT[i][j] = 1
        T = copy(tempT)
 









