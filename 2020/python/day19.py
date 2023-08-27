def neocheck(rule, message, n):
    n_n = []
    if n:
        if isinstance(rb[rule][0][0], str):
            for i_n in n:
                if len(message) > i_n:
                    if message[i_n] == rb[rule][0][0]:
                        n_n.append(i_n + 1)
        else:
            for i_n in n:                       # entry array
                for i_r in rb[rule]:            # rule array variants
                    m = i_n                     # take one from entry array
                    m_t = [m]                   # make it a list

                    for j in i_r:
                        m_t_new = []
                        t_new = (neocheck(j, message, m_t))

                        if t_new: m_t_new += t_new
                        m_t = m_t_new
                        if not m_t: break

                    n_n += m_t

    n_n = list(set(n_n))         
    return(n_n)

def check(rule, message, n = 0):
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

    return(result, n)

file = open("19.txt", "r")
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

messages = [message.strip() for message in file]
file.close()

count = 0
for m in messages:
    mcheck = neocheck(0, m, [0])
    if mcheck:
        for i in mcheck:
            if i == len(m): count += 1
print("Part 1:", count)

rb[8] = [[42], [42, 8]]
rb[11] = [[42, 31], [42, 11, 31]]
count = 0
for m in messages:
    mcheck = neocheck(0, m, [0])
    if mcheck:
        for i in mcheck:
            if i == len(m): count += 1
print("Part 2:", count)
