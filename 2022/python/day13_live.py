file = open("13.txt", "r")
import ast

dstream = []
for line in file:
    s = line.strip()
    if s:
        d = ast.literal_eval(s)
        dstream.append(d)

#get those in pairs for some convenience
data = []
for i in range(0, len(dstream), 2):
    data.append([dstream[i], dstream[i+1]])

def cmp(pl, pr):
    #print(pl, "and", pr)
    
    i = 0
    t = True
    while t:
        try:
            a = pl[i]
            #print("a", a)
        except IndexError: t = False
        
        try:
            b = pr[i]
            if not t: return 1
            #print("b", b)
        except IndexError:
            if t: return -1
            else: break

        if t:
            if type(a) == type(b):
                if isinstance(a, int):
                    if a > b: return -1
                    elif a < b: return 1
                elif isinstance(a, list):
                    if cmp(a, b): return cmp(a, b)
            else:
                if isinstance(a, int):
                    if cmp([a], b): return cmp([a], b)
                if isinstance(b, int):
                    if cmp(a, [b]): return cmp(a, [b])
            i += 1
    return 0

ix = 1
csum = 0
d_cor = []
for p in data:
    #print("{}\n{}".format(p[0], p[1]))
    if cmp(p[0], p[1]) >= 0:
        csum += ix
    ix += 1

print("P1:", csum)

#alriiiiight let's sort packets in some ineffective way lol
dstream.append([[2]])
dstream.append([[6]])


for i in range(len(dstream) - 1):
    d_next = []
    for j in range(len(dstream) - i - 1):
        a = dstream.pop(0)
        b = dstream.pop(0)
        if cmp(a, b) >= 0:
            d_next.append(a)
            dstream.insert(0, b)
        else:
            d_next.append(b)
            dstream.insert(0, a)
    dstream = d_next[:] + dstream

print("P2:", (dstream.index([[2]])+1) * (dstream.index([[6]])+1))
