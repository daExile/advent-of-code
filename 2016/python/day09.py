import re

#s = "X(8x2)(3x3)ABCY"
file = open("09.txt", "r")
s = file.read().strip()
file.close()

unpacked = ""
i = 0

while i < len(s):
    m = re.search("\(\d+x\d+\)", s[i:])
    if m:
        a, b = re.findall("\d+", m.group())
        unpacked += s[i:i+m.span()[0]] + s[i+m.span()[1]:i+m.span()[1] + int(a)] * int(b)
        i += m.span()[1] + int(a)
    else:
        unpacked += s[i:]
        i = len(s)

#print(unpacked)
print("Part 1 - unpacked length:", len(unpacked))

#ok let's figure out math for part 2

def get_ul(s):
    l = 0
    i = 0
    while i < len(s):
        m = re.search("\(\d+x\d+\)", s[i:])
        if m:
            a, b = [int(x) for x in re.findall("\d+", m.group())]
            l += m.span()[0] + get_ul(s[i+m.span()[1]:i+m.span()[1] + a]) * b
            i += m.span()[1] + a
        else:
            l += len(s[i:])
            i = len(s)
    return l

print("Part 2 - unpacked length:", get_ul(s))
