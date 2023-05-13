import re

bs = {}
p = {}
o = {}

file = open("10.txt", "r")
for line in file:
    s = line.strip()
    if s.startswith("value"):
        v, b = [int(x) for x in re.findall("(\d+)", s)]
        try: bs[b].append(v)
        except KeyError: bs[b] = [v]
    else:
        b, v1, v2 = [int(x) for x in re.findall("(\d+)", s)]
        _, d1, d2 = re.findall("(output|bot)", s)
        p[b] = {"l": (d1, v1), "h": (d2, v2)}
file.close()

print("Looking for part 1 answer...")
chk = True
while chk:
    chk = False
    for b in list(bs.keys()):
        if len(bs[b]) == 2:
            chk = True
            bs[b].sort()
            #print(b, bs[b])
            if bs[b] == [17, 61]: print("Bot", b, "got to compare 61 and 17")
            if p[b]["l"][0] == "output": o[p[b]["l"][1]] = bs[b][0]
            else:
                try: bs[p[b]["l"][1]].append(bs[b][0])
                except KeyError: bs[p[b]["h"][1]] = [bs[b][0]]
            if p[b]["h"][0] == "output": o[p[b]["h"][1]] = bs[b][1]
            else:
                try: bs[p[b]["h"][1]].append(bs[b][1])
                except KeyError: bs[p[b]["h"][1]] = [bs[b][1]]
            del bs[b]
            break
    #print(bs, "\n")
print("\n")
for out in o:
    print("Output {}: {}".format(out, o[out]))
print("\nPart 2 answer:", o[0] * o[1] * o[2])
