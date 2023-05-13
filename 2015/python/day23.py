file = open("23.txt", "r")

program = []
for line in file:
    s = line.strip()
    cmd = s[:3]
    if cmd in ("jmp", "inc", "tpl", "hlf"):
        program.append([cmd, s[4:]])
    else:
        a, b = s[4:].split(", ")
        program.append([cmd, a, b])
file.close()

a = b = 0
p = 0

while p < len(program):
    i = program[p]
    if i[0] == "inc":
        if i[1] == "a": a += 1
        else: b += 1
    elif i[0] == "hlf":
        if i[1] == "a": a, _ = divmod(a, 2)
        else: b, _ = divmod(a, 2)
    elif i[0] == "tpl":
        if i[1] == "a": a *= 3
        else: b *= 3
    elif i[0] == "jmp":
        p += int(i[1])
        continue
    elif i[0] == "jie":
        c = a if i[1] == "a" else b
        if c % 2 == 0:
            p += int(i[2])
            continue
    elif i[0] == "jio":
        c = a if i[1] == "a" else b
        if c == 1:
            p += int(i[2])
            continue
    p += 1

print("Part 1 answer:", b)

#bah i'll just copy it over lol

a = 1
b = 0
p = 0

while p < len(program):
    i = program[p]
    if i[0] == "inc":
        if i[1] == "a": a += 1
        else: b += 1
    elif i[0] == "hlf":
        if i[1] == "a": a, _ = divmod(a, 2)
        else: b, _ = divmod(a, 2)
    elif i[0] == "tpl":
        if i[1] == "a": a *= 3
        else: b *= 3
    elif i[0] == "jmp":
        p += int(i[1])
        continue
    elif i[0] == "jie":
        c = a if i[1] == "a" else b
        if c % 2 == 0:
            p += int(i[2])
            continue
    elif i[0] == "jio":
        c = a if i[1] == "a" else b
        if c == 1:
            p += int(i[2])
            continue
    p += 1

print("Part 2 answer:", b)
