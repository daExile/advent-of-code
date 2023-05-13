rules = [] # {"colour":"x", "contents":[]}

def count_bag_contents(colour, rules):
    total = 0
    for rule in rules:
        if rule["colour"] == colour:
            for i in range(0, len(rule["contents"]), 2):
                count = rule["contents"][i+1]
                total += count
                total += count * count_bag_contents(rule["contents"][i], rules)
            break
    return total

rulebook = open("07.txt", "r")
for line in rulebook:
    rule = {}
    t = line.strip(".\n").split("contain")

    rule["colour"] = t[0][:-6]
    
    rule["contents"] = []
    t = t[1].split(",")
    for item in t:
        if item.find("no other") == -1:
            item = item.strip()
            a = item.find(" ")
            b = item.find("bag")
            count = int(item[0:a])
            item = item[a+1:b-1]
            rule["contents"].append(item)
            rule["contents"].append(count)

    rules.append(rule)

# for rule in rules: print(rule)
yay = count_bag_contents("shiny gold", rules)

print("Total number of bags in yours:", yay)
