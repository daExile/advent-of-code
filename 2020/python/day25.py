file = open("25.txt")
c_pkey = int(file.readline())
d_pkey = int(file.readline())

#example
#c_pkey = 5764801
#d_pkey = 17807724

subj_n = 7

v = 1
c_loop = 0
while v != c_pkey:
    v = (v * subj_n) % 20201227
    c_loop += 1

v = 1
d_loop = 0
while v != d_pkey:
    v = (v * subj_n) % 20201227
    d_loop += 1

c_ekey, d_ekey = 1, 1
for i in range(d_loop):
    c_ekey = (c_ekey * c_pkey) % 20201227
#for i in range(c_loop):
#    d_ekey = (d_ekey * d_pkey) % 20201227
print("Answer:", c_ekey)
#print("D-Cloop run:", d_ekey)
