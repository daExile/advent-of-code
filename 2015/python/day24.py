import itertools as it
file = open("24.txt", "r")

packs = []
for line in file:
    packs.append(int(line.strip()))
file.close()

one_third = (int(sum(packs) / 3))

n = 1 #optimistic haha
g1 = []
while not g1 or n > len(packs):
    g1 = [x for x in it.combinations(packs, n) if sum(x) == one_third]
    n += 1

print("Part 1\nPassenger compartment:\n{} variants".format(len(g1)))

#let's check if they're all making valid solutions for the rest of it
#... they all are, hence commented out for FAST
#g1_c = []
#for v in g1:
#    g2_3 = [x for x in packs if x not in v]
#    n = 1
#    g2 = []
#    while not g2 or n > int(len(g2_3) / 2):
#        g2 = [x for x in it.combinations(g2_3, n) if sum(x) == one_third]
#        n += 1
#    if g2: g1_c.append(v)
#
#print("{} valid variants".format(len(g1_c)))

qe = None
for v in g1:
    qe_cur = 1
    for p in v: qe_cur *= p
    if not qe or qe_cur < qe: qe = qe_cur

print("Part 1 answer:", qe)

one_quarter = (int(sum(packs) / 4))
n = 1 #optimistic haha
g1 = []
while not g1 or n > len(packs):
    g1 = [x for x in it.combinations(packs, n) if sum(x) == one_quarter]
    n += 1

print("\nPart 2\nPassenger compartment:\n{} variants".format(len(g1)))

qe = None
for v in g1:
    qe_cur = 1
    for p in v: qe_cur *= p
    if not qe or qe_cur < qe: qe = qe_cur

print("Part 2 answer:", qe)
