local stuff = require("stuff")

local input = stuff.str2alnumchartable(io.open("../__in/01.txt", "r"):read())
local inputlen = #input

local checksum1, checksum2 = 0, 0

for i = 1, inputlen do
    local str_a = input[i]
    local str_check1 = input[i % inputlen + 1]
    local str_check2 = input[(inputlen / 2 + i - 1) % inputlen + 1]
    
    if str_a == str_check1 then checksum1 = checksum1 + str_a end
    if str_a == str_check2 then checksum2 = checksum2 + str_a end
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))