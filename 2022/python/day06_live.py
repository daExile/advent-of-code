file = open("06.txt", "r")
import re

s = file.read().strip()
file.close()
#s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for i, c in enumerate(s):
    a = set(s[i:i+4])
    if len(a) == 4:
        print("First packet marker:", i+4)
        break

for i, c in enumerate(s):
    a = set(s[i:i+14])
    if len(a) == 14:
        print("First message marker:", i+14)
        break
