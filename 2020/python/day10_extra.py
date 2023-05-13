adapters = [[0, 0],]
adlist = open("10.txt", "r")
for ad in adlist:
    adapters.append([int(ad), 0])
adlist.close()

adapters.sort()
adapters.append([adapters[-1][0]+3, 1])

for a in range(len(adapters)-1, -1, -1):
    for b in range(a+1, len(adapters)):
        if adapters[b][0] - adapters[a][0] > 3: break
        else:
            adapters[a][1] += adapters[b][1]

print(adapters)
print("Distinct ways:", adapters[0][1])
