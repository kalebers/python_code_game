import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = []
for i in range(h):
    rows.append(input())

ascII_art_array_search = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ?".split()

for row in rows:
    rowtext = ""
    for x in t:
        try: 
            index = ascII_art_array_search.index(x.upper())
        except ValueError:
            index = 26
        start = ((index) * l) 
        end = start + l
        rowtext = rowtext + row[start:end]

    print(rowtext)
