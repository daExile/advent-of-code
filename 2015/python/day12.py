file = open("12.txt", "r")
doc = file.read()
file.close()
#doc = "{1,{\"c\":\"red\",\"b\":2},3,{\"c\":\"blue\",\"b\":1},8,{\"c\":\"red\",\"b\":4},9}"
#doc = "{6,{5,{4,{3,{2:\"red\",{1}}}}}}"

doc_n = ""
for c in doc:
    if c not in "-0123456789": doc_n += " "
    else: doc_n += c

numbers = doc_n.split()
total = 0
for i in numbers: total += int(i.strip())

print("Part 1 answer:", total)

doc_less_red = ""
#let's just parse it for reds first
def red_obj(doc):
    doc_return = "{"
    doc_rest = doc[1:]
    i = 0
    while doc_rest[i] != "}":
        if doc_rest[i] == "{":
            a, b = red_obj(doc_rest[i:])

            doc_return += a[:]
            doc_rest = b[:]
            i = 0
        elif doc_rest[i] == "[":
            a, b = red_arr(doc_rest[i:])

            doc_return += a[:]
            doc_rest = b[:]
            i = 0
        else:
            doc_return += doc_rest[i]
            i += 1
    #print(doc_r)
    if "red" in doc_return: return("{}", doc_rest[i+1:])
    else: return(doc_return + "}", doc_rest[i+1:])

def red_arr(doc):
    doc_return = "["
    doc_rest = doc[1:]
    i = 0
    while doc_rest[i] != "]":
        if doc_rest[i] == "{":
            a, b = red_obj(doc_rest[i:])

            doc_return += a[:]
            doc_rest = b[:]
            i = 0
        elif doc_rest[i] == "[":
            a, b = red_arr(doc_rest[i:])

            doc_return += a[:]
            doc_rest = b[:]
            i = 0
        else:
            doc_return += doc_rest[i]
            i += 1
    #print(doc_r)
    return(doc_return.replace("red", "   "), doc_rest[i+1:])

while doc:
    if doc[0] == "[":
        a, b = red_arr(doc)
        doc_less_red += a
        doc = b[:]
    elif doc[0] == "{":
        a, b = red_obj(doc)
        doc_less_red += a
        doc = b[:]
    else:
        doc_less_red += doc[0]
        doc = doc[1:]
        
#now try if it works, it still needs edge case checks but maybe it works as is
#*lazy horse noises*
doc_n = ""
for c in doc_less_red:
    if c not in "-0123456789": doc_n += " "
    else: doc_n += c

#print(doc_less_red)
numbers = doc_n.split()
total = 0
for i in numbers: total += int(i.strip())

print("Part 2 answer:", total)
