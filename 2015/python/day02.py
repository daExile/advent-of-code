file = open("02.txt", "r")

paper_total = 0
ribbon_total = 0
for line in file:
    s = line.strip()
    d = []
    for subs in s.split("x"):
        d.append(int(subs))
    d.sort()
    paper_total += (3 * d[0] * d[1] + 2 * d[0] * d[2] + 2 * d[1] * d[2])
    ribbon_total += (2 * (d[0] + d[1]) + d[0] * d[1] * d[2])
file.close()

print("Paper needed:", paper_total)
print("Ribbon needed:", ribbon_total)
