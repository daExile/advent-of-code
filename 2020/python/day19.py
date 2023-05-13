def neocheck(rule, message, n):
    #print("Checking rule", rule, ", n:", n)
    n_n = []
    if n:
        if isinstance(rb[rule][0][0], str):
            for i_n in n:
                if len(message) > i_n:
                    if message[i_n] == rb[rule][0][0]:
                        n_n.append(i_n + 1)
                        #print("yea")
                    #else: print("nay")
        else:
            for i_n in n:                       # entry array
                for i_r in rb[rule]:            # rule array variants
                    #print("Sub", i_r, "in rule", rule)
                    m = i_n                     # take one from entry array
                    m_t = [m]                   # make it a list
                    # print("m =", m)
                    for j in i_r:
                        m_t_new = []
                        #for t in m_t:           # check each item in list
                        t_new = (neocheck(j, message, m_t))
                            #print("t =", t)
                        if t_new: m_t_new += t_new
                        m_t = m_t_new
                        if not m_t: break
                    #if not t: break
                    n_n += m_t
                #print("n_n =", n_n)
    n_n = list(set(n_n))         
    return(n_n)

def check(rule, message, n = 0):
    # print("Checking rule", rule, ", n =", n)
    if isinstance(rb[rule][0][0], str):
        if len(message) <= n: result = False
        elif message[n] == rb[rule][0][0]:
            result = True
            n += 1
        else: result = False
    else:
        result = True
        for i in rb[rule]:
            m = n
            for j in i:
                result, n = check(j, message, n)
                if result == False: break
            if result == True: break
            else: n = m
    #print("Result:", result)
    return(result, n)

file = open("19_extra.txt", "r")
rb = {}
for line in file:
    if not line.strip(): break
    else:
        r = line.strip().split(":")
        t = r[1].split("|")
        rules = []
        for item in t:
            a = item.strip().split(" ")
            if a[0].isdecimal():
                b = []
                for a_i in a:
                    b.append(int(a_i))
                rules.append(b)
            else:
                rules.append(a[0].strip()[1])
        rb[int(r[0])] = rules
#print(rb)

count = 0
for message in file:
    m = message.strip()
    mcheck = neocheck(0, m, [0])
    #print("mcheck =", mcheck)
    if mcheck:
        for i in mcheck:
            if i == len(m): count += 1
    #print("Message:", m, ", check:", mcheck, ", len:", len(m))
file.close()
print("Valid count:", count)

