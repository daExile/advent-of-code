p = []
pdata = open("02.txt", "r")
for line in pdata:
    tmp = line.split()
    tmp2 = tmp[0].split("-")
    p.append({"pass": tmp[2], "policy": tmp[1][0], "p1": int(tmp2[0]), "p2": int(tmp2[1])})
pdata.close()

# print(len(p))

bad = 0
report_none = "Password {} has no matches of {} on key positions ({}:{}, {}:{})."
report_both = "Password {} has two matches of {} on key positions ({}, {})."
for pswd in p:
    key = pswd["policy"]
    p1 = pswd["pass"][pswd["p1"]-1]
    p2 = pswd["pass"][pswd["p2"]-1]
    if (p1 == key and p2 == key):
        bad += 1
        print(report_both.format(pswd["pass"], key, pswd["p1"], pswd["p2"]))
    elif (p1 != key and p2 != key):
        bad += 1
        print(report_none.format(pswd["pass"], key, pswd["p1"], p1, pswd["p2"], p2))

print("Total bad passwords:", bad)
print("Total valid passwords:", len(p)-bad)
