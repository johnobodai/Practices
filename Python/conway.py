#!/usr/bin/python3

# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Creates a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0;
        column.append('#') # Add a living cell.
    else:
        column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.
