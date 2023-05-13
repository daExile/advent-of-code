file = open("09.txt", "r")

m = []
for line in file:
    s = line.strip().split()
    m.append((s[0], int(s[1])))
file.close()

tlog = []
h = (0, 0)
t = (0, 0)
tlog.append(t)

for item in m:
    if item[0] == "U": sh = (0, 1)
    elif item[0] == "D": sh = (0, -1)
    elif item[0] == "L": sh = (-1, 0)
    elif item[0] == "R": sh = (1, 0)

    for i in range(item[1]):
        h = (h[0] + sh[0], h[1] + sh[1])
        dx = h[0] - t[0]
        dy = h[1] - t[1]
        if abs(dx) > 1:
            if abs(dy) == 0: t = (t[0] + int(dx/abs(dx)), t[1])
            else: t = (t[0] + int(dx/abs(dx)), t[1] + int(dy/abs(dy)))
        elif abs(dy) > 1:
            if abs(dx) == 0: t = (t[0], t[1] + int(dy/abs(dy)))
            else: t = (t[0] + int(dx/abs(dx)), t[1] + int(dy/abs(dy)))
        #print(t)
        if t not in tlog: tlog.append(t)
print("P1 answer:", len(tlog))

#bah clumsy init for part 2
tlog = [[(0, 0)] for _ in range(10)]
ks = [(0, 0) for _ in range(10)]
for item in m:
    if item[0] == "U": sh = (0, 1)
    elif item[0] == "D": sh = (0, -1)
    elif item[0] == "L": sh = (-1, 0)
    elif item[0] == "R": sh = (1, 0)

    for i in range(item[1]):
        ks[0] = (ks[0][0] + sh[0], ks[0][1] + sh[1])
        for j in range(1, 10):
            dx = ks[j-1][0] - ks[j][0]
            dy = ks[j-1][1] - ks[j][1]
            if abs(dx) > 1:
                if abs(dy) == 0: ks[j] = (ks[j][0] + int(dx/abs(dx)), ks[j][1])
                else: ks[j] = (ks[j][0] + int(dx/abs(dx)), ks[j][1] + int(dy/abs(dy)))
            elif abs(dy) > 1:
                if abs(dx) == 0: ks[j] = (ks[j][0], ks[j][1] + int(dy/abs(dy)))
                else: ks[j] = (ks[j][0] + int(dx/abs(dx)), ks[j][1] + int(dy/abs(dy)))
            #print(t)
            if ks[j] not in tlog[j]: tlog[j].append(ks[j])
print("P2 answer:", len(tlog[9]))
