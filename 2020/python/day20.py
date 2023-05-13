file = open("20.txt", "r")
tiles = {}

#class Tile(object):
#    x, y = 0, 0
#    r, m = 0, 0
#    def __init__(self, tile_id, rotation, flip, coords...
#i guess i'll wait for something simpler    

while True:
    try: n = int(file.readline()[5:9])
    except ValueError: break
    #print(n)
    tile = []
    for i in range(0, 10):
        tile.append(file.readline().strip())
    #print(tile)
    tiles[n] = tile
    e = file.readline() #dumping spacers lol

del(e)
print("Tiles read:", len(tiles))

#let's parse that shit
bin_it = str.maketrans(".# ", "010")
p_tiles = {}

for k in tiles:
    t = []
    
    a = tiles[k][0].translate(bin_it)
    t.append([int(a, 2), int(a[::-1], 2)])

    a = ""
    for i in range(0, 10):
        a += tiles[k][i][9].translate(bin_it)
    t.append([int(a, 2), int(a[::-1], 2)])
    
    a = tiles[k][9].translate(bin_it)
    t.append([int(a, 2), int(a[::-1], 2)])
    
    a = ""
    for i in range(0, 10):
        a += tiles[k][i][0].translate(bin_it)
    t.append([int(a, 2), int(a[::-1], 2)])

    p_tiles[k] = t

def checkmatch(n, data):
    for i in range(0, 4):
        for j in range(0, 2):
            if n == data[i][j]:
                return((i, j))
    return(())

r_mx = [[[0, 2], [1, 1], [0, 2], [3, 3]],
        [[1, 3], [2, 2], [1, 3], [0, 0]],
        [[0, 2], [3, 3], [0, 2], [1, 1]],
        [[1, 3], [0, 0], [1, 3], [2, 2]]]
f_mx = [[[1, 0], [1, 0], [0, 1], [0, 1]],
        [[1, 0], [1, 0], [0, 1], [0, 1]],
        [[0, 1], [0, 1], [1, 0], [1, 0]],
        [[0, 1], [0, 1], [1, 0], [1, 0]]]

def get_xy(key, i):
    if i == 0: xy = (key[0], key[1] + 1)
    if i == 1: xy = (key[0] + 1, key[1])
    if i == 2: xy = (key[0], key[1] - 1)
    if i == 3: xy = (key[0] - 1, key[1])
    return xy

def mapping(n, t_id, data, md):
    #i guess i made it not as bad as old tetris code, still sucks tho
    rot = r_mx[n][md[0]][md[1]]
    flip = f_mx[n][md[0]][md[1]]
    #print(coords, data, rot, flip, md)
    if rot == 0:
        if flip == 0: data_o = [data[0][0], data[1][0], data[2][0], data[3][0]]
        else: data_o = [data[2][0], data[1][1], data[0][0], data[3][1]]
    if rot == 1:
        if flip == 0: data_o = [data[3][1], data[0][0], data[1][1], data[2][0]]
        else: data_o = [data[3][0], data[2][0], data[1][0], data[0][0]]
    if rot == 2:
        if flip == 0: data_o = [data[2][1], data[3][1], data[0][1], data[1][1]]
        else: data_o = [data[0][1], data[3][0], data[2][1], data[1][0]]
    if rot == 3:
        if flip == 0: data_o = [data[1][0], data[2][1], data[3][0], data[0][1]]
        else: data_o = [data[1][1], data[0][1], data[3][1], data[2][1]]
    #print("New data:", data_o)
    a = n + 2 if n < 2 else n - 2
    data_o[a] = 0
    return({'id':t_id, 'edges':data_o, 'rot':rot, 'flip':flip})

tmap = {}

#init
t = p_tiles.popitem()
tmap[(0, 0)] = {'id': t[0], 'edges': [t[1][0][0], t[1][1][0], t[1][2][0], t[1][3][0]], 'rot': 0, 'flip': 0}

