#fancy_math = "5 + (4 * (3 + 2 + 5 + 9 * 3))"
p = False

def eval_p(math):
    if math.startswith("("):
        t = eval_p(math[1:])
        a, math = int(t[0]), t[1]
    else:
        t = math.split(" ", 1)
        a, math = int(t[0]), t[1]
    while math:
        t = math.split(" ", 1)
        math = t[1]
        if t[0] == "*":
            if math.startswith("("):
                t = eval_p(math[1:])
                math = t[1]
                if p: print("tp*", t)
                if t[0].endswith(")"):
                    tmp = t[0].split(")", 1)
                    a *= int(tmp[0])
                    if len(tmp) == 1: a = str(a)
                    else: a = str(a) + (tmp[1])
                    break
                else:
                    a *= int(t[0])
                    math = t[1]
            else:
                t = math.split(" ", 1)
                if p: print("t *", t)
                math = t[1] if len(t) > 1 else ""
                if t[0].endswith(")"):
                    tmp = t[0].split(")", 1)
                    a *= int(tmp[0])
                    if len(tmp) == 1: a = str(a)
                    else: a = str(a) + (tmp[1])
                    break
                else:
                    a *= int(t[0])
        else:
            if math.startswith("("):
                t = eval_p(math[1:])
                math = t[1]
                if p: print("tp+", t)
                if t[0].endswith(")"):
                    tmp = t[0].split(")", 1)
                    a += int(tmp[0])
                    if len(tmp) == 1: a = str(a)
                    else: a = str(a) + (tmp[1])
                    math = t[1]
                    break
                else:
                    a += int(t[0])
            else:
                t = math.split(" ", 1)
                if p: print("t +", t)
                math = t[1] if len(t) > 1 else ""
                if t[0].endswith(")"):
                    tmp = t[0].split(")", 1)
                    a += int(tmp[0])
                    if len(tmp) == 1: a = str(a)
                    else: a = str(a) + (tmp[1])
                    break
                else:
                    a += int(t[0])
    if p: print([a, math])
    return [a, math]

def eval_p1(math):
    if math.startswith("("):
        t = eval_p(math[1:])
        a, math = int(t[0]), t[1]
    else:
        t = math.split(" ", 1)
        a, math = int(t[0]), t[1]
    while math:
        t = math.split(" ", 1)
        math = t[1]
        if t[0] == "*":
            if math.startswith("("):
                t = eval_p(math[1:])
                a *= int(t[0])
                math = t[1]
            else:
                t = math.split(" ", 1)
                math = t[1] if len(t) > 1 else ""
                a *= int(t[0])
        else:
            if math.startswith("("):
                t = eval_p(math[1:])
                a += int(t[0])
                math = t[1]
            else:
                t = math.split(" ", 1)
                math = t[1] if len(t) > 1 else ""
                a += int(t[0])
    return a

def eval_p2(math):
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
        expr.append(eval_p2(math[1:i]))
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
                expr.append(eval_p2(math[1:i]))
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
                expr[-1] += eval_p2(math[1:i])
                math = math[(i+1):].strip()
            else:
                t = math.split(" ", 1)
                math = t[1] if len(t) > 1 else ""
                expr[-1] += int(t[0])

    a = 1
    for i in expr:
        a *= i
    return a

n, total_p1, total_p2 = 0, 0, 0
file = open("18.txt", "r")
for line in file:
    total_p1 += eval_p1(line.strip())
    total_p2 += eval_p2(line.strip())
file.close()

print("Part 1:", total_p1)
print("Part 2:", total_p2)
