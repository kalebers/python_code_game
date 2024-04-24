import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(list(line))

# loop around height(y axis) and width(x axis) to check positions
for y in range(height):
    for x in range(width):
        # starts checking positions
        if lines[y][x] == '.':
            continue
        # if there's no neighbour marks with -1
        right_x = right_y = bottom_x = bottom_y = -1
        try:
            # searches for cells in the X axis, adding to the current pos, until it reaches the one without any neighbours  
            for tx in range(x+1,width):
                if(lines[y][tx]=='0'):
                    right_x = tx
                    right_y = y
                    break
        except Exception:
            pass
        try:
            # searches for cells in the Y axis, adding to the current pos, until it reaches the one without any neighbours  
            for ty in range(y+1, height):
                if(lines[ty][x]=='0'):
                    bottom_x = x
                    bottom_y = ty
                    break
        except Exception:
            pass
        # prints the positions for each set of node coordinates 
        # (x1,y1 coordinates from start node) (right_x, right_y coordinates for the right neighbour), 
        # (bottom_x, bottom_y coordinates for bottom neighbour)
        print("{0} {1} {2} {3} {4} {5}".format(x, y, right_x, right_y, bottom_x, bottom_y))



