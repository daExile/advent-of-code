file = open("22.txt", "r")
import re

mappo = [[" "]]
for line in file:
    s = line.strip("\n")
    if s: mappo.append([" "] + list(s) + [" "])
    else: break
mappo.append([" "])
#let's pad it to "square"
w = max([len(row) for row in mappo])
for row in mappo:
    row += [" "] * (w - len(row))

logmappo = []
for row in mappo:
    logmappo.append(row[:])

path = []
for line in file:
    path = re.findall(r"(\d+|[RL])", line.strip())
file.close()

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
arrows = [">", "^", "<", "v"]
#for row in mappo:
#    print(row)
#print(path)

y0 = 1
x0 = mappo[1].index(".")
#print(y0, x0)
def wrap(y0, x0, dy, dx):    
    if dx == 0:
        y = len(mappo)-1 if dy == -1 else 0
        x = x0
    else:
        x = len(mappo[y0])-1 if dx == -1 else 0
        y = y0
    while mappo[y][x] == " ":
        y += dy
        x += dx
    #print("wraps from", (y0, x0), "to", (y, x))
    return (y, x)

def is_edge(y, x):
    yo, xo = y, x
    if y < 0: y += len(mappo)
    elif y == len(mappo): y = 0
    elif x < 0: x += len(mappo[y])
    elif x == len(mappo[y]): x = 0
    if xo != x or yo != y: print("wraps from", (yo, xo), "to", (y, x))
    return(y, x)

for step in path:
    #print("step:", step)
    if step == "R":
        dirs = dirs[-1:] + dirs[:-1]
        arrows = arrows[-1:] + arrows[:-1]
        #logmappo[y0][x0] = arrows[0]
    elif step == "L":
        dirs = dirs[1:] + dirs[:1]
        arrows = arrows[1:] + arrows[:1]
        #logmappo[y0][x0] = arrows[0]
    else:
        s = int(step)
        dy = dirs[0][0]
        dx = dirs[0][1]
        for j in range(s):
            y, x = y0 + dy, x0 + dx
            if mappo[y][x] == " ": y, x = wrap(y, x, dy, dx)
            if mappo[y][x] == ".":
                y0 = y
                x0 = x
                #logmappo[y0][x0] = arrows[0]
            else:
                #print("hits # at", (y, x))
                break
            
    #print(step, y0 + 1, x0 + 1)
#print(y0 + 1, x0 + 1, dirs.index((0, 1)))
print(y0, x0, arrows[0])
print("P1:", 1000 * (y0) + 4 * (x0) + dirs.index((0, 1)))

#hardcode part2, no general solution today lol
def cubewrap(y0, x0, dy, dx):
    #now this is hardcoded part
    if dx == 0:
        if dy == 1:
            if x0 in range(1, 51):
                x = x0 + 100
                y = 0
            elif x0 in range(51, 101):
                x = 51
                y = x0 + 100
                dy = 0
                dx = -1
            else:
                x = 101
                y = x0 - 50
                dy = 0
                dx = -1
        else:
            if x0 in range(1, 51):
                x = 50
                y = x0 + 50
                dx = 1
                dy = 0
            elif x0 in range(51, 101):
                x = 0
                y = x0 + 100
                dy = 0
                dx = 1
            else:
                x = x0 - 100
                y = 201
    else:
        if dx == 1:
            if y0 in range(1, 51):
                x = 101
                y = 151 - y0
                dx = -1
            elif y0 in range(51, 101):
                x = y0 + 50
                y = 51
                dy = -1
                dx = 0
            elif y0 in range(101, 151):
                x = 151
                y = 151 - y0
                dx = -1
            else:
                x = y0 - 100
                y = 151
                dy = -1
                dx = 0
        else:
            if y0 in range(1, 51):
                x = 0
                y = 151 - y0
                dx = 1
            elif y0 in range(51, 101):
                x = y0 - 50
                y = 50
                dx = 0
                dy = 1
            elif y0 in range(101, 151):
                x = 50
                y = 151 - y0
                dx = 1
            else:
                x = y0 - 100
                y = 0
                dy = 1
                dx = 0

    while mappo[y][x] == " ":
        y += dy
        x += dx
    print("wraps from", (y0, x0), "to", (y, x))
    return (y, x, dy, dx)

y0 = 1
x0 = mappo[1].index(".")
d = 0

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arrows = [">", "v", "<", "^"]
for k in range(len(path)):
    step = path[k]
    #print("step:", step)
    if step == "R":
        d += 1
        if d == 4: d = 0
        logmappo[y0][x0] = arrows[d]
    elif step == "L":
        d -= 1
        if d == -1: d = 3
        logmappo[y0][x0] = arrows[d]
    else:
        s = int(step)
        dy = dirs[d][0]
        dx = dirs[d][1]
        for j in range(s):
            y, x = y0 + dy, x0 + dx
            if mappo[y][x] == " ":
                print("wraps at step", k)
                y, x, dy, dx = cubewrap(y, x, dy, dx)
                
            if mappo[y][x] == ".":
                y0 = y
                x0 = x
                d = dirs.index((dy, dx))
                if k > len(path)-10: logmappo[y0][x0] = arrows[d]
            else:
                #print("hits # at", (y, x))
                break

print(y0, x0, arrows[0])
print("P2:", 1000 * (y0) + 4 * (x0) + d)
file = open("22_chart.txt", "w")
for row in logmappo:
    file.write("".join(row) + "\n")
file.close()
