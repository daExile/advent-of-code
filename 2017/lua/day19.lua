local stuff = require("stuff")

local input = {}
for line in io.lines("19.txt") do table.insert(input, stuff.str2anychartable(line)) end

local dir, row, col = {1, 0}, 1
for i, v in ipairs(input[1]) do if v ~= " " then col = i break end end

local s, count = "", 0
repeat
    row = row + dir[1]; col = col + dir[2]; count = count + 1
    local tile = input[row][col]
    if tile == "+" then
        local check = stuff.turnleft(dir)
        if input[row + check[1]][col + check[2]] ~= " " then dir = check else dir = stuff.turnright(dir) end
    elseif string.match(tile, "%a") then s = s..tile end
until input[row][col] == " "

print(string.format("Part 1: %s", s))
print(string.format("Part 2: %d", count))