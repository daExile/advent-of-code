file = open("23.txt")
init = [int(c) for c in file.readline()]

cups = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(init)):
    cups[init[i]] = init[(i+1) % len(init)]
curr = init[0]

for m in range(100):
    dest = curr - 1 if curr > 1 else 9

    p1 = cups[curr]
    p2 = cups[p1]
    p3 = cups[p2]
    pick = (p1, p2, p3)

    while dest in pick:
        dest = dest - 1 if dest > 1 else 9
            
    try: cups[curr] = cups[p3]
    except IndexError: print(curr, p3)
    cups[p3] = cups[dest]
    cups[dest] = p1
        
    curr = cups[curr]

curr = 1
p1 = ""
for i in range(8):
    p1 += str(cups[curr])
    curr = cups[curr]

print("Part 1:", p1)

cups = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
init.append(10)
for i in range(len(init)-1):
    cups[init[i]] = init[i+1]
for i in range(11, 1000001):
    cups.append(i)
    
cups.append(init[0])
curr = init[0]

for m in range(100):
    #print("{}%".format(m))
    for i in range(100000):
        dest = curr - 1 if curr > 1 else 1000000

        p1 = cups[curr]
        p2 = cups[p1]
        p3 = cups[p2]
        pick = (p1, p2, p3)

        while dest in pick:
            dest = dest - 1 if dest > 1 else 1000000
            
        try: cups[curr] = cups[p3]
        except IndexError: print(curr, p3)
        cups[p3] = cups[dest]
        cups[dest] = p1
        
        curr = cups[curr]

a = cups[1]
b = cups[a]
print("Part 2:", a * b)
