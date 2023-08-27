rules = [] # {"colour":"x", "contents":[colour, count, ...]}

def get_bag_rules(colour, rules):
    bag_rules = []
    for rule in rules:
        if colour in rule["contents"]:
            bag_rules.append(rule["colour"])
    if bag_rules != []:
        more_rules = []
        for item in bag_rules:
            more_rules.extend(get_bag_rules(item, rules))
        bag_rules.extend(more_rules)
    return set(bag_rules)

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

yay = get_bag_rules("shiny gold", rules)
print("Part 1:", len(yay))

yay = count_bag_contents("shiny gold", rules)
print("Part 2:", yay)
