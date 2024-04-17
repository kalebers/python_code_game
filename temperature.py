import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
bestTemp = 6000 # round up temp
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if abs(t) < abs(bestTemp):
        bestTemp = t

    if abs(t) == abs(bestTemp) and t > 0:
        bestTemp = t

if bestTemp == 6000:
    bestTemp = 0

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(bestTemp)
