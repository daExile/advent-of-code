forest_map = []
treecount_by_route = []
x_y_diffs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
pdata = open("03.txt", "r")
for line in pdata:
    forest_map.append(line.strip())

for x_y in x_y_diffs:
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
        if x_y[1] > 1:
            for map_y in range(y+1, y+x_y[1]):
                if map_y < len(forest_map): print(forest_map[map_y], " ", forest_map[map_y])
        y += x_y[1]
        x += x_y[0]
    treecount_by_route.append({"route": x_y, "trees": treecount})
    print("Right", x_y[0], "Down", x_y[1], "- Tree smash count:", treecount)

answer = 1
for route in treecount_by_route:
    answer *= route["trees"]
print("Answer:", answer)
