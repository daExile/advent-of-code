import re
file = open('22.txt', 'r')

nodes = {}
for line in file:
    s = line.strip()
    m = re.findall(r'.*x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*', s)
    if m:
        x, y, size, used, avail = [int(x[i]) for i in range(5) for x in m]
        nodes[(x, y)] = {"s": size, "u": used, "a": avail}
        if used == 0: n0 = (x, y)
file.close()
#print(n0)

vpairs = []
for i in nodes:
    for j in nodes:
        if i == j: continue
        else:
            if nodes[i]["u"] <= nodes[j]["a"] and nodes[i]["u"] > 0:
                vpairs.append((i, j))

print("P1:", len(vpairs))

def is_near(xy1, xy2):
    a = abs(xy1[0] - xy2[0])
    b = abs(xy1[1] - xy2[1])
    if (a, b) == (0, 1) or (a, b) == (1, 0): return True
    return False

def get_path(m, start, dest, xymax):
    t = {}
    t[0] = start
    curr = [start]
    log = [start]
    n = 1
    while dest not in log:
        nstep = []
        for i in curr:
            for j in [(i[0]+1, i[1]), (i[0], i[1]+1), (i[0]-1, i[1]), (i[0], i[1]-1)]:
                #print(j)
                if j[0] < 0 or j[1] < 0 or j[0] > xymax[0] or j[1] > xymax[1]:
                    continue
                if j not in nstep and j not in log:
                    #print(j[0], j[1], len(m), len(m[0]))
                    if m[j[1]][j[0]] == 0:
                        log.append(j)
                        nstep.append(j)
                        if n in t: t[n].append(j)
                        else: t[n] = [j]
        n += 1
        curr = nstep[:]
    
    route = [dest]
    for i in range(n-1, 0, -1):
        for node in t[i]:
            if is_near(route[0], node):
                route.insert(0, node)
                break
    return route
        

xmax = max(nodes.keys(), key = lambda x: x[0])[0]
ymax = max(nodes.keys(), key = lambda x: x[1])[1]
print(xmax, ymax)
nmap = []
for j in range(ymax + 1):
    row = []
    for i in range(xmax + 1):
        a = 0 if nodes[(i, j)]["s"] < 100 else -1
        row.append(a)
    nmap.append(row[:])
#print(nmap)
target = (0, 0)
zero_node = n0
data_cur = (xmax, 0)

moves = 0
data_path = get_path(nmap, data_cur, target, (xmax, ymax))
while data_cur != target:
    nmap[data_cur[1]][data_cur[0]] = 1
    zero_path = get_path(nmap, zero_node, data_path[0], (xmax, ymax))
    print(zero_path)
    moves += len(zero_path)

    #sort of move data one step
    nmap[data_cur[1]][data_cur[0]] = 0
    zero_node = data_cur
    data_cur = data_path.pop(0)
    moves += 1
print("P2:", moves)
