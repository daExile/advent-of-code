import itertools
file = open("24.txt", "r")
mappo = []

for line in file:
    s = line.strip()
    mappo.append(list(s))

pois = {}
for y, row in enumerate(mappo):
    for x, tile in enumerate(row):
        if tile not in [".", "#"]:
            pois[int(tile)] = (y, x)

def get_neighbours(yx):
    y, x = yx
    return [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]

def find_path_lengths(m, start, targets):
    steps = {0: [start]}
    log = [start]
    path_lengths = {}
    n = 0
    
    while targets:
        t = []
        for i in steps[n]:
            t += get_neighbours(i)
        t = list(set(t))

        n += 1
        steps[n] = [i for i in t if m[i[0]][i[1]] != "#" and i not in log]
        log += steps[n][:]

        f = []
        for i in targets:
            if targets[i] in steps[n]:
                path_lengths[i] = n
                f.append(i)
        for key in f: targets.pop(key)
    return path_lengths

pw_dists = {}
for poi in list(pois.keys()):
    pw_dists[poi] = {}

p_k = list(pois.keys())
for k in range(len(pois)-1):
    start = pois[p_k[k]]
    targets = {i:pois[i] for i in p_k[k+1:]}
    ds = find_path_lengths(mappo, start, targets)
    for item in ds:
        pw_dists[p_k[k]][item] = ds[item]
        pw_dists[item][p_k[k]] = ds[item]

p_k.pop(p_k.index(0))

min_route = None
for a in itertools.permutations(p_k):
    r_len = 0
    route = [0] + list(a)
    for i in range(len(a)):
        r_len += pw_dists[route[i]][route[i+1]]
    if not min_route or min_route > r_len: min_route = r_len
    #print(route, r_len)

print("P1:", min_route)

min_route = None
for a in itertools.permutations(p_k):
    r_len = 0
    route = [0] + list(a) + [0] #super-lazy
    for i in range(len(a)+1):
        r_len += pw_dists[route[i]][route[i+1]]
    if not min_route or min_route > r_len: min_route = r_len
    #print(route, r_len)

print("P2:", min_route)
