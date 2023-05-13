mem = {}
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
        # if t[0][4:-2] in mem: print("Rewriting", t[0][4:-2])
        mem[int(t[0][4:-2])] = int(m_t, 2)
        
program.close()

print(mem)
chksum = 0
for m, v in mem.items():
    chksum += v
print("Checksum:", chksum)
