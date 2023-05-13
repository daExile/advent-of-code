file = open("11.txt", "r")
import re, math

f = []
for line in file:
    if line.strip(): f.append(line.strip())
file.close()

ms = {}
for i in range(int(len(f)/6)):
    m = int(f[i*6][7])
    items = [int(x) for x in re.findall(r"\d+", f[i*6+1])]
    #print(items)
    op = f[i*6+2].rsplit(" ", 2)[1:]
    test = [int(f[i*6+3].rsplit(" ", 1)[1]), int(f[i*6+4][-1]), int(f[i*6+5][-1])]
    #print(m, op, test)
    ms[m] = {"items": items, "op": op, "test": test}
#print(ms)
    
rounds = 10000
r = 0
m_count = [0] * len(ms)
dall = 1
for m in ms:
    dall *= ms[m]["test"][0]
#print(dall)
#print(len(ms))
while r < rounds:
    for m in ms:
        #print("\nmonke", m, ms[m]["items"])
        if ms[m]["items"]:
            d = ms[m]["test"][0]
            for i in ms[m]["items"]:
                a = i if ms[m]["op"][1] == "old" else int(ms[m]["op"][1])
                i_n = i * a if ms[m]["op"][0] == "*" else i + a
                #i_n = math.floor(i_n / 3)
            
                if i_n % d == 0:
                    #ms[ms[m]["test"][1]]["items"].append(i_n)
                    ms[ms[m]["test"][1]]["items"].append(i_n % dall)
                    #print(i_n, i_n % ms[m]["test"][0], ms[m]["test"][1])
                else:
                    #ms[ms[m]["test"][2]]["items"].append(i_n)
                    ms[ms[m]["test"][2]]["items"].append(i_n % dall)
                    #print(i_n, i_n % ms[m]["test"][0], ms[m]["test"][2])
                m_count[m] += 1
            ms[m]["items"] = []
        #print(ms)

    #print("round", r+1)
    #for m in ms:
    #    print(m, ms[m]["items"])
    r += 1
    #print(m_count)

print(m_count)
m_count.sort(reverse = True)
print("Monkey business:", m_count[0] * m_count[1])
