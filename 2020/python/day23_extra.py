#shame on me for looking up some ideas on how to make it fast
#would prolly arrive to something similar
#or just let slow one finish. A-a-a-anyway

rounds = 100000
#init = [3, 8, 9, 1, 2, 5, 4, 6, 7] #test example
init = [int(c) for c in input("Puzzle input: ")]
cups = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
init.append(10)
for i in range(len(init)-1):
    cups[init[i]] = init[i+1]
for i in range(11, 1000001):
    cups.append(i)
#print(len(cups))
cups.append(init[0])
curr = init[0]

#well, gotta do the list thing after all
for m in range(100):
    print("{}%".format(m))
    for i in range(rounds):
        dest = curr - 1 if curr > 1 else 1000000
        #print("dest =", dest)

        p1 = cups[curr]
        p2 = cups[p1]
        p3 = cups[p2]
        pick = (p1, p2, p3)
        #print("pick =", pick)
        while dest in pick:
            dest = dest - 1 if dest > 1 else 1000000
        #print("dest =", dest)
            
        try: cups[curr] = cups[p3]
        except IndexError: print(curr, p3)
        cups[p3] = cups[dest]
        cups[dest] = p1
        
        curr = cups[curr]
        #print(cups)

a = cups[1]
b = cups[a]
print(a, b)
print("Part 2 answer:", a * b)
