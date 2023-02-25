from random import randrange

def check_ok(boat, taken):

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 9 == 0 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break

    return boat
def check_boat(b, start, dirn, taken):
    
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)
            boat = check_ok(boat, taken)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            print(start + i)
            boat = check_ok(boat, taken)
    if dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            print(start + i*10)
            boat = check_ok(boat, taken)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            print(start - i)  
            boat = check_ok(boat, taken)
    return boat

def create_boats():
    taken = []
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            print(b,boat_start,boat_direction)
            boat = check_boat(b,boat_start,boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)
    
    return ships,taken

def show_board(taken):
    coordinate = 0
    print("            Battleship")
    print("   0  1  2  3  4  5  6  7  8  9")

    for x in range(10):
        row = ""
        for y in range(10):
            character = " - "
            if coordinate in taken:
                character = " o "
            row += character
            coordinate += 1
        print(x, row)

boats, taken = create_boats()
show_board(taken)
