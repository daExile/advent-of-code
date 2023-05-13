file = open("04.txt", "r")

count = 0
count2 = 0
for line in file:
    s = line.strip()
    i, j = line.split(",")
    a, b = [int(x) for x in i.split("-")]
    c, d = [int(x) for x in j.split("-")]
    if a <= c and b >= d: count += 1
    elif c <= a and d >= b: count += 1

    l1 = range(a, b+1)
    l2 = range(c, d+1)
    lc = len(set(l1) & set(l2))
    if lc > 0: count2 += 1
file.close()
print(count)
print(count2)
