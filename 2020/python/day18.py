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


def eval(math):
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

#print(eval(fancy_math))

n, total = 0, 0
file = open("18.txt", "r")
for line in file:
    result = eval(line.strip())
#    n += 1
#    print(n, ":", result)
    total += eval(line.strip())
file.close()

print(total)
