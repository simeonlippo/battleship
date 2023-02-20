"""
Minimal requirments: Show board, players shot, 
check hit, miss or sink in loop.

Board needs to be interactive, change "coordinate" to "x" as in "xy graph"
"""

#Board
shot_hit = 21
coordinate = 0
print("            Battleship")
print("   0  1  2  3  4  5  6  7  8  9")

for x in range(10):
    row = ""
    for y in range(10):
        character = " - "
        if coordinate == 21:
            character = " x "
        row += character
        coordinate += 1
    print(x, row)
