forest_map = []
pdata = open("03.txt", "r")
for line in pdata:
    forest_map.append(line.strip())
    
x = 0
y = 0
treecount = 0
xmax = len(forest_map[0])

while y < len(forest_map):
    if x >= xmax: x -= xmax
    huh = "O"
    if forest_map[y][x] == "#":
        huh = "X"
        treecount += 1
    path_map = forest_map[y][0:x] + huh + forest_map[y][x+1:xmax]
    print(forest_map[y], " ", path_map)
    y += 1
    x += 3
print("Tree smash count:", treecount)
