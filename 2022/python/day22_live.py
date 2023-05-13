file = open("22.txt", "r")
import re

mappo = []
for line in file:
    s = line.strip("\n")
    if s: mappo.append(list(s))
    else: break

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

y0 = 0
x0 = mappo[0].index(".")
#print(y0, x0)
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
        logmappo[y0][x0] = arrows[0]
    elif step == "L":
        dirs = dirs[1:] + dirs[:1]
        arrows = arrows[1:] + arrows[:1]
        logmappo[y0][x0] = arrows[0]
    else:
        s = int(step)
        dy = dirs[0][0]
        dx = dirs[0][1]
        for j in range(s):
            y, x = y0 + dy, x0 + dx
            y, x = is_edge(y, x)
            #print((y, x))
            while mappo[y][x] == " ":                
                y, x = y + dy, x + dx
                y, x = is_edge(y, x)
                #print("finding nonspace:", (y, x))
            #print("after bordercheck", (y, x))
            if mappo[y][x] == ".":
                y0 = y
                x0 = x
                logmappo[y0][x0] = arrows[0]
            else:
                #print("hits # at", (y, x))
                break
            
    #print(step, y0 + 1, x0 + 1)
#print(y0 + 1, x0 + 1, dirs.index((0, 1)))
print(y0+1, x0+1, arrows[0])
print("P1:", 1000 * (y0 + 1) + 4 * (x0 + 1) + dirs.index((0, 1)))
file = open("22_chart.txt", "w")
for row in logmappo:
    file.write("".join(row) + "\n")
file.close()
