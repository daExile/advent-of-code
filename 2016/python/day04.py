import string
file = open("04.txt", "r")

rooms = {}
for i, line in enumerate(file):
    s = line.strip()
    csum = s[-6:-1]
    name, r_id = s[:-7].rsplit("-", 1)
    rooms[i] = {"id": int(r_id), "name": name, "chksum": csum}

real_rooms = {}
a = 0
for r in rooms:
    n = rooms[r]["name"].replace("-", "")
    count = []
    for char in set(n):
        count.append([char, n.count(char)])
        count.sort(key = lambda x: x[0])
        count.sort(key = lambda x: x[1], reverse = True)
    check = "".join([x[0] for x in count[:5]])
    #print(r, count, check, rooms[r]["chksum"])
    if check == rooms[r]["chksum"]:
        real_rooms[r] = rooms[r]

print("Real rooms count:", len(real_rooms))
print("Real rooms ID sum:", sum([real_rooms[x]["id"] for x in real_rooms]))
print("\nNow to decipher names...")

for r in real_rooms:
    shift = real_rooms[r]["id"] % 26
    a = string.ascii_lowercase + "-"
    c = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] + " "
    decipher = str.maketrans(a, c)
    print("{}: {}".format(real_rooms[r]["id"], real_rooms[r]["name"].translate(decipher)))
