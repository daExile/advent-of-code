file = open("10.txt", "r")

cmd = []
for line in file:
    s = line.strip().split()
    if s[0] == "noop": cmd.append([s[0]])
    else:
        a, b = s[0], int(s[1])
        cmd.append([a, b])
file.close()

X = 1
n, N = 0, 0
cps = [20, 60, 100, 140, 180, 220]
sigstr = 0
out = ""
while n < len(cmd):
    cy = 1 if cmd[n][0] == "noop" else 2
    for i in range(cy):
        if X-1 <= (N % 40) <= X+1: out += "#"
        else: out += "."
        N += 1
        if N in cps: sigstr += N * X
    if cmd[n][0] == "addx": X += cmd[n][1]
    n += 1

print("P1 answer:", sigstr)
for i in range(0, len(out), 40):
    print(out[i:i+39])
