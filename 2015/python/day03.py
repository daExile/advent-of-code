file = open("03.txt", "r")

s = file.read()
file.close()

visited = {(0, 0):1} #init: origin point house with a gift
x_s = y_s = x_r = y_r = 0
turn = True
for char in s:
    if turn:
        if char == "^": y_s += 1
        elif char == "v": y_s -= 1
        elif char == ">": x_s += 1
        elif char == "<": x_s -= 1
        if (x_s, y_s) in visited: visited[(x_s, y_s)] += 1
        else: visited[(x_s, y_s)] = 1
    else:
        if char == "^": y_r += 1
        elif char == "v": y_r -= 1
        elif char == ">": x_r += 1
        elif char == "<": x_r -= 1
        if (x_r, y_r) in visited: visited[(x_r, y_r)] += 1
        else: visited[(x_r, y_r)] = 1
    turn = not turn

print("Houses visited:", len(visited))
