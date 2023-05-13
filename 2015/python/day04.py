my_i = input("Puzzle input: ")

import hashlib

n = 0
hexd = "00001"
while hexd[:5] != "00000":
    n += 1
    hexd = hashlib.md5((my_i + str(n)).encode()).hexdigest()

print("\n5 zeroes!")
print("n =", n)
print("md5 check:", hexd)

while hexd[:6] != "000000":
    n += 1
    hexd = hashlib.md5((my_i + str(n)).encode()).hexdigest()

print("\n6 zeroes!")
print("n =", n)
print("md5 check:", hexd)
