file = open("17.txt", "r")
inpt = [line.strip() for line in file]
file.close()

cmap = []
t = []
y = 0
for line in inpt:
    x = 0
    for s in line:
        if s == "#": t.append((x, y, 0))
        x += 1
    y += 1
cmap.append(t)

for turn in range(1, 7):
    cmap.append([])
    temp = []
    
    # building array of cubes to check
    for c in cmap[turn - 1]:
        for x in range(c[0] - 1, c[0] + 2):
            for y in range(c[1] - 1, c[1] + 2):
                for z in range(c[2] - 1, c[2] + 2):
                    if (x, y, z) not in temp: temp.append((x, y, z))

    # now let's check them
    for c in temp:
        if c in cmap[turn - 1]:
            neigh = -1
            for x in range(c[0] - 1, c[0] + 2):
                for y in range(c[1] - 1, c[1] + 2):
                    for z in range(c[2] - 1, c[2] + 2):
                        if (x, y, z) in cmap[turn - 1]: neigh += 1
            if neigh in [2, 3]: cmap[turn].append(c)
        else:
            neigh = 0
            for x in range(c[0] - 1, c[0] + 2):
                for y in range(c[1] - 1, c[1] + 2):
                    for z in range(c[2] - 1, c[2] + 2):
                        if (x, y, z) in cmap[turn - 1]: neigh += 1
            if neigh == 3: cmap[turn].append(c)
            
print("Part 1:", len(cmap[6]))

cmap = []
t = []
y = 0
for line in inpt:
    x = 0
    for s in line:
        if s == "#": t.append((x, y, 0, 0))

        x += 1
    y += 1
file.close()
cmap.append(t)

for turn in range(1, 7):
    cmap.append([])
    temp = []
    
    # building array of cubes to check
    for c in cmap[turn - 1]:
        for x in range(c[0] - 1, c[0] + 2):
            for y in range(c[1] - 1, c[1] + 2):
                for z in range(c[2] - 1, c[2] + 2):
                    for w in range(c[3] - 1, c[3] + 2):
                        temp.append((x, y, z, w))
    temp = list(set(temp))

    # now let's check them
    for c in temp:
        if c in cmap[turn - 1]:
            neigh = -1
            for x in range(c[0] - 1, c[0] + 2):
                for y in range(c[1] - 1, c[1] + 2):
                    for z in range(c[2] - 1, c[2] + 2):
                        for w in range(c[3] - 1, c[3] + 2):
                            if (x, y, z, w) in cmap[turn - 1]: neigh += 1
            if neigh in [2, 3]: cmap[turn].append(c)
        else:
            neigh = 0
            for x in range(c[0] - 1, c[0] + 2):
                for y in range(c[1] - 1, c[1] + 2):
                    for z in range(c[2] - 1, c[2] + 2):
                        for w in range(c[3] - 1, c[3] + 2):
                            if (x, y, z, w) in cmap[turn - 1]: neigh += 1
            if neigh == 3: cmap[turn].append(c)
            
print("Part 2:", len(cmap[6]))
