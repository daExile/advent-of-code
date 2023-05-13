file = open("19.txt", "r")
import re, math

tmax = 24
bps = {}
for line in file:
    data = [int(x) for x in re.findall(r"(\d+)", line)]
    bp = data[0]
    ore = (data[1], 0, 0, 0)
    cly = (data[2], 0, 0, 0)
    obs = (data[3], data[4], 0, 0)
    geo = (data[5], 0, data[6], 0)
    bps[bp] = [ore, cly, obs, geo]

#for bp in bps:
#    print(bp, bps[bp])

def get_dt(c, rs, res):
    dts = [max(0, (math.ceil((bps[bp][c][i]-res[i])/rs[i])))+1 if rs[i] > 0 else 0 for i in range(3)]
    return max(dts)

def go(bp, t = 0, rs = [1, 0, 0, 0], res = [0, 0, 0, 0]):
    if t in glog:
        if glog[t] > res[3]: return 0
        elif res[3] > glog[t]: glog[t] = res[3]
    else: glog[t] = res[3]

    if t == tmax - 1:
        return res[3] + rs[3]
    else:
        geo_max = res[3]
        choices = []        
        if rs[2] > 0: choices.append(3)
        if rs[1] > 0 and get_dt(2, rs, res) <= get_dt(3, rs, res): choices.append(2)
        if rs[1] < bps[bp][2][1]: choices.append(1)
        if rs[0] < omax: choices.append(0)
        #print(choices)
        for c in choices:
            dt = get_dt(c, rs, res)
            #print(c, dt)

            if t + dt >= tmax:
                dt = tmax - t
                a = res[3] + dt*rs[3]
                if res[3] > geo_max: geo_max = res[3]
            else:
                res_n = [r+dt*rs[i]-bps[bp][c][i] for i, r in enumerate(res)]
                rs_n = rs[:]
                rs_n[c] += 1
                a = go(bp, t+dt, rs_n[:], res_n[:])
                if a > geo_max: geo_max = a
        return geo_max

ql = {}
p1_a = 0
print("Part 1")
for bp in bps:
    omax = max([bps[bp][i][0] for i in range(3)])
    glog = {}
    ql[bp] = go(bp)
    print("BP{:02d} quality level: {}".format(bp, ql[bp]))
    p1_a += bp * ql[bp]
print("Answer:", p1_a)

print("\nPart 2")
tmax = 32
g = {}
p2_a = 1
for bp in range(1, 4):
    omax = max([bps[bp][i][0] for i in range(3)])
    glog = {}
    g[bp] = go(bp)
    print("Geodes from BP{:02d}: {}".format(bp, g[bp]))
    p2_a *= g[bp]
print("Answer:", p2_a)
