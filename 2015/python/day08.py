file = open("08.txt", "r")

s_code = s_mem = s_enc = 0
for line in file:
    s = line.strip()
    s_code += len(s)

    i = 1
    while i < len(s[1:-1]) + 1:
        if s[i] == "\\":
            if s[i+1] == "x": i += 4
            else: i += 2
        else: i += 1
        s_mem += 1
    #print(s_code, s_mem, s[i])

    s_enc += 2
    for i in range(len(s)):
        if s[i] in ["\"", "\\"]: s_enc += 2
        else: s_enc += 1

file.close()
print("Part 1 answer:", s_code - s_mem)
print("Part 2 answer:", s_enc - s_code)
