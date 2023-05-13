rounds = 100
#init = "389125467" #test example
init = input("Puzzle input: ")

cups = init
#for i in range(len(init)):
#    cups.append(int(init[i]))
    
#print(cups)

for i in range(rounds):
    dest = int(cups[0]) - 1 if int(cups[0]) > 1 else 9
    pick = cups[1:4]
    cups = cups[0] + cups[4:]
    
    while str(dest) not in cups:
        dest = dest - 1 if dest > 1 else 9
        
    j = cups.find(str(dest))
    #print(cups, dest, j)
    cups = cups[:j + 1] + pick + cups[j + 1:]   #insert pick
    cups = cups[1:] + cups[0]               #shift cups
    print("Round", i + 1, "- Cups:", cups)

j = cups.find("1")
print("Part 1 answer:", cups[j + 1:] + cups[:j])
