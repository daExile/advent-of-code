import re
#this goes into some sort of a endless loop,
#i got the answer but needs a fix lol
#maybe it's not endless but like (answer)! checks,
#if there's a lot of way to arrive to 'e',
#and it seems so, since there seems to be
#no variance in found (med -> 'e') steps numbers.

#file = ["e => H",
#        "e => O",
#        "H => HO",
#        "H => OH",
#        "O => HH",
#        "",
#        "HOHOHO",]
file = open("19.txt", "r")

p_p = {}
for line in file:
    s = line.strip()
    if not s: break
    else:
        prec, prod = s.split(" => ")
        if prod in p_p: print("fuck")
        else: p_p[prod] = prec

#print(p_p)
#med = (file[-1].strip())
med = (file.readline().strip())
file.close()

def get_matches(med):
    l = []
    for prod in p_p:
        if prod in med: l.append((prod, med.rfind(prod)))
    l.sort(reverse = True, key = lambda i: i[1] + len(i[0]))
    return(l)

def get_step_n(med, step, s_min = None):
    mlist = get_matches(med)
    if not mlist:
        s = None
    else:
        for i in mlist:
            r = p_p[i[0]]
            med_p = med[:i[1]] + r
            if i[1] + len(i[0]) < len(med): med_p += med[(i[1] + len(i[0])):]
            if r == "e" and len(med_p) == 1:
                s = step + 1
                print("Reached \'e\' on step {}".format(s))
            elif r == "e" and len(med_p) > 1: s = None
            else: s = get_step_n(med_p, step + 1, s_min)
                
            if not s: pass
            elif not s_min: s_min = s
            elif s_min > s: s_min = s
    return s_min

a = get_step_n(med, 0)
                             
print("Part 2 answer:", a)
