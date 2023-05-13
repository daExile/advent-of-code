#init 1M lights thing
lights = []
for i in range(1000):
    lights.append([0] * 1000)

def get_coords(begin, end):
    b = begin.split(",")
    e = end.split(",")
    x = [int(b[0]), int(e[0]) + 1]
    y = [int(b[1]), int(e[1]) + 1]
    return(x, y)

file = open("06.txt", "r")

for line in file:
    s = line.strip()
    if s.startswith("turn"):
        cmd, begin, _, end = s[5:].split()
        x, y = get_coords(begin, end)
        val = 1 if cmd == "on" else 0
        #print("Turn", cmd, x[0], y[0], "to", x[1]-1, y[1]-1)
        for i in range(x[0], x[1]):
            for j in range(y[0], y[1]):
                lights[i][j] = val
    else:
        _, begin, _, end = s.split()
        x, y = get_coords(begin, end)
        #print("Toggle", x[0], y[0], "to", x[1]-1, y[1]-1)
        for i in range(x[0], x[1]):
            for j in range(y[0], y[1]):
                if lights[i][j] == 0: lights[i][j] = 1
                else: lights[i][j] = 0

file.close()

l_count = 0
for row in lights: l_count += row.count(1)
print("Lights on:", l_count)
