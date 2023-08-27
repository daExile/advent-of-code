reportdata = []
report = open("01.txt", "r")
for n in report:
    reportdata.append(int(n))
report.close()

reportdata.sort()

# print(reportdata)
a = 0
b = len(reportdata)-1
while (a < b):
    t = reportdata[a]+reportdata[b]
    if t == 2020: break
    elif t < 2020:
        a += 1
    else: b -= 1

print("Part 1:", reportdata[a]*reportdata[b])

for a in range(0, len(reportdata)):
    for b in range(a+1, len(reportdata)):
        for c in range(b+1, len(reportdata)):
            t = reportdata[a] + reportdata[b] + reportdata[c]
            if t == 2020:
                print("Part 2:", reportdata[a]*reportdata[b]*reportdata[c])
            if t >= 2020: break
        if t >= 2020: break
    if t == 2020: break
