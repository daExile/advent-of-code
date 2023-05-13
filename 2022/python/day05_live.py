file = open("05.txt", "r")
import re
cm9001 = True

#what a fucking mess with regex that costed me a damn hour
stacks = [ [] for _ in range(10) ]
for line in file:
    s = line.rstrip()
    #print(s)    
    if not s: break
    elif "[" not in s: continue
    else:
        for i in range(0, len(s), 4):
            if s[i+1] != " ": stacks[int(i/4) + 1].append(s[i+1])
for i, st in enumerate(stacks):
    stacks[i] = stacks[i][::-1]

s2 = []
for s in stacks:
    s2.append("".join(s))
for st in range(1, 10):
    print("{}:".format(st), s2[st])
print("\n")

for line in file:
    s = line.strip()
    n, a, b = [int(x) for x in re.findall(r"[a-z\s]*(\d+)[a-z\s]*(\d+)[a-z\s]*(\d+)", s)[0]]
    #print(n, a, b)
    t = s2[a][-n:]
    s2[a] = s2[a][:-n]
    if not cm9001: t = t[::-1]
    s2[b] += t
    #print(s2[a], s2[b])
        #if stacks[a]:
         #   t = stacks[a].pop()
          #  stacks[b].append(t)
        
    #print("{} from {} to {}\n".format(n, a ,b))
    #for st in range(1, 10):
    #      print("{}:".format(st), s2[st])
    
top = ""
for st in range(1, 10):
    if s2[st]: top += s2[st][-1]
    else: top += "_"

print(top)
    
