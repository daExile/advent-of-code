file = open("24.txt", "r")

bzs = {"<": [],
       "^": [],
       ">": [],
       "v": []}
m0 = []
for y, line in enumerate(file):
    row = []
    for x, c in enumerate(line.strip()):
        if c == "#" or c == ".": row.append(c)
        else:
            row.append(".")
            bzs[c].append((y, x))
    m0.append(row)

ymax = len(m0) - 2
xmax = len(m0[0]) - 2

def move_bzs(bzs):
    bzs_new = {"<": [], "^": [], ">": [], "v": []}
    for b in bzs["<"]:
        if b[1] > 1: bzs_new["<"].append((b[0], b[1]-1))
        else: bzs_new["<"].append((b[0], xmax))
    for b in bzs["^"]:
        if b[0] > 1: bzs_new["^"].append((b[0]-1, b[1]))
        else: bzs_new["^"].append((ymax, b[1]))
    for b in bzs[">"]:
        if b[1] < xmax: bzs_new[">"].append((b[0], b[1]+1))
        else: bzs_new[">"].append((b[0], 1))
    for b in bzs["v"]:
        if b[0] < ymax: bzs_new["v"].append((b[0]+1, b[1]))
        else: bzs_new["v"].append((1, b[1]))
    return bzs_new

def get_map(m0, bzs):
    m = []
    b_all = set([] + [j for i in list(bzs.keys()) for j in bzs[i]])
    for y, row in enumerate(m0):
        row_n = []
        for x, c in enumerate(row):
            if (y, x) in b_all: row_n.append("#")
            else: row_n.append(m0[y][x])
        #print("".join(row_n))
        m.append(row_n)
    return m

def dashing_thru_the_snow(start, target, t0):
    global bzs
    t = t0
    mov = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
    e = [start]
    while True:
        t += 1
        #print("Round", t)
        bzs = move_bzs(bzs)
        m_cur = get_map(m0, bzs)
        #print(m_cur)
        e_new = []
        for i in e:
            for m in mov:
                y = i[0] + m[0]
                x = i[1] + m[1]
                if 0 <= y <= ymax + 1 and 0 <= x <= xmax + 1:
                    if m_cur[y][x] == "." and (y, x) not in e_new: e_new.append((y, x))
        e = e_new[:]
        #print(e)
        if target in e: return t

target = (ymax + 1, xmax)
#print(target)
t = dashing_thru_the_snow((0, 1), target, 0)
print("P1:", t)
t = dashing_thru_the_snow(target, (0, 1), t)
t = dashing_thru_the_snow((0, 1), target, t)
print("P2:", t)
