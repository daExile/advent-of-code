local map, r, c, queue  = {}, 1, 1
for line in io.lines("../__in/21.txt") do
    local map_row = {}
    for tile in string.gmatch(line, ".") do
        if tile == "S" then tile = "."; queue = {{r, c}} end
        table.insert(map_row, tile)
        c = c + 1
    end
    r, c = r + 1, 1
    
    table.insert(map, map_row) end

-- as puzzle input seems to have empty edges and "axes", let's log steps when entering middle / corners / edge middle
local step_logs = {}
for i = -1, 1 do
    step_logs[i] = {}
    for j = -1, 1 do
        local step_map, queue = {[66 - 65 * i] = {[66 - 65 * j] = true}}, {{66 - 65 * i, 66 - 65 * j}}
        local step = (i == 0 and j == 0) and 0 or 1
        step_logs[i][j] = {}; step_logs[i][j][step] = 1
        
        while #queue > 0 do
            step = step + 1
            local queue_next, count = {}, 0
            
            for _, tile in ipairs(queue) do
                for _, dir in ipairs({{1, 0}, {0, 1}, {-1, 0}, {0, -1}}) do
                    r, c = tile[1] + dir[1], tile[2] + dir[2]
                    
                    if not step_map[r] then step_map[r] = {} end
                    if map[r] and map[r][c] == "." and not step_map[r][c] then
                        step_map[r][c], count = true, count + 1
                        table.insert(queue_next, {r, c}) end
                end
            end
            
            queue = queue_next
            if count > 0 then step_logs[i][j][step] = count + (step_logs[i][j][step - 2] or 0) end
        end
    end
end

local function plot_count(i, j, steps)
    local n = #step_logs[i][j]; return steps <= n and step_logs[i][j][steps] or step_logs[i][j][n - (steps - n) % 2] end

print(string.format("Part 1: %d", plot_count(0, 0, 64)))

local steps, n = 26501365, 0

-- now counting all the plots the elf can reach using step logs + number of steps it takes to reach each next map tile...
local count_p2 = plot_count(0, 0, steps)

for step = 66, 26501365, 131 do
    local x = steps - step + 1
    count_p2 = count_p2 + plot_count(1, 0, x) + plot_count(0, 1, x) + plot_count(-1, 0, x) + plot_count(0, -1, x) end

for step = 132, 26501365, 131 do
    local x = steps - step + 1; n = n + 1
    count_p2 = count_p2 + (plot_count(1, 1, x) + plot_count(1, -1, x) + plot_count(-1, 1, x) + plot_count(-1, -1, x)) * n end
        
print(string.format("Part 2: %.0f", count_p2))