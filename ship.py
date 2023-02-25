from random import randrange

def check_boat(b, start, dirn):
    
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            print(start + i)
    if dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            print(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            print(start - i)  

boats = [5,] # 4, 3, 3, 2, 2]
for b in boats:
    boat_start = randrange(99)
    boat_direction = randrange(1,4)
    print(b,boat_start,boat_direction)
    check_boat(b,boat_start,boat_direction)