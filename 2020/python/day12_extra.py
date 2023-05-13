ship = [0, 0]
wpnt = [10, 1]
actions = []

def rotate(wpnt, act):
    a = 1 if act[0] == "L" else -1
    if act[1] == 90:
        trix = [[0, -a], [a, 0]]
    elif act[1] == 180:
        trix = [[-1, 0], [0, -1]]
    elif act[1] == 270:
        trix = [[0, a], [-a, 0]]
    return [(wpnt[0] * trix[0][0] + wpnt[1] * trix[0][1]), (wpnt[0] * trix[1][0] + wpnt[1] * trix[1][1])]
    
def move(ship, wpnt, act):
    move = [wpnt[0] * act[1], wpnt[1] * act[1]]            
    return [ship[0] + move[0], ship[1] + move[1]]

def waypoint(wpnt, act):
    if act[0] == "N": return [wpnt[0], wpnt[1] + act[1]]
    elif act[0] == "W": return [wpnt[0] - act[1], wpnt[1]]
    elif act[0] == "S": return [wpnt[0], wpnt[1] - act[1]]
    elif act[0] == "E": return [wpnt[0] + act[1], wpnt[1]]

instructions = open("12.txt", "r")
for act in instructions:
    actions.append([act[0], int(act[1:].strip())])
instructions.close()

print("Ship is at:", ship, ", waypoint", wpnt)
for act in actions:
    if act[0] in ["R", "L"]: wpnt = rotate(wpnt, act)
    elif act[0] == "F": ship = move(ship, wpnt, act)
    else: wpnt = waypoint(wpnt, act)
    print("Action:", act, ", ship is at:", ship, ", waypoint", wpnt)

print("Endpoint:", ship, "\nManhattan distance:", abs(ship[0]) + abs(ship[1]))