p = 0
while p < len(tiles):
    tm_keys = list(tmap.keys())
    for i in range(0, 4):        
        xy = get_xy(tm_keys[p], i)
        if xy not in tmap:
            n = tmap[tm_keys[p]]['edges'][i]
            p_keys = list(p_tiles.keys())
            if p_keys:
                for j in range(0, len(p_tiles)):
                    c = checkmatch(n, p_tiles[p_keys[j]])
                    if c:
                        t = p_tiles.pop(p_keys[j])
                        break
                if c: tmap[xy] = mapping(i, p_keys[j], t, c)
        #else: print("Found tile by side", i, "of", tmap[p][0])
        #print(tmap[-1])
        tmap[tm_keys[p]]['edges'][i] = 0
    p += 1
    #print(p)
#print(len(tmap))
#print(tmap)
#let's find corners lmao
xmin, xmax, ymin, ymax = 0, 0, 0, 0
for tile in list(tmap.keys()):
    if xmin > tile[0]: xmin = tile[0]
    if xmax < tile[0]: xmax = tile[0]
    if ymin > tile[1]: ymin = tile[1]
    if ymax < tile[1]: ymax = tile[1]

print("Part 1 answer:", tmap[(xmin, ymin)]['id'] * tmap[(xmax, ymin)]['id'] * tmap[(xmin, ymax)]['id'] * tmap[(xmax, ymax)]['id'])

#build a tile table
#tt = []
#for y in range(ymax - ymin + 1):
#    tt.append([0] * (xmax - xmin + 1))
#for tile in tmap:
#    x = tile[0][0] - xmin
#    y = tile[0][1] - ymin
#    tt[y][x] = tile[1]
#print(tt)

def rotflip(data, rot, flip):
    n = len(data)

    if flip:
        t_f = data[::-1]
    else: t_f = data[:]

    t_r = []
    if rot == 3:            #figure why 1 and 3 had to be swapped
        for i in range(n - 1, -1, -1):
            s = ""
            for j in range(n):
                s += t_f[j][i]
            t_r.append(s)
    elif rot == 2:
        for line in t_f[::-1]:
            t_r.append(line[::-1])
    elif rot == 1:
        for i in range(n):
            s = ""
            for j in range(n - 1, -1, -1):
                s += t_f[j][i]
            t_r.append(s)
    else: t_r = t_f[:]
    return t_r

def get_tile(data):
    t_og = []
    for i in range(1, 9):
        t_og.append(tiles[data['id']][i][1:9])

    t_r = rotflip(t_og, data['rot'], data['flip'])
    return t_r

xd = xmax - xmin
yd = ymax - ymin
img = []
for y in range(ymax, ymin - 1, -1):
    for x in range(xmin, xmax + 1):
        a = get_tile(tmap[(x, y)])
        for i in range(8):
            if len(img) - 1 < (y - ymax) * -8 + i:
                img.append(a[i].translate(bin_it))
            else: img[(y - ymax) * -8 + i] += a[i].translate(bin_it)

snaek = ["                  # ",
         "#    ##    ##    ###",
         " #  #  #  #  #  #   "]
s = [int("                  # ".translate(bin_it), 2),
     int("#    ##    ##    ###".translate(bin_it), 2),
     int(" #  #  #  #  #  #   ".translate(bin_it), 2)]

snaek_mass = 0
for slice in snaek:
    snaek_mass += slice.count("#")

stuff_total = 0
for line in img:
    stuff_total += line.count("1")

n = len(img)
for f in [0, 1]:
    for r in [0, 1, 2, 3]:
        #print("Rotation", r, "\nFlip", f)
        count = 0
        t = rotflip(img, r, f)
        for i in range(n - 2):
            for j in range(n - 19):
                if int(t[i][j:j + 20], 2) & s[0] == s[0]:
                    if int(t[i + 1][j:j + 20], 2) & s[1] == s[1]:
                        if int(t[i + 2][j:j + 20], 2) & s[2] == s[2]: count += 1
        #print("Sea monsters found:", count, "\n")
        if count: break
    if count: break

print("Part 2 answer:", stuff_total - count * snaek_mass)
#yay no monster overlaps
