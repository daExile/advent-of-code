mem_p1 = {}
mem_p2 = {}
mask = ""
program = open("14.txt", "r")
for line in program:
    t = line.split("=")
    if t[0].strip() == "mask": mask = t[1].strip()
    else:
        m = bin(int(t[1].strip()))[2:]
        if len(m) < 36:
            m = "0" * (36 - len(m)) + m
        m_t = ""
        for n in range(0,36):
            if mask[n] == "X": m_t += m[n]
            else: m_t += mask[n]
        mem_p1[int(t[0][4:-2])] = int(m_t, 2)

        addr = [bin(int(t[0][4:-2].strip()))[2:]]
        if len(addr[0]) < 36:
            addr[0] = "0" * (36 - len(addr[0])) + addr[0]
        # masking 0/1
        for n in range(0,36):
            if mask[n] == "1": addr[0] = addr[0][0:n] + "1" + addr[0][n+1:]
        # masking X
        for n in range(0,36):
            if mask[n] == "X":
                addr_iter = []
                for a in addr:
                    a = a[0:n] + "0" + a[n+1:]
                    addr_iter.append(a)
                    a = a[0:n] + "1" + a[n+1:]
                    addr_iter.append(a)
                addr = addr_iter

        for a in addr:
            mem_p2[int(a, 2)] = int(t[1].strip())
        
program.close()

chksum = 0
for m, v in mem_p1.items():
    chksum += v
print("Part 1:", chksum)

chksum = 0
for m, v in mem_p2.items():
    chksum += v
print("Part 2:", chksum)
