mem = {}
mask = ""
program = open("14.txt", "r")
for line in program:
    t = line.split("=")
    if t[0].strip() == "mask": mask = t[1].strip()
    else:
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
            mem[int(a, 2)] = int(t[1].strip())
        #    else: m_t += mask[n]
        # if t[0][4:-2] in mem: print("Rewriting", t[0][4:-2])
        #mem[int(t[0][4:-2])] = int(m_t, 2)
    # print("Memory loaded:", len(mem))
program.close()

chksum = 0
for m, v in mem.items():
    chksum += v
    # print(m, v)
print("Checksum:", chksum)
