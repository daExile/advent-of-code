file = open("03.txt", "r")
prios = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
si = []
rs = []
for line in file:
    rs.append(line.strip())
file.close()
print(len(rs))

for r in rs:
    st = []
    for i in range(int(len(r) / 2)):
        for j in range(int(len(r) / 2)):
            if r[i] == r[j + int(len(r)/2)]:
                st.append(r[i])
    si.append(st[0])
ptotal = 0
for item in si:
    ptotal += prios.index(item)
print(ptotal)

file = open("03.txt", "r")
bs = []
for i in range(0, len(rs), 3):
    s1 = set(rs[i])
    s2 = set(rs[i+1])
    s3 = set(rs[i+2])
    b = (s1 & s2) & s3
    bs.append(list(b)[0])
ptotal = 0
for item in bs:
    ptotal += prios.index(item)

print(ptotal)
