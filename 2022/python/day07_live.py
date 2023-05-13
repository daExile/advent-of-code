file = open("07.txt", "r")
import re

curr = ""
h = []

f = []
dirs = {}
dirsizes = {}
for line in file:
    f.append(line.strip())
file.close()

def get_dirsize(d, l):
    #print("dir =", d, "lv =", l, "items:", dirs[d])
    size = 0
    for item in dirs[d]:
        if item[1] == "dir":
            if item[0] in dirsizes: size += dirsizes[item[0]]
            else:
                t = get_dirsize(item[0], l+1)
                dirsizes[item[0]] = t
                size += t                
        else: size += item[1]
    #print("size =", size)
    return size

i = 0
d_id = 0
while i < len(f):
    s = f[i]
    if s.startswith("$ cd"):
        t = s[5:]
        #print(h, t)
        if t == "..":
            h.pop()
            curr = "".join(h)
        else:
            if not h: curr = t
            else: curr = h[-1] + t 
            h.append(curr)                     
    elif s.startswith("$ ls"):
        if curr not in dirs: dirs[curr] = []
        j = 1
        while (i+j) < len(f) and not f[i+j].startswith("$"):
            a, b = f[i+j].split()
            try:
                a = int(a)
            except ValueError:
                b = curr + b
            dirs[curr].append((b, a))
            j += 1
        i += j - 1
    i += 1
#print(dirs)
ans1 = 0
for d in dirs:
    a = get_dirsize(d, 0)
    if a <= 100000: ans1 += a
    dirsizes[d] = a
print("Part 1 answer:", ans1)

to_free = 30000000 - (70000000 - dirsizes["/"])
m2del = dirsizes["/"]
for item in dirsizes:
    if dirsizes[item] >= to_free and dirsizes[item] < m2del: m2del = dirsizes[item]
print("Part 2 answer:", m2del)
