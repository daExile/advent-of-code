file = open("17.txt", "r")

target_cap = 150
containers = []
for line in file:
    containers.append(int(line.strip()))
file.close()

capacities = []
c_n = []
for i in range(2 ** 20):
    n = "{:020b}".format(i)
    cap = cnum = 0
    for j in range(20):
        cap += int(n[j]) * containers[j]
        cnum += int(n[j])
    if cap == target_cap:
        if cnum not in c_n: c_n.append(cnum)
        capacities.append((cnum, n))

#print(capacities)
print("Part 1 answer:", len(capacities))

min_n = min(capacities, key = lambda c: c[0])[0]
#why lambda a: a[0] didn't work for min(capacities)
#now it works for the sake of it

capacities_min = []
for i in capacities:
    if i[0] == min(c_n): capacities_min.append(i)

#print(capacities_min)
print("Part 2 answer:", len(capacities_min))
