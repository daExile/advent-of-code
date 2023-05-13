file = open("18.txt", "r")
import ast
neigh = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

lava = []
s_area = 0
for line in file:
    l = ast.literal_eval(line.strip())

    #neighbours
    a = sum([1 if (l[0]+n[0],l[1]+n[1],l[2]+n[2]) in lava else 0 for n in neigh])
    s_area += (6 - 2 * a)
    lava.append(l)

print("P1:", s_area)

c2 = lava[:]
c2.sort(key = lambda x: x[0])
xmin, xmax = c2[0][0], c2[-1][0]
c2.sort(key = lambda x: x[1])
ymin, ymax = c2[0][1], c2[-1][1]
c2.sort(key = lambda x: x[2])
zmin, zmax = c2[0][2], c2[-1][2]

o = (xmin - 1, ymin - 1, zmin - 1)
free = [o]
t = {0: [o]}
stop = False
n = 0
while not stop:
    t_n = []
    for c in t[n]:
        for a in [(c[0]+n[0],c[1]+n[1],c[2]+n[2]) for n in neigh]:
            if a not in free and a not in lava and a not in t_n:
                if xmin-1<=a[0]<=xmax+1 and ymin-1<=a[1]<=ymax+1 and zmin-1<=a[2]<=zmax+1:
                    t_n.append(a)

    if not t_n: stop = True
    else:
        n += 1
        free += t_n[:]
        t[n] = t_n[:]

iso = []
iso_area = 0
for x in range(xmin+1, xmax):
    for y in range(ymin+1, ymax):
        for z in range(zmin+1, zmax):
            if (x, y, z) not in lava and (x, y ,z) not in free:
                a = sum([1 if (x+n[0],y+n[1],z+n[2]) in iso else 0 for n in neigh])
                iso_area += (6 - 2 * a)
                iso.append((x, y, z))

#print(iso)
#print(iso_area)
print("P2:", s_area - iso_area)
