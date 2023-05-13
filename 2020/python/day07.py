rules = [] # {"colour":"x", "contents":[]}

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

rulebook = open("07.txt", "r")
for line in rulebook:
    rule = {}
    t = line.strip(".\n").split("contain")

    rule["colour"] = t[0][:-6]
    
    rule["contents"] = []
    t = t[1].split(",")
    for item in t:
        item = item.strip()
        a = item.find(" ")
        b = item.find("bag")
        item = item[a+1:b-1]
        if item != "no other": rule["contents"].append(item)

    rules.append(rule)

yay = get_bag_rules("shiny gold", rules)

print(yay)
print("Number or colours:", len(yay))
