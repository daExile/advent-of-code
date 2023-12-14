local map, log = {}, {[0] = {}}

local function count_load(map)
    local score = 0
    for r = 1, #map do
        local d = #map - r + 1
        for c = 1, #map[1] do if map[r][c] == "O" then score = score + d end end end
        
    return score end

local function match(t, n) for i = 1, #t do if t[i] ~= log[n][i] then return false end end; return true end

local function spin(map, n)
    local r_max, c_max, cycle_length, target = #map, #map[1]
    for cycle = 1, n do
        for r = 1, r_max do     -- north
            for c = 1, c_max do
                if map[r][c] == "O" then
                local r_n = r - 1; while r_n > 0 and map[r_n][c] == "." do r_n = r_n - 1 end
                map[r][c] = "."; map[r_n + 1][c] = "O" end end end
        
        if cycle == 1 then print(string.format("Part 1: %d", count_load(map))) end
        
        for c = 1, c_max do     -- west
            for r = 1, r_max do
                if map[r][c] == "O" then
                local c_n = c - 1; while c_n > 0 and map[r][c_n] == "." do c_n = c_n - 1 end
                map[r][c] = "."; map[r][c_n + 1] = "O" end end end
        
        for r = r_max, 1, -1 do -- south
            for c = 1, c_max do
                if map[r][c] == "O" then
                local r_n = r + 1; while r_n <= r_max and map[r_n][c] == "." do r_n = r_n + 1 end
                map[r][c] = "."; map[r_n - 1][c] = "O" end end end
        
        for c = c_max, 1, -1 do -- east
            for r = 1, r_max do
                if map[r][c] == "O" then
                local c_n = c + 1; while c_n <= c_max and map[r][c_n] == "." do c_n = c_n + 1 end
                map[r][c] = "."; map[r][c_n - 1] = "O" end end end
        
        -- logging / checking / restoring correct final state
        local t = {}
        for i = 1, #map do table.insert(t, table.concat(map[i])) end
        local ok; for n = cycle - 1, 0, -1 do ok = match(t, n); if ok then cycle_length = cycle - n; break end end
        
        if not ok then log[cycle] = t
        else
            target = cycle - cycle_length + (n - cycle) % cycle_length
            
            for i = 1, #map do
                local map_row = {}
                for tile in string.gmatch(log[target][i], ".") do table.insert(map_row, tile) end
                map[i] = map_row end
            break end
    end
end

for line in io.lines("../__in/14.txt") do
    table.insert(log[0], line)
    local map_row = {}; for tile in string.gmatch(line, ".") do table.insert(map_row, tile) end
    table.insert(map, map_row) end

spin(map, 1000000000)
print(string.format("Part 2: %d", count_load(map)))