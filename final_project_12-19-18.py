#Conway's Game of Life rules (found on Wikipedia):
    #1: Live cell with fewer than two neighbors dies (underpopulation)
    #2: Live cell with two or three neighbors lives
    #3: Live cell with more than three neighbors dies (overpopulation)
    #4: Dead cell with exactly three neighbors becomes a live cell (reproduction)

import random

rows = 10
cols = 10

class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
    def __str__(self):
        return f"{self.x}, {self.y}: {self.alive}"
    __repr__ = __str__

cells = []

for y in range(rows):
    row = []
    for x in range(cols):
        row.append(Cell(x, y, random.choice([True, False])))
    cells.append(row)

for row in cells:
    for cell in row:
        if cell.alive:
            print("X", end = " | ")
        else:
            print(" ", end = " | ")
    print(" ")