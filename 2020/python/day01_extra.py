reportdata = []
report = open("01.txt", "r")
for n in report:
    reportdata.append(int(n))
report.close()

reportdata.sort()

# print(reportdata)
for a in range(0, len(reportdata)):
    for b in range(a+1, len(reportdata)):
        for c in range(b+1, len(reportdata)):
            t = reportdata[a] + reportdata[b] + reportdata[c]
            print(reportdata[a], "+", reportdata[b], "+", reportdata[c], "=", t)
            if t == 2020:
                print("n1:", reportdata[a])
                print("n2:", reportdata[b])
                print("n3:", reportdata[c])
                print("Answer:", reportdata[a]*reportdata[b]*reportdata[c])
            if t >= 2020: break
        if t >= 2020: break
    if t == 2020: break
