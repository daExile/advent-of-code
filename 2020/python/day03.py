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
        
        if forest_map[y][x] == "#":
            treecount += 1
            
        y += x_y[1]
        x += x_y[0]
    treecount_by_route.append({"route": x_y, "trees": treecount})

answer = 1
for route in treecount_by_route:
    answer *= route["trees"]
    
print("Part 1:", treecount_by_route[1]["trees"])
print("Part 2:", answer)
