p = []
pdata = open("02.txt", "r")
for line in pdata:
    tmp = line.split()
    tmp2 = tmp[0].split("-")
    p.append({"pass": tmp[2], "policy": tmp[1][0], "lower": int(tmp2[0]), "upper": int(tmp2[1])})
pdata.close()

# print(len(p))

bad = 0
report = "Password {} has {} \"{}\" instead of {}-{}."
for pswd in p:
    c = pswd["pass"].count(pswd["policy"])
    if c < pswd["lower"] or c > pswd["upper"]:
        bad += 1
        print(report.format(pswd["pass"], c, pswd["policy"], pswd["lower"], pswd["upper"]))

print("Total bad passwords:", bad)
print("Total valid passwords:", len(p)-bad)
