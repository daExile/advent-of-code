my_input = input("Puzzle input: ")
#ayy i ruined part 1 code but anyway

import hashlib

n = 0
hexd = "00001"
password = "        "
while password.count(" ") > 0:
    while hexd[:5] != "00000":
        n += 1
        hexd = hashlib.md5((my_input + str(n)).encode()).hexdigest()
    pos = int(hexd[5], 16)
    char = hexd[6]
    hexd = "00001"
   
    if pos > 7 or password[pos] != " ": continue
    else:
        if pos == 7: password = password[:pos] + char
        else: password = password[:pos] + char + password[pos+1:]
        print("{}/8 found: [{}]".format(8 - password.count(" "), password))

print("Password:", password)
