file = open("24.txt")
tiles = []
days = 100

for line in file:
    i = 0
    c = (0, 0)
    ref = line.strip()
    while i < len(ref):
        if ref[i] == "w":
            c = (c[0] - 1, c[1] + 1)
            i += 1
        elif ref[i] == "e":
            c = (c[0] + 1, c[1] - 1)
            i += 1
        elif ref[i] == "n":
            if ref[i+1] == "e":
                c = (c[0] + 1, c[1])
            else: c = (c[0], c[1] + 1)
            i += 2
        else:
            if ref[i+1] == "e":
                c = (c[0], c[1] - 1)
            else: c = (c[0] - 1, c[1])
            i += 2
    #print(c)
    if c in tiles: tiles.remove(c)
    else: tiles.append(c)

print("Part 1 answer:", len(tiles))

#let's try conway cubes way
#kinda slow but works, no idea how to optimise this for now
for d in range(days):
    t_c = []
    for t in tiles:
        t_c.extend((t,
                    (t[0], t[1] + 1),
                    (t[0] + 1, t[1]),
                    (t[0], t[1] - 1),
                    (t[0] - 1, t[1]),
                    (t[0] - 1, t[1] + 1),
                    (t[0] + 1, t[1] - 1)))
    t_c = list(set(t_c[:]))

    t_n = []
    for t in t_c:
        neigh = 0
        if t in tiles:
            for i in ((t[0], t[1] + 1), (t[0] + 1, t[1]),
                      (t[0], t[1] - 1), (t[0] - 1, t[1]),
                      (t[0] - 1, t[1] + 1), (t[0] + 1, t[1] - 1)):
                if i in tiles: neigh += 1
                if neigh > 2: break
            if neigh == 1 or neigh == 2: t_n.append(t)
        else:
            for i in ((t[0], t[1] + 1), (t[0] + 1, t[1]),
                      (t[0], t[1] - 1), (t[0] - 1, t[1]),
                      (t[0] - 1, t[1] + 1), (t[0] + 1, t[1] - 1)):
                if i in tiles: neigh += 1
                if neigh > 2: break
            if neigh == 2: t_n.append(t)
    tiles = t_n[:]
    print("Day", d + 1, "-", len(tiles), "black tiles")
print("Part 2 answer:", len(tiles))
