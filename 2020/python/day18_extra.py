#fancy_math = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
#fancy_math = "2 * 3 + (4 * 5)"
#fancy_math = "2 * 3 + 4 * 5"
#fancy_math = "5 + (8 * 3 + 9 + 3 * 4 * 3)"

# oh well, complete rework inbound.

def eval(math):
    # init
    expr = []
    if math.startswith("("):
        par_o = 1
        par_c = 0
        i = 0
        while not par_o == par_c:
            i += 1
            if math[i] == "(": par_o += 1
            elif math[i] == ")": par_c += 1
        expr.append(eval(math[1:i]))
        math = math[(i+1):].strip()
    else:
        t = math.split(" ", 1)
        expr.append(int(t[0]))
        math = t[1]

    # sort of calc
    while math:
        t = math.split(" ", 1)
        math = t[1]
        if t[0] == "*":
            if math.startswith("("):
                par_o = 1
                par_c = 0
                i = 0
                while not par_o == par_c:
                    i += 1
                    if math[i] == "(": par_o += 1
                    elif math[i] == ")": par_c += 1
                expr.append(eval(math[1:i]))
                math = math[(i+1):].strip()
            else:
                t = math.split(" ", 1)
                math = t[1] if len(t) > 1 else ""
                expr.append(int(t[0]))
        else:
            if math.startswith("("):
                par_o = 1
                par_c = 0
                i = 0
                while not par_o == par_c:
                    i += 1
                    if math[i] == "(": par_o += 1
                    elif math[i] == ")": par_c += 1
                expr[-1] += eval(math[1:i])
                math = math[(i+1):].strip()
            else:
                t = math.split(" ", 1)
                math = t[1] if len(t) > 1 else ""
                expr[-1] += int(t[0])

    # print(expr)
    a = 1
    for i in expr:
        a *= i
    return a

#print(eval(fancy_math))

n, total = 0, 0
file = open("18.txt", "r")
for line in file:
#    result = eval(line.strip())
#    n += 1
#    print(n, ":", result)
    total += eval(line.strip())
file.close()

print(total)
