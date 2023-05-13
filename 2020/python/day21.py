foods = []
i_all, a_all = [], []
file = open("21.txt", "r")
for line in file:
    f = {}
    if line.strip().endswith(")"):
        i, a = line.strip().split("(")
        f['ingred'] = i.strip().split(" ")
        f['allerg'] = a[8:-1].strip().replace(",","").split(" ")
    else:
        f['ingred'] = line.strip().split(" ")
        f['allerg'] = []
    for item in f['ingred']:
        if item not in i_all: i_all.append(item)
    if f['allerg']:
        for item in f['allerg']:
            if item not in a_all: a_all.append(item)
    foods.append(f)
file.close()

#print("All ingredients:", i_all)
#print("All allergens:", a_all)

#ok now some subpar list parsing
a_fil = {}
for a in a_all:
    i = i_all[:]
    for food in foods:
        if a in food['allerg']:
            i = list(set(i) & set(food['ingred']))
    a_fil[a] = i

a_match = {}
while a_fil:
    af_keys = list(a_fil.keys())
    for key in af_keys:
        if len(a_fil[key]) == 1:
            k = key
            break
    a_match[k] = a_fil.pop(key)
    af_keys = list(a_fil.keys())
    for key in af_keys:
        a_fil[key] = list(set(a_fil[key]) - set(a_match[k]))
print(a_match)

#let's count answer 1
a1 = 0
a_list = []
#keys = list(a_match.keys())
for key in a_match:
    a_list.append(a_match[key][0])
print(a_list)
for f in foods:
    a1 += len(set(f['ingred']) - set(a_list))
print("Part 1 answer:", a1)

a_keys = list(a_match.keys())
a_keys.sort()

#canonical dangerous ingredient list
cdil=""
for key in a_keys:
    cdil += a_match[key][0] +","
print("Part 2 answer:", cdil[:-1])
