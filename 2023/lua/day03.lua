local grid = {}

local function get_number(row, col)
    local t, numstr = col, ""
    repeat t = t - 1 until not grid[row][t] or not(tonumber(grid[row][t])); t = t + 1
    while grid[row][t] and tonumber(grid[row][t]) do numstr = numstr .. grid[row][t]; t = t + 1 end
    return tonumber(numstr) end

local function nearby_numbers(row, col, part)
    local sum, count, ratio = 0, 0, 1
    for i = row - 1, row + 1 do
        local lastnum
        for j = col - 1, col + 1 do
            if tonumber(grid[i][j]) then
                x = get_number(i, j)
                if not lastnum then sum = sum + x; count = count + 1; ratio = ratio * x; lastnum = x end
            else lastnum = nil end
        end
    end
    
    if part ~= "*" or count ~= 2 then ratio = 0 end
    return sum, ratio end

for line in io.lines("../__in/03.txt") do
    local t = {}; for tile in string.gmatch(line, ".") do table.insert(t, tile) end
    table.insert(grid, t) end

local total, gear_total = 0, 0
for i, row in ipairs(grid) do
    for j, char in ipairs(row) do
        if not string.match(char, "[%d%.]") then
            t, g = nearby_numbers(i, j, char)
            total = total + t; gear_total = gear_total + g end end end

print(string.format("Part 1: %d", total))
print(string.format("Part 2: %d", gear_total))