import copy
bootcopy = open("08.txt", "r")
code = []
for line in bootcopy:
    cmd = {}
    t = line.strip().split(" ")
    cmd["cmd"] = t[0]    
    cmd["mod"] = int(t[1])
    cmd["trn"] = 0
    code.append(cmd)

def loop_or_die(mess):
    for cmd in mess: cmd["trn"] = 0
    curr = 0
    acc = 0
    turn = 1
    # print(mess)
    while True:
        if curr >= len(code):
            print("Correctly terminates! Acc =", acc)
            return True
        elif mess[curr]["trn"] > 0:
            print("Still loops at turn", turn)
            return False
        else:
            mess[curr]["trn"] = turn
            turn += 1
            if mess[curr]["cmd"] == "nop": curr += 1
            elif mess[curr]["cmd"] == "acc":
                acc += mess[curr]["mod"]
                curr += 1
            else:
                curr += mess[curr]["mod"]

curr = 0
acc = 0
turn = 1
yay = False
while not yay: #louder!
    mess = {}
    # print(code[curr])
    if code[curr]["cmd"] != "acc":
        print("Let's try line", curr, "-", code[curr]["cmd"], code[curr]["mod"])
        if code[curr]["cmd"] == "jmp":
            code[curr]["cmd"] = "nop"
            mess = copy.deepcopy(code)
            code[curr]["cmd"] = "jmp"
        elif code[curr]["cmd"] == "nop":
            code[curr]["cmd"] = "jmp"
            mess = copy.deepcopy(code)
            code[curr]["cmd"] = "nop"
        yay = loop_or_die(mess)

    code[curr]["trn"] = turn
    turn += 1
    if code[curr]["cmd"] == "nop": curr += 1
    elif code[curr]["cmd"] == "acc":
        acc += code[curr]["mod"]
        curr += 1
    else:
        curr += code[curr]["mod"]

print("Yay!")
