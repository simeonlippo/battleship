"""
Minimal requirments: Show board, players shot, 
check hit, miss or sink in loop.

Board needs to be interactive, change "coordinate" to "x" as in "xy graph"
"""

def get_shot_input():
    shot = input("Please enter your guess: ")
    shot = int(shot)
    if shot < 0 or shot > 99:
        print("incorrect input, please guess again: ")

#Board
def show_board(shot_hit, shot_miss, shot_sink):
    coordinate = 0
    print("            Battleship")
    print("   0  1  2  3  4  5  6  7  8  9")

    for x in range(10):
        row = ""
        for y in range(10):
            character = " - "
            if coordinate in shot_miss:
                character = " o "
            elif coordinate in shot_hit:
                character = " x "
            elif coordinate in shot_sink:
                character = " ! "
            row += character
            coordinate += 1
        print(x, row)

shot_hit = [21, 22]
shot_miss = [18, 19, 20]
shot_sink = [23]

#functions
get_shot_input()
show_board(shot_hit, shot_miss, shot_sink)