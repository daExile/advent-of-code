file = open("15.txt", "r")
import re

sensors = []
beacons = []
for line in file:
    x, y, xb, yb = [int(x) for x in re.findall(r"([-\d]+)", line)]
    dx = abs(x-xb)
    dy = abs(y-yb)
    md = dx+dy
    sensors.append((x, y, md))
    beacons.append((xb, yb))

beacons = list(set(beacons))
bcount2m = 0
for b in beacons:
    if b[1] == 2000000: bcount2m += 1

y2m = []
for s in sensors:
    dy2m = abs(s[1] - 2000000)
    if s[2] >= dy2m:
        dx2m = s[2] - dy2m
        y2m.append((s[0] - dx2m, s[0] + dx2m))

y2m.sort(key = lambda x: x[0])
sensors.sort(key = lambda x: x[0])

imps = None
for i, r in enumerate(y2m):
    if not imps:
        imps = r
    else:
        if imps[1] < r[0]: print("Found a gap to code around, abort mission :D")
        else:
            if imps[1] >= r[1]: continue
            else: imps = (imps[0], r[1])
    
#print(imps)
#print(bcount2m)
print("P1:", (imps[1] - imps[0] + 1) - bcount2m)

for y in range(4000001):
    x = 0
    for s in sensors:
        #print(s)
        dy = abs(s[1] - y)
        if s[2] >= dy:
            dx = s[2] - dy
            #print("dx dy", dx, dy)
            if x >= s[0] - dx and x <= s[0] + dx:
                x = s[0] + dx + 1
                #print("new x", x)
    if x <= 4000000:
        print("x = {}, y = {}".format(x, y))
        print("P2:", 4000000 * x + y)
        break
