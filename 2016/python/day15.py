import re

class Disc:
    def __init__(self, teeth, init_pos = 0):
        self.t = teeth
        self.p0 = init_pos

d = [None]

file = open("15.txt", "r")
for line in file:
    _, t, _, p0 = [int(x) for x in re.findall("\d+", line)]
    d.append(Disc(t, p0))
file.close()

def yay(d, t = 0):
    yay = False
    while not yay:
        for i in range(1, len(d)):
            if (d[i].p0 + i + t) % d[i].t == 0: yay = True
            else:
                yay = False
                break
        if not yay: t += 1
    return t

print("Part 1 answer: t = {}".format(yay(d)))
d.append(Disc(11))
print("Part 2 answer: t = {}".format(yay(d)))
