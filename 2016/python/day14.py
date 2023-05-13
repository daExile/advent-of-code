my_input = input("Puzzle input: ")
#my_input = "abc"
extra = True

import hashlib, re

def get_hash(a):
    return hashlib.md5(a.encode()).hexdigest()

def get_hash_extra(a):
    for i in range(2017):
        a = get_hash(a)
    return a

n = 0
hexdb = []
keys = []
p3 = r'([0-9a-f])\1{2,}'
while len(keys) < 64:
    if len(hexdb) < n + 1:
        if extra: h = get_hash_extra(my_input + str(n))
        else: h = get_hash(my_input + str(n))
        hexdb.append(h)
    m = re.findall(p3, hexdb[n])
    if m:
        p5 = r"(" + m[0] + r")\1{4,}"
        #print(n, p5)
        for k in range(n + 1, n + 1001):
            if len(hexdb) < k + 1:
                if extra: h = get_hash_extra(my_input + str(k))
                else: h = get_hash(my_input + str(k))
                hexdb.append(h)
                
            if re.findall(p5, hexdb[k]):
                keys.append(n)
                print("Getting keys... {:2}/64".format(len(keys)))
                break
    n += 1
    
print("Part {} answer:".format(2 if extra else 1), keys[63])
