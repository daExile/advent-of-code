import re
file = open('21.txt', 'r')
init = 'abcdefgh'
#file = open('21_test.txt', 'r')
#init = "abcde"
debug = False

def swap(l, a, b):
    t = l[a]
    l[a] = l[b]
    l[b] = t
    return l

def rot(l, a):
    return l[a:] + l[:a]

p = list(init)
if debug: print(p)
for line in file:
    s = line.strip()
    if s.startswith('swap letter'):
        a, b = re.findall(r'letter (\w)', s)
        p = swap(p[:], p.index(a), p.index(b))
    elif s.startswith('swap position'):
        a, b = [int(x) for x in re.findall(r'position (\d)', s)]
        p = swap(p[:], a, b)
    elif s.startswith('rotate based'):
        a = p.index(s[-1])
        n = 1 + a if a < 4 else 2 + a
        p = rot(p[:], -(n % len(p)))
    elif s.startswith('rotate'):
        t = re.search(r'(left|right) (\w)', s).group().split()
        a = -int(t[1]) if t[0] == "right" else int(t[1])
        p = rot(p[:], a)
    elif s.startswith('reverse'):
        a, b = [int(x[i]) for i in range(2) for x in re.findall(r'(\d) through (\d)', s)]
        t = p[a:b+1]
        p_l = p[:a]
        p_r = p[b+1:]
        t = t[::-1]
        p = p_l + t + p_r
    else:
        a, b = [int(x) for x in re.findall(r'position (\d)', s)]
        t = p.pop(a)
        p.insert(b, t)
    if debug: print(p)
file.close()

print("Part 1 password:", "".join(p))

file = open('21.txt', 'r')
init = 'fbgdceah'
#init = 'bdfhgeca' #my result from part 1 as test case
#read all instructions and reverse list
instructions = []
for line in file:
    instructions.insert(0, line.strip())
file.close()
#unscrew code with some things mirrored
p = list(init)
if debug: print(p)
for line in instructions:
    s = line.strip()
    if s.startswith('swap letter'):
        a, b = re.findall(r'letter (\w)', s)
        p = swap(p[:], p.index(a), p.index(b))
    elif s.startswith('swap position'):
        a, b = [int(x) for x in re.findall(r'position (\d)', s)]
        p = swap(p[:], a, b)
    elif s.startswith('rotate based'):
        a = p.index(s[-1])
        for i in range(8):
            a_n = (1 + i) % len(p) if i < 4 else (2 + i) % len(p)
            if (i + a_n) % len(p) == a:
                p = rot(p[:], -(i - a) % len(p))
                break
    elif s.startswith('rotate'):
        t = re.search(r'(left|right) (\w)', s).group().split()
        a = -int(t[1]) if t[0] == "left" else int(t[1])
        p = rot(p[:], a)
    elif s.startswith('reverse'):
        a, b = [int(x[i]) for i in range(2) for x in re.findall(r'(\d) through (\d)', s)]
        t = p[a:b+1]
        p_l = p[:a]
        p_r = p[b+1:]
        t = t[::-1]
        p = p_l + t + p_r
    else:
        a, b = [int(x) for x in re.findall(r'position (\d)', s)]
        t = p.pop(b)
        p.insert(a, t)
    if debug: print(p)

print("Part 2 password:", "".join(p))
