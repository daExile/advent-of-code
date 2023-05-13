#my input
c_pkey = int(input("Card public key: "))
d_pkey = int(input("Door public key: "))

#example
#c_pkey = 5764801
#d_pkey = 17807724

subj_n = 7

v = 1
c_loop = 0
print("Card public key:", c_pkey)
print("Getting card loop size...")
while v != c_pkey:
    v = (v * subj_n) % 20201227
    c_loop += 1
print("Loop", c_loop, "- value", v)

v = 1
d_loop = 0
print("\nDoor public key:", d_pkey)
print("\nGetting door loop size...")
while v != d_pkey:
    v = (v * subj_n) % 20201227
    d_loop += 1
print("Loop", d_loop, "- value", v)

print("\nGetting encryption key...")
c_ekey, d_ekey = 1, 1
for i in range(d_loop):
    c_ekey = (c_ekey * c_pkey) % 20201227
for i in range(c_loop):
    d_ekey = (d_ekey * d_pkey) % 20201227
print("C-Dloop run:", c_ekey)
print("D-Cloop run:", d_ekey)
