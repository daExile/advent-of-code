def rotate(drct, act):
    a = 1 if act[0] == "L" else -1
    if act[1] == 90:
        trix = [[0, -a], [a, 0]]
    elif act[1] == 180:
        trix = [[-1, 0], [0, -1]]
    elif act[1] == 270:
        trix = [[0, a], [-a, 0]]
    return [(drct[0] * trix[0][0] + drct[1] * trix[0][1]), (drct[0] * trix[1][0] + drct[1] * trix[1][1])]
    
def move_p1(ship, drct, act):
    if act[0] == "F":
        move = [drct[0] * act[1], drct[1] * act[1]]
    else:
        if act[0] == "N": move = [0, act[1]]
        elif act[0] == "W": move = [-act[1], 0]
        elif act[0] == "S": move = [0, -act[1]]
        elif act[0] == "E": move = [act[1], 0]            
    return [ship[0] + move[0], ship[1] + move[1]]

def move_p2(ship, wpnt, act):
    move = [wpnt[0] * act[1], wpnt[1] * act[1]]            
    return [ship[0] + move[0], ship[1] + move[1]]

def waypoint(wpnt, act):
    if act[0] == "N": return [wpnt[0], wpnt[1] + act[1]]
    elif act[0] == "W": return [wpnt[0] - act[1], wpnt[1]]
    elif act[0] == "S": return [wpnt[0], wpnt[1] - act[1]]
    elif act[0] == "E": return [wpnt[0] + act[1], wpnt[1]]

actions = []
instructions = open("12.txt", "r")
for act in instructions:
    actions.append([act[0], int(act[1:].strip())])
instructions.close()

ship = [0, 0]
drct = [1, 0] # this is east, k?
for act in actions:
    if act[0] in ["R", "L"]: drct = rotate(drct, act)
    else: ship = move_p1(ship, drct, act)

print("Part 1:", abs(ship[0]) + abs(ship[1]))

ship = [0, 0]
drct = [10, 1]
for act in actions:
    if act[0] in ["R", "L"]: drct = rotate(drct, act)
    elif act[0] == "F": ship = move_p2(ship, drct, act)
    else: drct = waypoint(drct, act)

print("Part 2:", abs(ship[0]) + abs(ship[1]))
