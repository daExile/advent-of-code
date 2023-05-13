data = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}
file = open("16.txt", "r")

sue_me = {}
for line in file:
    s = line[4:].strip()
    n, rest = s.split(": ", 1)
    rest = rest.split(", ")
    sue_me[n] = {}
    for item in rest:
        a, b = item.split(": ")
        sue_me[n][a] = int(b)
file.close()

def check(aunt):
    global data, sue_me
    for item, value in sue_me[aunt].items():
        if value != data[item]: return False
    return True

for aunt in sue_me:
    if check(aunt):
        valid_sue = aunt
        break

print("Part 1 answer: #{}".format(valid_sue))

def check_mod(aunt):
    global data, sue_me
    #print(aunt)
    for item, value in sue_me[aunt].items():
        #print(item, value)
        if item in ["cats", "trees"]:
            if value <= data[item]: return False
        elif item in ["pomeranians", "goldfish"]:
            if value >= data[item]: return False
        else:
            if value != data[item]: return False
    return True

valid_sue = None
for aunt in sue_me:
    if check_mod(aunt):
        valid_sue = aunt
        break

print("Part 2 answer: #{}".format(valid_sue))
