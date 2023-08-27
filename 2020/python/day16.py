from copy import deepcopy
file = open("16.txt", "r")
field_data = {}
stuff = []
for line in file:
    if line.strip() == "": break
    else:
        t = line.strip().split(":")
        t[1] = t[1].split(" or ")
        a = t[1][0].split("-")
        b = t[1][1].split("-")
        field_data[t[0]] = [(int(a[0]), int(a[1])), (int(b[0]), int(b[1]))]
t = file.readline().strip().split(",")
my = []
for n in t:
    my.append(int(n))

lb = ub = 500
for item in field_data:
    if field_data[item][0][0] < lb: lb = field_data[item][0][0]
    if field_data[item][1][1] > ub: ub = field_data[item][1][1]

rest = []
error_rate = 0
for line in file:
    t = line.strip().split(",")
    ticket = []
    for n in t:
        ticket.append(int(n))
    bad = False
    for n in ticket:
        if n < lb or n > ub:
            bad = True
            error_rate += n
    if not bad: rest.append(ticket)
file.close()

#time to find the fields out
def belongs(k, n):
    if (n >= field_data[k][0][0] and n <= field_data[k][0][1]) or (n >= field_data[k][1][0] and n <= field_data[k][1][1]): return True
    return False

cats = []
fields = []
for k in field_data:
    cats.append(k)

for x in range(0, 20):
    l = deepcopy(cats)
    for ticket in rest:
        for cat in l:
            if not belongs(cat, ticket[x]): l.remove(cat)
    fields.append(l)

# ohwell, of course it would not be simple sorting out
finally_ = [[] for _ in range(0, 20)]
#print(finally_)
for x in range(0, len(fields)):
    for f in range(0, len(fields)):
        if len(fields[f]) == 1:
            finally_[f].append(fields[f][0])
            t = fields[f][0]
            break
    for f in fields:
        if len(f) > 0: f.remove(t)

answer = 1
for i in range(0, 20):
    if finally_[i][0].startswith("departure"): answer *= my[i]

print("Part 1:", error_rate)
print("Part 2:", answer)
