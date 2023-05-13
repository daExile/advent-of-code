import re
#file = ["e => H",
#        "e => O",
#        "H => HO",
#        "H => OH",
#        "O => HH",
#        "",
#        "HOHOHO",]
file = open("19.txt", "r")

def list_atoms(molecule):
    atoms = []
    ins = [index.start() for index in re.finditer("[A-Z]", molecule)]
    for a, i in enumerate(ins):
        try: atoms.append(molecule[ins[a]:ins[a+1]])
        except IndexError: atoms.append(molecule[ins[a]:])
    return atoms

reps = {}
for line in file:
    s = line.strip()
    if not s: break
    else:
        o, r = s.split(" => ")
        atoms = list_atoms(r)
        if o in reps:
            reps[o].append(atoms)
        else: reps[o] = [atoms]

#target = list_atoms(file[-1].strip())
target = list_atoms(file.readline().strip())
file.close()

distinct = []
for i, a in enumerate(target):
    if a in reps.keys():
        for r in reps[a]:
            try: m_new = target[:i] + r + target[i+1:]
            except IndexError: m_new = target[:i] + r
            if m_new not in distinct: distinct.append(m_new)
            
print("Part 1 answer:", len(distinct))

rep_potential = {}
for a in reps.keys():
    t = []
    for i in reps[a]:
        if i[0] not in t: t.append(i[0])
    u = 0
    while u < len(t):
        try:
            for i in reps[t[u]]:
                if i[0] not in t: t.append(i[0])
        except KeyError: pass
        u += 1
    rep_potential[a] = t
#print(rep_potential)
#print(reps)
    
def check_chem(p, m):
    if len(m) > len(target) or p >= len(m): return []
    elif m[p] not in reps.keys():
        if m[p] == target[p]: return check_chem(p+1, m) 
        else: return []
    elif m[p] == target[p]:
        if target[p] in rep_potential[m[p]]: return [p] + check_chem(p+1, m)
        else: return check_chem(p+1, m)
    else:
        if target[p] in rep_potential[m[p]]: return [p]
        else: return []

chem = [(0, ["e"])]
log = []
steps = 0
while (target not in [c[1] for c in chem]): #and steps < 3:
    print("\n", steps, "\n")
    chem_new = []
    for c in chem:
        p, m = c
        #print(m, p)
        if p < len(m):
            for var in reps[m[p]]:
                m_new = m[:p] + var + m[p+1:] if p+1 < len(m) else m[:p] + var
                #print(m_new)
                p_new = check_chem(p, m_new)
                if p_new and m_new not in log:
                    [chem_new.append((p_i, m_new)) for p_i in p_new]
                    log.append(m_new)
    print(chem_new)
    chem = chem_new[:]
    steps += 1

print("Part 2 answer:", steps)
