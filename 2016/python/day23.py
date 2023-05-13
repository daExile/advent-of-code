code = []
file = open("23.txt", "r")
for line in file:
    s = line.strip()
    code.append(s.split())
#print(code)

#run it
def run_code(r):
    n = 0
    while n < len(code):
        #print(r)
        #print(n, code[n])
        if code[n][0] == "tgl":
            try: tgt = r[code[n][1]] + n
            except KeyError: tgt = code[n][1] + n

            if tgt not in range(0, len(code)): pass
            else:
                if code[tgt][0] == "cpy": code[tgt][0] = "jnz"
                elif code[tgt][0] == "jnz": code[tgt][0] = "cpy"
                elif code[tgt][0] == "inc": code[tgt][0] = "dec"
                else: code[tgt][0] = "inc"
            #print(code)
        elif code[n][0] == "inc":
            r[code[n][1]] += 1
        elif code[n][0] == "dec":
            r[code[n][1]] -= 1
        elif code[n][0] == "cpy":
            try: r[code[n][2]] = int(code[n][1])
            except ValueError: r[code[n][2]] = r[code[n][1]]
        else:
            try:
                if r[code[n][1]] != 0:
                    try: n += int(code[n][2])
                    except ValueError: n += r[code[n][2]]
                    continue
            except KeyError:
                if int(code[n][1]) != 0:
                    try: n += int(code[n][2])
                    except ValueError: n += r[code[n][2]]
                    continue
        n += 1
    return r

r = run_code({"a": 7, "b": 0, "c": 0, "d": 0})
print("Part 1, register A end value:", r["a"])

#r = run_code({"a": 12, "b": 0, "c": 0, "d": 0})
#print("Part 2, register A end value:", r["a"])
