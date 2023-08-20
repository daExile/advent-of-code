local stuff = require("stuff")

local function getgrid()
    local grid, inputsize, row = {}
    for line in io.lines("22.txt") do
        if not inputsize then inputsize = #line; row = (inputsize - 1) / 2 end
    
        grid[row] = {}
        for i, v in ipairs(stuff.str2anychartable(line)) do
            if v == "#" then grid[row][i - (inputsize - 1) / 2 - 1] = v end end
        row = row - 1 end
    return grid end

local x, dx, y, dy, count, grid = 0, 0, 0, 1, 0, getgrid()
for i = 1, 10000 do
    if not grid[y] then grid[y] = {} end
    if not grid[y][x] then grid[y][x] = "#"; dx, dy = -dy, dx; count = count + 1
    else grid[y][x] = nil; dx, dy = dy, -dx end
    
    x, y = x + dx, y + dy end

print(string.format("Part 1: %d", count))

x, dx, y, dy, count, grid = 0, 0, 0, 1, 0, getgrid()
for i = 1, 10000000 do
    if not grid[y] then grid[y] = {} end
    if not grid[y][x] then grid[y][x] = "W"; dx, dy = -dy, dx
    elseif grid[y][x] == "W" then grid[y][x] = "#"; count = count + 1
    elseif grid[y][x] == "#" then grid[y][x] = "F"; dx, dy = dy, -dx
    else grid[y][x] = nil; dx, dy = -dx, -dy end
    
    x, y = x + dx, y + dy end

print(string.format("Part 2: %d", count))