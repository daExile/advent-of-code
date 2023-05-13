xy = (0, 0)

file = open("01.txt", "r")
path_ = file.readline().strip().split(", ")
#path = ["R8", "R4", "R4", "R8"]
file.close()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for step in path_:
    dirs = dirs[1:] + dirs[:1] if step[0] == "R" else dirs[-1:] + dirs[:-1]
    xy = (xy[0] + dirs[0][0] * int(step[1:]), xy[1] + dirs[0][1] * int(step[1:]))
    #print(step, "->", xy)

print("Final distance from origin:", abs(xy[0]) + abs(xy[1]))

xy = (0, 0)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
log = [xy] #yeah lazy writing starting point in

p_x = None
for step in path_:
    dirs = dirs[1:] + dirs[:1] if step[0] == "R" else dirs[-1:] + dirs[:-1]
    n = int(step[1:])
    #print(step, n)
    p_i = xy
    for i in range(1, n+1):
        p_i = (p_i[0] + dirs[0][0], p_i[1] + dirs[0][1])
        #print(p_i)
        if p_i not in log: log.append(p_i)
        else:
            p_x = p_i
            break
    if p_x: break
    xy = (xy[0] + dirs[0][0] * int(step[1:]), xy[1] + dirs[0][1] * int(step[1:]))
    #print(step, "->", xy)

print("First location to visit twice:", p_i, "which is", abs(p_i[0]) + abs(p_i[1]), "blocks away from origin.")
