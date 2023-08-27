adapters = [[0, 0]]
adlist = open("10.txt", "r")
for ad in adlist:
    adapters.append([int(ad), 0])
adlist.close()

adapters.sort(key = lambda item: item[0])
adapters.append([adapters[-1][0]+3, 1])
diffs = [0, 0, 0, 0, 0, 0]

for n in range(0, len(adapters)-1): diffs[(adapters[n+1][0] - adapters[n][0])] += 1

print("Part 1:", diffs[1] * diffs[3])

for a in range(len(adapters)-1, -1, -1):
    for b in range(a+1, len(adapters)):
        if adapters[b][0] - adapters[a][0] > 3: break
        else:
            adapters[a][1] += adapters[b][1]

print("Part 2:", adapters[0][1])
