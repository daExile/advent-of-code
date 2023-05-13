xmasdata = []
xmasstream = open("09.txt", "r")
for n in xmasstream:
    xmasdata.append(int(n))
xmasstream.close()

for n in range(25, len(xmasdata)):
    t = xmasdata[n]
    pre = xmasdata[n-25:n]
    pre.sort()
    # print(pre)
    a = 0
    b = 24
    r = []
    while (a < b):
        if pre[a] + pre[b] == t:
            # print(pre[a], "+", pre[b],"=", t)
            r = [pre[a], pre[b]]
            break
        elif pre[a] + pre[b] < t:
            a += 1
        else: b -= 1
    if r == []:
        print("Weakness sum:", t)
        break

for n in range(0,len(xmasdata)):
    chksum = 0
    chkdata = []
    for m in range(n, len(xmasdata)):
        chksum += xmasdata[m]
        chkdata.append(xmasdata[m])
        if chksum == t:
            print("Weakness sequence:", chkdata)
            chkdata.sort()
            print("Answer sum:", chkdata[0]+chkdata[-1])
        if chksum >= t:
            break
    if chksum == t:
        break
