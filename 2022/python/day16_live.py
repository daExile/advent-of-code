file = open("16.txt", "r")
import re
tmax = 30

vs = {}
for line in file:
    a = re.findall(r"([A-Z][A-Z])", line)
    f = int(re.search(r"(\d+)", line).group())
    vs[a[0]] = {"f":f, "t":a[1:]}

vnz = []
for v in vs:
    if vs[v]["f"] > 0: vnz.append(v)

def path(v, dest, p = [], pbest = None):
    p.append(v)
    if pbest and len(p) >= pbest: return None
    if dest in vs[v]["t"]:
        p_n = p[:]
        p_n.append(dest)
        return p_n
    else:
        p_n = []
        for t in vs[v]["t"]:
            if t in p: continue
            p_t = path(t, dest, p[:], pbest)
            if p_t:
                if not pbest or len(p_t) < pbest:
                    p_n = p_t[:]
                    pbest = len(p_t)
        return p_n

#route lengths between nonzero valves
rs = {}
for v in vnz:
    rs[v] = {}
    ds = vnz[:]
    ds.pop(ds.index(v))
    for d in ds:
        t = path(v, d, [])
        rs[v][d] = len(t) - 1
#print(rs)

def go(start, dest = "", t0 = 0, pr = 0, pr_turn = 0, v_open = [], pr_best = 0):
    #print(v_open, t0)
    t = t0
    if dest:
        if start == "AA": steps = len(path("AA", dest, []))-1
        else: steps = rs[start][dest]
        while t < tmax:
            steps -= 1
            pr += pr_turn
            t += 1
            if steps < 0:
                pr_turn += vs[dest]["f"]
                v_open.append(dest)
                #print("now these are open:", v_open, "for", pr_turn, "total")
                break
        if t == tmax:
            #print("ey")
            #pr += pr_turn
            if pr > pr_best: return pr
            else: return pr_best
        else:
            #print(dest, [x for x in rs[dest] if x not in v_open])
            for v in rs[dest]:
                if v in vnz and v not in v_open:
                    pr_best = go(dest, v, t, pr, pr_turn, v_open[:], pr_best)
            #and "just waiting here" option
            #print("huh")
            pr += (tmax - t) * pr_turn
            #print("v:", v_open, "pr:", pr)
            if pr > pr_best: pr_best = pr
    else:
        for v in vnz:
            pr_best = go(start, v, pr_best = pr_best, v_open = [])
    return pr_best

print("P1:", go("AA"))

#here's trouble, let's make it double
tmax -= 4

def go_together(o1, o2, d1 = "", d2 = "", s1 = None, s2 = None, t0 = 0, pr = 0, pr_turn = 0, v_open = [], pr_best = 0):
    t = t0
    ele_f = []
    if not d1 and not d2:
        for v in vnz:
            ele_f.append(v)
            for v_e in vnz:
                if v != v_e and v_e not in ele_f:
                    print(v, v_e)
                    pr_best = go_together(o1, o2, v, v_e, pr_best = pr_best, v_open = [])                
        
    else:
        #print(o1, d1, s1, o2, d2, s2, pr_turn)
        if s1 == None and d1 != "Stay":
            if o1 == "AA":
                s1 = len(path("AA", d1, []))-1
                #print("you", o1, d1, s1)
            else:
                s1 = rs[o1][d1]
                #print("you", o1, d1, s1)
        
        if s2 == None and d2 != "Stay":
            if o2 == "AA":
                s2 = len(path("AA", d2, []))-1
                #print("ele", o2, d2, s2)                
            else:
                s2 = rs[o2][d2]
                #print("ele", o2, d2, s2)
        brk = False
        while t < tmax and not brk:
            #print(o1, o2, d1, d2, s1, s2, pr_turn)
            if d1 != "Stay": s1 -= 1
            if d2 != "Stay": s2 -= 1
            #print(d1, d2, s1, s2, pr, pr_turn)
            pr += pr_turn
            t += 1
            if s1 != None and s1 < 0:
                pr_turn += vs[d1]["f"]
                v_open.append(d1)
                #print("now open:",v_open, pr_turn, "on", t, d1, d2)
                brk = True
            if s2 != None and s2 < 0:
                pr_turn += vs[d2]["f"]
                v_open.append(d2)
                #print("now open:",v_open, pr_turn, "on", t, d1, d2)
                brk = True
                
        if t == tmax:
            #print(v_open, pr_turn, pr, pr_best)
            if pr > pr_best: return pr
            else: return pr_best
        else:
            if s1 != None and s1 < 0 and s2 != None and s2 < 0:
                for v in rs[d1]:
                    for v_e in rs[d2]:
                        if v in vnz and v not in v_open and v_e in vnz and v_e not in v_open and v != v_e:
                            #print(v, v_e)
                            pr_best = go_together(d1, d2, v, v_e, None, None, t, pr, pr_turn, v_open[:], pr_best)            
                #pr_best = go_together(d1, d2, "Stay", "Stay", None, None, t, pr, pr_turn, v_open[:], pr_best)
            elif s1 != None and s1 < 0:
                for v in rs[d1]:
                    if v in vnz and v not in v_open and v != d2:
                        pr_best = go_together(d1, o2, v, d2, None, s2, t, pr, pr_turn, v_open[:], pr_best)
                #pr_best = go_together(d1, o2, "Stay", d2, None, s2, t, pr, pr_turn, v_open[:], pr_best)
            elif s2 != None and s2 < 0:
                for v_e in rs[d2]:
                    if v_e in vnz and v_e not in v_open and v_e != d1:
                        pr_best = go_together(o1, d2, d1, v_e, s1, None, t, pr, pr_turn, v_open[:], pr_best)
                #pr_best = go_together(o1, d2, d1, "Stay", s1, None, t, pr, pr_turn, v_open[:], pr_best)

            if pr > pr_best: pr_best = pr
    return pr_best

print("P2:", go_together("AA", "AA"))
