import itertools
file = open("25.txt", "r")

code = []
for line in file:
    s = line.strip()
    code.append(s.split())
#print(code)

def inc(a):
    a += 1

def dec(a):
    a -= 1

def cpy(a, b):
    b = a

#inc(a)
#cpy(2, a)
#cpy(a, b)
#dec(b)
#print(a, b, c, d)

#run it

def run_code(r):
    out_o = None
    count = 0
    countmax = 9 #turns out it's 192 with countmax = 9 or higher
    clkyeah = True
    n = 0
    while n < len(code) and count < countmax:
        #print(r)
        #print(n, code[n])
        if code[n][0] == "out":
            try: out_n = r[code[n][1]]
            except KeyError: out_n = code[n][1]

            if out_o == None or (out_o == 0 and out_n == 1) or (out_o == 1 and out_n == 0):
                out_o = out_n
                count += 1
            else:
                clkyeah = False
                break
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
    return clkyeah

a0 = 0
clkyeah = False
while not clkyeah:
    clkyeah = run_code({"a": a0, "b": 0, "c": 0, "d": 0})
    if not clkyeah: a0 += 1
print("P1:", a0)
