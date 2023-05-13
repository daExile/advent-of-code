code = []
file = open("12.txt", "r")
for line in file:
    s = line.strip()
    code.append(s.split())
#print(code)

#run it
def run_code(r):
    n = 0
    while n < len(code):
        if code[n][0] == "inc":
            r[code[n][1]] += 1
        elif code[n][0] == "dec":
            r[code[n][1]] -= 1
        elif code[n][0] == "cpy":
            try: r[code[n][2]] = int(code[n][1])
            except ValueError: r[code[n][2]] = r[code[n][1]]
        else:
            try:
                if r[code[n][1]] != 0:
                    n += int(code[n][2])
                    continue
            except KeyError:
                if int(code[n][1]) != 0:
                    n += int(code[n][2])
                    continue
        n += 1
    return r

r = run_code({"a": 0, "b": 0, "c": 0, "d": 0})
print("Part 1, register A end value:", r["a"])

r = run_code({"a": 0, "b": 0, "c": 1, "d": 0})
print("Part 2, register A end value:", r["a"])
