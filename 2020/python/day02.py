p = []
pdata = open("02.txt", "r")
for line in pdata:
    tmp = line.split()
    tmp2 = tmp[0].split("-")
    p.append({"pass": tmp[2], "policy": tmp[1][0], "p1": int(tmp2[0]), "p2": int(tmp2[1])})
pdata.close()

bad = 0
for pswd in p:
    c = pswd["pass"].count(pswd["policy"])
    if c < pswd["p1"] or c > pswd["p2"]:
        bad += 1

print("Part 1:", len(p)-bad)

bad = 0
for pswd in p:
    key = pswd["policy"]
    p1 = pswd["pass"][pswd["p1"]-1]
    p2 = pswd["pass"][pswd["p2"]-1]
    if (p1 == key and p2 == key):
        bad += 1
    elif (p1 != key and p2 != key):
        bad += 1

print("Part 2:", len(p)-bad)
