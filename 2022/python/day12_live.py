file = open("12.txt", "r")
import re, math

m = []
n = 0
for line in file:
    s = list(line.strip())
    m.append(s)
    if "E" in s: dest = (s.index("E"), n)
    if "S" in s:
        start = (s.index("S"), n)
        m[start[1]][start[0]] = "a"
    n += 1

all_a = []
for i, row in enumerate(m):
    for j, item in enumerate(row):
        if item == "a": all_a.append((j, i))
    
x, y = len(m[0])-1, len(m)-1

hchart = "abcdefghijklmnopqrstuvwxyzE"

def viable_ps(xy):
    a = []
    if 0 <= xy[0]-1: a.append((xy[0]-1,xy[1]))
    if xy[0]+1 <= x: a.append((xy[0]+1,xy[1]))
    if 0 <= xy[1]-1: a.append((xy[0],xy[1]-1))
    if xy[1]+1 <= y: a.append((xy[0],xy[1]+1))
    return a

def hcheck(xy0, xy):
    if hchart.index(m[xy0[1]][xy0[0]])+1 >= hchart.index(m[xy[1]][xy[0]]):
        return True
    return False


#solve for S
pf = {0: [start]}
log = [start]
n = 0

while True:
    pf[n+1] = []
    for p in pf[n]:
        q = viable_ps(p)
        for item in q:
            if hcheck(p, item) and item not in log:
                log.append(item)
                pf[n+1].append(item)
    if dest in log:
        print("P1:", n+1)
        break
    else: n += 1

#solve for all a's
pf = {0: all_a[:]}
log = all_a[:]
n = 0

while True:
    pf[n+1] = []
    for p in pf[n]:
        q = viable_ps(p)
        for item in q:
            if hcheck(p, item) and item not in log:
                log.append(item)
                pf[n+1].append(item)
    if dest in log:
        print("P2:", n+1)
        break
    else: n += 1
