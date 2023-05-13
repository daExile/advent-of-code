my_input = int(input("Puzzle input: "))
target = (31, 39)
office = {}
start = (1, 1)

def is_wall(a, fnum = 10):
    x, y = a
    if bin(x*x + 3*x + 2*x*y + y + y*y + fnum).count("1") % 2 == 0:
        return False
    return True

def find_dist(start, target):
    office[start] = 0
    curr = [start]
    n = 1
    while target not in office:
        nstep = []
        for i in curr:
            for j in [(i[0]+1, i[1]), (i[0], i[1]+1), (i[0]-1, i[1]), (i[0], i[1]-1)]:
                if j[0] < 0 or j[1] < 0: continue
                if j not in nstep and j not in office:
                    if not is_wall(j, my_input):
                        nstep.append(j)
                        office[j] = n
                    else: office[j] = "#"
        n += 1
        curr = nstep[:]
    return(office[target])

print("Part 1: distance to {}:".format(target), find_dist(start, target))
o50 = {}
for i in office.keys():
    if office[i] != "#" and office[i] <= 50: o50[i] = office[i]
print("Part 2: tiles within 50 steps:", len(o50))
