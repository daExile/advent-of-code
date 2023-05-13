file = open("21.txt", "r")

monke = {}
m_n = {}

for line in file:
    s = line.strip()
    m, j = s[0:4], s[6:]
    try: monke[m] = int(j)
    except ValueError: monke[m] = (s[11], s[6:10], s[13:])
file.close()

def sign(a):
    if a == 0: return 0
    else:
        if a > 0: return 1
        return -1

def monke_number(m):
    if m in m_n: return m_n[m]
    else:
        if isinstance(monke[m], int):
            m_n[m] = monke[m]
        else:
            a = monke_number(monke[m][1])
            b = monke_number(monke[m][2])
            m_n[m] = eval("{} {} {}".format(a, monke[m][0], b))
        return m_n[m]

def monke_only_number(m):
    if m in m_n: return m_n[m]
    elif m == "humn": return None
    else:
        if isinstance(monke[m], int):
            m_n[m] = monke[m]
        else:
            a = monke_only_number(monke[m][1])
            b = monke_only_number(monke[m][2])
            if a == None or b == None: return None
            elif monke[m][0] == "=": return None
            else:
                m_n[m] = eval("{} {} {}".format(a, monke[m][0], b))
        return m_n[m]
            
#print(monke)
print("P1:", int(monke_number("root")))

#bruteforcing part 2 of course
monke["root"] = ("-", monke["root"][1], monke["root"][2])

m_n = {}
#preload all ints
for m in monke:
    monke_only_number(m)
m_st = dict(m_n)
#print(m_st)
#n = 3916936880000
#now make a code to search for it by digits
n = 0
m_n["humn"] = n #bah entry point
s_o = sign(monke_number("root"))

done = False
#get 
while not done:
    #print(n)
    m_n = dict(m_st)
    m_n["humn"] = 10 ** n
    s_n = sign(monke_number("root"))
    if s_n == s_o: n += 1
    elif s_n == 0:
        done = True
        break
    else:
        n -= 1
        break

x = 10 ** n
while not done:
    m_n = dict(m_st)    
    x_n = x + 10 ** n
    #print(x_n)
    m_n["humn"] = x_n
    s_n = sign(monke_number("root"))
    if s_n == s_o: x = x_n
    elif s_n == 0: done = True
    else: n -= 1
    
print("P2:", x_n)
