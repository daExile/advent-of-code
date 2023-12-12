local input = io.open("../__in/25.txt", "r"):read("*a")

local rulepattern = "value is ([01]).*value ([01]).*to the ([%w]+).*state ([A-Z])"
local rules = {}
for rule in string.gmatch(input, "(In state [A-Z].-state [A-Z].-state [A-Z])") do
    local t = {}
    
    for block in string.gmatch(rule, "(If.-state [A-Z])") do
        local v_in, v_out, dir, nextstate, delta = string.match(block, rulepattern)
        if dir == "left" then delta = -1 else delta = 1 end
        
        t[tonumber(v_in)] = {tonumber(v_out), delta, string.byte(nextstate) - 64} end
    table.insert(rules, t)
end

local state, ptr, checksum, tape = string.byte(string.match(input, "Begin in state ([A-Z])")) - 64, 0, 0, {}
for i = 1, tonumber(string.match(input, "after ([%d]+) steps")) do
    local v = tape[ptr] or 0
    local t = rules[state][v]
    
    tape[ptr] = t[1]
    checksum, ptr, state = checksum + t[1] - v, ptr + t[2], t[3]
end

print(string.format("Answer: %d", checksum))