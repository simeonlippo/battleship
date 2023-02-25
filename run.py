def get_shot_input(guesses):
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect input, please try again: ")
            elif shot in guesses:
                print("you've alredy shot there! Try again: ")
            else:
                ok = "y"
                break
        except:
            print("incorrect entry, please enter again: ")

    return shot

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

def check_shot(shot, boat1, boat2, shot_hit, shot_miss, shot_sink):
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            shot_hit.append(shot)
        else:
            shot_sink.append(shot)
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            shot_hit.append(shot)
        else:
            shot_sink.append(shot)
    else:
        shot_miss.append(shot)

    return boat1, boat2, shot_hit, shot_miss, shot_sink

boat1 = [1, 2, 3]
boat2 = [34, 35, 36]

shot_hit = []
shot_miss = []
shot_sink = []
print(boat_start)

#functions
for i in range(100):
    guesses = shot_hit + shot_miss + shot_sink
    shot = get_shot_input(guesses)
    boat1, boat2, shot_hit, shot_miss, shot_sink = check_shot(shot, boat1, boat2, shot_hit, shot_miss, shot_sink)
    show_board(shot_hit, shot_miss, shot_sink)

    if len(boat1) < 1 and len(boat2) < 1:
        print("You've won the game!")
        break

print("Finished")