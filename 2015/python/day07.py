file = open("07.txt", "r")

circuit = {}
c_data = {}
for line in file:
    s = line.strip()
    code, wire = s.split(" -> ")
    c_parse = code.split()

    if len(c_parse) == 1:
        circuit[wire] = {"cmd": None, "o1": c_parse[0]}
    elif len(c_parse) == 2:
        circuit[wire] = {"cmd": "NOT", "o1": c_parse[1]}
    else:
        circuit[wire] = {"cmd": c_parse[1], "o1": c_parse[0], "o2": c_parse[2]}

def get_wire(wire):
    global circuit, c_data
    if wire in c_data: return c_data[wire]
    w = circuit[wire]
    #print(wire)
    
    if not w["cmd"]:
        if w["o1"].isdecimal(): signal = int(w["o1"])
        else: signal = get_wire(w["o1"])
    elif w["cmd"] == "NOT":
        signal = 65535 - get_wire(w["o1"])
    else:
        if w["cmd"] == "RSHIFT":
            signal = get_wire(w["o1"]) >> int(w["o2"])
        elif w["cmd"] == "LSHIFT":
            signal = (get_wire(w["o1"]) << int(w["o2"])) % 65536
        else:
            a = int(w["o1"]) if w["o1"].isdecimal() else get_wire(w["o1"])
            b = int(w["o2"]) if w["o2"].isdecimal() else get_wire(w["o2"])
            if w["cmd"] == "OR": signal = a | b
            else: signal = a & b
    c_data[wire] = signal
    return signal

answer = get_wire("a")
print("Part 1: Wire \'a\' signal:", answer)
#setting wire 'b' to result and resetting the rest
c_data = {"b": answer}
answer = get_wire("a")
print("Part 2: Wire \'a\' signal:", answer)
