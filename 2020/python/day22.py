d1, d2 = [], []
file = open("22.txt", "r")
#load deck 1
for line in file:
    if line.startswith("Player"): pass
    elif line.strip():
        d1.append(int(line.strip()))
    else: break
#load deck 2
for line in file:
    if line.startswith("Player"): pass
    elif line.strip():
        d2.append(int(line.strip()))
    else: break
file.close()

r_lvl = 0

def play(d1_i, d2_i, recursive):
    d1 = d1_i[:]
    d2 = d2_i[:]
    global r_lvl
    history = []
    while d1 and d2:
        if [d1[:], d2[:]] not in history:
            history.append([d1[:], d2[:]])
            p1 = d1.pop(0)
            p2 = d2.pop(0)

            if recursive and len(d1) >= p1 and len(d2) >= p2:
                r_lvl += 1
                x, _ = play(d1[:p1], d2[:p2], True) #right, slices i forgot about
                if x == 1: d1.extend([p1, p2])
                else: d2.extend([p2, p1])
            else:
                if p1 > p2: d1.extend([p1, p2])
                else: d2.extend([p2, p1])

        else:
            r_lvl -= 1
            return(1, d1)
        
    r_lvl -= 1
    if d1: return(1, d1)
    else: return(2, d2)

ans = 0
_, win = play(d1[:], d2[:], False)
for i in range(len(win)):
    ans += (len(win) - i) * win[i]

print("Part 1:", ans)

ans = 0
_, win = play(d1[:], d2[:], True)
for i in range(len(win)):
    ans += (len(win) - i) * win[i]
print("Part 2:", ans)
