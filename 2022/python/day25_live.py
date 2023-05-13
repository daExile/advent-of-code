file = open("25.txt", "r")

dec = []
for line in file:
    s = line.strip()
    n = 0
    p5 = 0
    for c in range(len(s) - 1, -1, -1):
        if s[c] == "-": t = -1
        elif s[c] == "=": t = -2
        else: t = int(s[c])
        n += (5 ** p5) * t
        p5 += 1
    dec.append(n)
    
file.close()
a_dec = sum(dec)

def dec2snafu(n):
    p5 = 0
    while 5 ** p5 <= a_dec:
        p5 += 1

    t = []
    while p5 >= 0:
        q, r = divmod(n, 5 ** p5)
        t.append(q)
        n = r
        p5 -= 1
        
    for i in range(len(t)-1, -1, -1):
        if t[i] > 2:
            t[i] -= 5
            t[i-1] += 1
    if t[0] == 0: t.pop(0)
    s = ""
    for i in t:
        if i == -1: s += "-"
        elif i == -2: s += "="
        else: s += str(i)
    return(s)
    
print(dec2snafu(a_dec))
