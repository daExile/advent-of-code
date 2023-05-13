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

print("Deck 1:", d1)
print("Deck 2:", d2)

#history check
#it would be nice if i added history.append() to start with, right?
#d1 = [43, 19]
#d2 = [2, 29, 14]

#now let's play it
#yeah i don't want to refactor it into d[[1], [2]] at this point
#so it will be clunky stuff

r_lvl = 0

def play(d1_i, d2_i):
    d1 = d1_i[:]
    d2 = d2_i[:]
    global r_lvl
    history = []
    while d1 and d2:
        #print(history)
        #print([d1[:], d2[:]])
        if [d1[:], d2[:]] not in history:
            history.append([d1[:], d2[:]])
            p1 = d1.pop(0)
            p2 = d2.pop(0)
            #print(p1,"v", p2)
            if len(d1) >= p1 and len(d2) >= p2:
                #print(" " * r_lvl, "Recursive...")
                r_lvl += 1
                x, _ = play(d1[:p1], d2[:p2])   #right, slices i forgot about
                if x == 1: d1.extend([p1, p2])
                else: d2.extend([p2, p1])
            else:
                if p1 > p2: d1.extend([p1, p2])
                else: d2.extend([p2, p1])
            #print("Deck 1:", d1)
            #print("Deck 2:", d2)
        else:
            #print(" " * r_lvl, "Happened before!")
            r_lvl -= 1
            return(1, d1)
    r_lvl -= 1
    if d1: return(1, d1)
    else: return(2, d2)

#count win score
ans = 0
_, win = play(d1, d2)
for i in range(len(win)):
    ans += (len(win) - i) * win[i]

print("Win score:", ans)
