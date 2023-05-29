stuff = require("stuff")

function redistribute(k)
    bank, banks[k] = banks[k], 0
    for i = 1, bank do
        k = k % #banks + 1
        banks[k] = banks[k] + 1
    end
end

banks = stuff.str2numtable(io.input("06.txt"):read())
io.close()

log = {}
cycle = 0
while true do
    cycle = cycle + 1
    redistribute(stuff.tablemaxindex(banks))
    state = table.concat(banks, " ")
    if log[state] then break else log[state] = cycle end
end

print(string.format("Part 1: %d", cycle))
print(string.format("Part 2: %d", cycle - log[state]))