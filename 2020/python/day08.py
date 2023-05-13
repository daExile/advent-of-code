bootcopy = open("08.txt", "r")
code = []
for line in bootcopy:
    cmd = {}
    t = line.strip().split(" ")
    cmd["cmd"] = t[0]    
    cmd["mod"] = int(t[1])
    cmd["trn"] = 0
    code.append(cmd)

curr = 0
acc = 0
turn = 1
while True: #hue hue hue hue
    print(code[curr])
    if code[curr]["trn"] > 0:
        print("Acc value:", acc)
        break
    else:
        code[curr]["trn"] = turn
        turn += 1
        if code[curr]["cmd"] == "nop": curr += 1
        elif code[curr]["cmd"] == "acc":
            acc += code[curr]["mod"]
            curr += 1
        else:
            curr += code[curr]["mod"]
