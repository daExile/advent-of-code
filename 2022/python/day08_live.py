file = open("08.txt", "r")
import re
tmap = []
for line in file:
    s = line.strip()
    tmap.append([int(c) for c in s])
file.close()

tmap_vis = []
a = len(tmap)
b = len(tmap[0])
for i in range(0, a):
    tr = ""
    for j in range(0, b):
        if i == 0 or i == a or j == 0 or j == b: tr += str(tmap[i][j])
        else:
            if not [tmap[i][k] for k in range(0, j) if tmap[i][k] >= tmap[i][j]]: tr += str(tmap[i][j])
            elif not [tmap[k][j] for k in range(0, i) if tmap[k][j] >= tmap[i][j]]: tr += str(tmap[i][j])
            elif not [tmap[i][k] for k in range(b-1, j, -1) if tmap[i][k] >= tmap[i][j]]: tr += str(tmap[i][j])
            elif not [tmap[k][j] for k in range(a-1, i, -1) if tmap[k][j] >= tmap[i][j]]: tr += str(tmap[i][j])
            else: tr += "."
    tmap_vis.append(tr)

count_nv = 0
for row in tmap_vis:
    count_nv += row.count(".")
print("P1 answer:", (99 * 99 - count_nv))

scmax = 0
for i in range(1, a-1):
    for j in range(1, b-1):
        scenic = 1
        for k in range(i-1, -1, -1):
            if tmap[k][j] >= tmap[i][j] or k == 0:
                scenic *= i - k
                break
        for k in range(i+1, a):
            if tmap[k][j] >= tmap[i][j] or k == a-1:
                scenic *= k - i
                break
        for k in range(j-1, -1, -1):
            if tmap[i][k] >= tmap[i][j] or k == 0:
                scenic *= j - k
                break
        for k in range(j+1, b):
            if tmap[i][k] >= tmap[i][j] or k == b-1:
                scenic *= k - j
                break
        if scenic > scmax: scmax = scenic
print("P1 answer:", scmax)
