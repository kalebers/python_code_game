import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = map(int, input().split())

# reads the frid and stores he room types
grid = []
for rooms in range(h):
    row = list(map(int, input().split()))  
    grid.append(row)  

input()

# Define a function to calculate Indy's next position
def next_position(x, y, pos, room_type):
    # Indy cannot move in type 0 room
    if room_type == 0:
        return x, y  
    
    # definition of each room type and each direction that can be done
    # (x,y are the coordinates for each possible room in the grid (see diagram))
    if room_type == 1:
        return x, y + 1
    
    if room_type == 2 or room_type == 6:
        if pos == "LEFT":
            return x + 1, y
        elif pos == "RIGHT":
            return x - 1, y        
    
    if room_type == 3:
        if pos == "TOP":
            return x, y + 1
    
    if room_type == 4:
        if pos == "TOP":
            return x - 1, y
        elif pos == "RIGHT":
            return x, y + 1
    
    if room_type == 5:
        if pos == "TOP":
            return x + 1, y
        elif pos == "LEFT":
            return x, y + 1
    
    if room_type == 7:
        if pos == "TOP" or pos == "RIGHT":
            return x, y + 1
    
    if room_type == 8:
        if pos == "LEFT" or pos == "RIGHT":
            return x, y + 1
    
    if room_type == 9:
        return x, y + 1
    
    if room_type == 10:
        return x - 1, y
    
    if room_type == 11:
        return x + 1, y
    
    if room_type == 12:
        return x, y + 1
    
    if room_type == 13:
        return x, y + 1

# Infinite loop to read Indy's position and provide the next position
while True:
    # (x1, yi current position)
    xi, yi, pos = input().split()
    xi, yi = int(xi), int(yi)
    
    room_type = grid[yi][xi]
    x, y = next_position(xi, yi, pos, room_type)
    
    print(x, y)
