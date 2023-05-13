file = open("06.txt", "r")

count = []
for line in file:
    for i, char in enumerate(line.strip()):
        if len(count) < i + 1: count.append({})
        
        if char not in count[i]: count[i][char] = 1
        else: count[i][char] += 1

msg_mc = msg_lc = ""
for p in count:
    cc = [[c, p[c]] for c in p]
    cc.sort(key = lambda x: x[1], reverse = True)
    msg_mc += cc[0][0]
    msg_lc += cc[-1][0]

print("Error-corrected message, part 1:", msg_mc)
print("Error-corrected message, part 2:", msg_lc)
