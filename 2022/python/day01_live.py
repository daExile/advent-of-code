file = open("01.txt", "r")

elves = []
e = 0
for line in file:
    s = line.strip()
    if s:
        e += int(s)
    else:
        elves.append(e)
        e = 0
file.close()
print(max(elves))
elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])
