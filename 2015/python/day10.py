old = input("Puzzle input: ")

for i in range(40):
    new = ""
    n = 0
    while n < len(old):
        s = old[n]
        j = 1
        while n + j < len(old) and old[n+j] == s:
            j += 1
        new += str(j) + s
        n += j
    print("...Turn", i+1, "-", len(new))
    old = new

print("Part 1 answer:", len(old))

for i in range(10):
    new = ""
    n = 0
    while n < len(old):
        s = old[n]
        j = 1
        while n + j < len(old) and old[n+j] == s:
            j += 1
        new += str(j) + s
        n += j
    print("...Turn", i+41, "-", len(new))
    old = new
    
print("Part 2 answer:", len(old))
