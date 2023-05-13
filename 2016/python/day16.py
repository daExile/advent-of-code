#input
a = input("Puzzle input: ")
#desired length
d1 = 272
d2 = 35651584

#generate string
def get_data(a, d):
    r = str.maketrans("01", "10")
    while len(a) < d:
        b = a[::-1].translate(r)
        a = a + "0" + b
    return a

def get_chksum(a, d):
    c = ""
    while len(c) % 2 == 0:
        if not c:
            for i in range(0, d, 2):
                c += "1" if a[i] == a[i+1] else "0"
        else:
            c_next = ""
            for i in range(0, len(c), 2):
                c_next += "1" if c[i] == c[i+1] else "0"
            c = c_next
    return c
        
print("Disk size: {}, checksum: {}".format(d1, get_chksum(get_data(a, d1), d1)))
print("Disk size: {}, checksum: {}".format(d2, get_chksum(get_data(a, d2), d2)))
