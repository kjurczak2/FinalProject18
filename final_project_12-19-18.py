#Conway's Game of Life rules (found on Wikipedia):
    #1: Live cell with fewer than two neighbors dies (underpopulation)
    #2: Live cell with two or three neighbors lives
    #3: Live cell with more than three neighbors dies (overpopulation)
    #4: Dead cell with exactly three neighbors becomes a live cell (reproduction)

import random
import time
import pygame

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("game of life")
clock = pygame.time.Clock()

run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

rows = 10
cols = 10

class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.north = self.y - 1
        if self.y == 0:
            self.north = cols - 1
        self.east = self.x + 1
        if self.x == rows - 1:
            self.east = 0
        self.south = self.y + 1
        if self.y == cols - 1:
            self.south = 0
        self.west = self.x - 1
        if self.x == 0:
            self.west = rows - 1


    def check_neighbors(self):
        """Check neighboring cells' status when given the center cell"""
        #cell coordinates: (y,x)
        #rows: (0,0) (0,1) (0,2) . . .
        #cols: (0,0) (1,0) (2,0) . . .
        n = ((self.north), (self.x))
        ne = ((self.north), (self.east))
        e = ((self.y), (self.east))
        se = ((self.south), (self.east))
        s = ((self.south), (self.x))
        sw = ((self.south), (self.west))
        w = ((self.y), (self.west))
        nw = ((self.north), (self.west))
        locations = [n, ne, e, se, s, sw, w, nw]
        neighbors = []
        #print(f"getting neighbors of {self.y} {self.x} now - {self.alive}")
        for loc in locations:
            #print(loc)
            neighbors.append(cells[loc[0]][loc[1]])
        return neighbors

    def neighbors_status(self, neighbor_cells):
        """Check status of neighboring cells (either alive or dead)"""
        live_neighbors = 0
        for n in neighbor_cells:
            if n.alive == True:
                live_neighbors += 1
        #print(live_neighbors)
        return live_neighbors

    def next_gen(self, live_neighbors):
        """Move from one generation to the next; determine if cells survive based on number of live neighbors"""
        if self.alive == True:
            if live_neighbors < 2:
                self.alive = False
            elif live_neighbors == 2 or live_neighbors == 3:
                self.alive = True
            elif live_neighbors >= 4:
                self.alive = False
        if self.alive == False:
            if live_neighbors == 3:
                self.alive = True
        #print(f"{self.alive}")

    #def __str__(self):
        #return f"{self.x}, {self.y}: {self.alive}"
    #__repr__ = __str__

cells = []

for y in range(rows):
    #print("Making a row")
    row = []
    for x in range(cols):
        row.append(Cell(x, y, random.choice([True, False])))
    cells.append(row)

def print_grid():
    """print grid for game, marking all live cells"""
    for row in cells:
        for cell in row:
            if cell.alive:
                print("X", end = " | ")
            else:
                print(" ", end = " | ")
        print(" ")
    print("________________________________________")

while True:
    print_grid()
    time.sleep(1)
    for row in cells:
        for cell in row:
            neighbors = cell.check_neighbors()
            live_neighbors = cell.neighbors_status(neighbors)
            cell.next_gen(live_neighbors)