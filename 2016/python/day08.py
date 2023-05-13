#init a list for display, idk seems right
#not strings this time, maybe next time i should try arrays
d = []
row = ["." for _ in range(50)]
for rows in range(6):
    d.append(row[:])

file = open("08.txt", "r")
for line in file:
    s = line.strip()
    
    if s.startswith("rect"):
        c = s[5:].split("x")
        x, y = int(c[0]), int(c[1])
        for i in range(y):
            for j in range(x):
                d[i][j] = "#"
    else:
        c = s[7:].split(" ", 1)
        if c[0] == "row":
            c = c[1][2:].split(" by ")
            y, s = int(c[0]), int(c[1])
            d[y] = d[y][-s:] + d[y][:-s]
        else:
            c = c[1][2:].split(" by ")
            x, s = int(c[0]), int(c[1])
            #bah manual slicing
            t = []
            for y in range(6):
                t.append(d[y][x])
            t = t[-s:] + t[:-s]
            for y in range(6):
                d[y][x] = t[y]
#print that out
for i in range(6):
    r = "".join(d[i])
    print(r)
print("\n")

count = 0
for i in range(6):
    count += d[i].count("#")

print("Lit pixels total:", count)
