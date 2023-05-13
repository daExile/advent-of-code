file = open("23.txt", "r")
import re

elves = []
row = 0
for line in file:
    e = [index.start() for index in re.finditer(r"#", line)]
    if e:
        for i in e: elves.append((row, i))
    row += 1

#for y in range(-2, 9):
#    print("".join(["#" if (y, x) in elves else "." for x in range(-3, 11)]))
#print(elves)
prop = [(-1, 0), (1, 0), (0, -1), (0, 1)]
neigh_order = [-2, 2, 4, 0]
def propose(elf, d):
    sur_xy = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
    sur = [1 if (elf[0]+s[0], elf[1]+s[1]) in elves else 0 for s in sur_xy]

    if sum(sur) == 0: return None
    #why the hell sum() didn't work
    neigh = [sur[k]+sur[k+1]+sur[k+2] for k in neigh_order]
    neigh = neigh[d:] + neigh[:d]
    
    for i, n in enumerate(neigh):
        if n == 0:
            return (elf[0]+prop[(d+i)%4][0],elf[1]+prop[(d+i)%4][1])
    return None
            
d = 0 #0123 = NSWE
r = 0
while True:
    r += 1
    #proposal phase
    e_props = {}
    for e in elves:
        e_p = propose(e, d)
        if e_p:
            if e_p not in e_props: e_props[e_p] = [e]
            else: e_props[e_p].append(e)

    #collision check / movement
    movecount = 0
    for e in e_props:
        #print(e, e_props[e])
        if len(e_props[e]) == 1 and e_props[e][0]:
            elves.remove(e_props[e][0])
            elves.append(e)
            movecount += 1
    print("Round {} - elves moved: {}".format(r, movecount))
    if r == 10:
        elves.sort(key = lambda e: e[0])
        dy = elves[-1][0] - elves[0][0] + 1
        elves.sort(key = lambda e: e[1])
        dx = elves[-1][1] - elves[0][1] + 1
        print("...Part 1 answer:", dy * dx - len(elves))
    if movecount:
        d += 1
        if d == 4: d = 0
    else: break

print("...Part 2 answer:", r)
