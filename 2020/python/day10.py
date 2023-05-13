adapters = [0,]
adlist = open("10.txt", "r")
for ad in adlist:
    adapters.append(int(ad))
adlist.close()

adapters.sort()
adapters.append(adapters[-1]+3)
diffs = [0, 0, 0, 0, 0, 0]

for n in range(0, len(adapters)-1):
    diffs[(adapters[n+1] - adapters[n])] += 1
    print(adapters[n+1], "-", adapters[n], "=", adapters[n+1]-adapters[n], "(this diff count:", diffs[adapters[n+1]-adapters[n]], ")")

# print(adapters)
print(diffs[1:])
print("Answer:", diffs[1] * diffs[3])
