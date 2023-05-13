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
    print(reportdata[a], "+", reportdata[b],"=", t)
    if t == 2020: break
    elif t < 2020:
        a += 1
    else: b -= 1

print("n1:", reportdata[a])
print("n2:", reportdata[b])
print("Answer:", reportdata[a]*reportdata[b])
