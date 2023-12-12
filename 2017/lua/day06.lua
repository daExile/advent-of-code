local stuff = require("stuff")
local banks = stuff.str2numtable(io.input("../__in/06.txt"):read()); io.close()

local function redistribute(k)
    local bank = banks[k]; banks[k] = 0
    for i = 1, bank do
        k = k % #banks + 1
        banks[k] = banks[k] + 1
    end
end

local log, cycle, state = {}, 0
while true do
    cycle = cycle + 1
    redistribute(stuff.tablemaxindex(banks))
    state = table.concat(banks, " ")
    if log[state] then break else log[state] = cycle end
end

print(string.format("Part 1: %d", cycle))
print(string.format("Part 2: %d", cycle - log[state]))