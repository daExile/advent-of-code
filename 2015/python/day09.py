file = open("09.txt", "r")

routes = {}
for line in file:
    s = line.strip()
    r, n = s.split(" = ")
    c1, c2 = r.split(" to ")

    if c1 in routes:
        routes[c1][c2] = int(n)
    else: routes[c1] = {c2: int(n)}

    if c2 in routes:
        routes[c2][c1] = int(n)
    else: routes[c2] = {c1: int(n)}

file.close()

locs = list(routes.keys())

def get_min_route(locs, dep = ""):
    global routes

    dmin = None
    #print(locs)
    for l in locs:
        locs_new = locs[:]
        locs_new.remove(l)
        d = routes[dep][l] if dep else 0
        if locs_new: d += get_min_route(locs_new, l)
        if dmin:
            if d < dmin: dmin = d
        else: dmin = d
    return dmin

def get_max_route(locs, dep = ""):
    global routes

    dmax = None
    #print(locs)
    for l in locs:
        locs_new = locs[:]
        locs_new.remove(l)
        d = routes[dep][l] if dep else 0
        if locs_new: d += get_max_route(locs_new, l)
        if dmax:
            if d > dmax: dmax = d
        else: dmax = d
    return dmax

print("Part 1 answer:", get_min_route(locs))
print("Part 2 answer:", get_max_route(locs))
