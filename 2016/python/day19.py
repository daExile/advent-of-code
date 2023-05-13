my_input = int(input("Puzzle input: "))
#my_input = 5

def setup(n):
    e = []
    for i in range(n):
        e.append(i+1)
    return e

i = 0
e = setup(my_input)
while len(e) > 1:
    a = len(e)
    e = e[i::2]
    if a % 2 == 1: i = (i + 1) % 2

print("Elves:", my_input)
print("Rules v.1:")
print("Last elf standing: #{}".format(e[0]))

print("Rules v.2:")
#this gonna take eternity for now
#really should speed this up
i = 0
e = setup(my_input)
while len(e) > 1:
    a = int(i + len(e)/2) % len(e)
    b = e[i]
    e.pop(a)
    i = e.index(b) + 1 % len(e)
    if i >= len(e): i = 0
    if len(e) % 10000 == 0: print("{} left...".format(len(e)))
print("Last elf standing: #{}".format(e[0]))
