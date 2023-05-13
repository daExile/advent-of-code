file = open("03.txt", "r")

triangles = []
t_v = []
for line in file:
    t = [int(x) for x in line.strip().split()]
    triangles.append(t[:])
    t.sort()
    if t[2] < t[0] + t[1]: t_v.append(t)

print("Part 1")
print("Total triangles:", len(triangles))
print("Valid triangles:", len(t_v), "\n")

triangles_readcol = []
t_v_col = []
for i in range(0, len(triangles), 3):
    for j in range(3):
        t = [triangles[i][j], triangles[i+1][j], triangles[i+2][j]]
        triangles_readcol.append(t)
        t.sort()
        if t[2] < t[0] + t[1]: t_v_col.append(t)

print("Part 2")
print("Total triangles:", len(triangles_readcol))
print("Valid triangles:", len(t_v_col))
