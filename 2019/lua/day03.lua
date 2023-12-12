local deltas = {["U"] = {0, 1}, ["D"] = {0, -1}, ["L"] = {-1, 0}, ["R"] = {1, 0}}

local input, grid, x_closest, x_shortest = {}, {}
for line in io.lines("../__in/03.txt") do table.insert(input, line) end

local x, y, step = 0, 0, 0  -- wire1 to grid
for segment in string.gmatch(input[1], "([UDLR]%d+)") do
    local dir, n = string.match(segment, "([UDLR])(%d+)")
    local dx, dy = deltas[dir][1], deltas[dir][2]
    
    for i = 1, tonumber(n) do
        x, y, step = x + dx, y + dy, step + 1
        
        if not grid[y] then grid[y] = {} end
        if not grid[y][x] then grid[y][x] = step end
    end end

x, y, step = 0, 0, 0        -- wire2 matching
for segment in string.gmatch(input[2], "([UDLR]%d+)") do
    local dir, n = string.match(segment, "([UDLR])(%d+)")
    local dx, dy = deltas[dir][1], deltas[dir][2]
    
    for i = 1, tonumber(n) do
        x, y, step = x + dx, y + dy, step + 1
        
        if grid[y] and grid[y][x] then
            if not x_closest or math.abs(x) + math.abs(y) < x_closest then x_closest = math.abs(x) + math.abs(y) end
            if not x_shortest or step + grid[y][x] < x_shortest then x_shortest = step + grid[y][x] end
    end end end

print(string.format("Part 1: %d", x_closest))
print(string.format("Part 2: %d", x_shortest))