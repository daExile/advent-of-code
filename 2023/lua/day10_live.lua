local tokens = {["|"] = { {-1, 0}, {1, 0} },
                ["-"] = { {0, -1}, {0, 1} },
                ["7"] = { {0, -1}, {1, 0} },
                ["F"] = { {1, 0}, {0, 1} },
                ["J"] = { {-1, 0}, {0, -1} },
                ["L"] = { {-1, 0}, {0, 1} },
                ["."] = {}}

local map, start, r, c = {}, {}, 1
for line in io.lines("../__in/10.txt") do
    local row = {}; c = 1
    for tile in string.gmatch(line, ".") do
        if tile == "S" then start = {r, c} end
        table.insert(row, tile); c = c + 1 end
        
    table.insert(map, row); r = r + 1 end

-- connect starting tile in a very clumsy check-and-match way
local tmp = {}
for _, dir in ipairs({{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) do
    t = map[start[1] + dir[1]][start[2] + dir[2]]
    if t then
        for _, v in ipairs(tokens[t]) do
            if dir[1] == -v[1] and dir[2] == -v[2] then table.insert(tmp, dir) end end end
end

for k, v in pairs(tokens) do
    if k ~= "." and tmp[1][1] == v[1][1] and tmp[1][2] == v[1][2] and tmp[2][1] == v[2][1] and tmp[2][2] == v[2][2] then
        map[start[1]][start[2]] = k end end

-- path this in an even worse way
local trace, step, to_check = {}, 0, {start}
local function add(r, c, step)
    if not trace[r] then trace[r] = {} end; if not trace[r][c] then trace[r][c] = step; return true end return false end

while #to_check > 0 do
    local t = {}
    for _, tile in ipairs(to_check) do
        if add(tile[1], tile[2], step) then
            for _, dirs in ipairs(tokens[map[tile[1]][tile[2]]]) do
                local r, c = tile[1] + dirs[1], tile[2] + dirs[2]
                if not trace[r] or not trace[r][c] then table.insert(t, {r, c}) end end end end
    
    to_check = t; if #t > 0 then step = step + 1 end
end

print(string.format("Part 1: %d", step))

-- alright, "can squeeze between pipes" needs some tricks, so just one direction to check, fuck optimisation for now
local r_min, r_max, c_min, c_max, inside_loop = 1, #map, 1, #map[1], 0
for r = 1, #map do
    for c = 1, #map[1] do
        if not trace[r] or not trace[r][c] then     -- find tile not marked by loop trace
            local pipe_down = 0                     -- pick any of two directions (i chose down as it's +1 for my setup)
            for x = 1, c - 1 do                     -- and now count all part-of-the-loop pipes going that direction
                if trace[r] and trace[r][x] then    -- between tile being checked and edge of the map.
                    if map[r][x] == "|" or map[r][x] == "7" or map[r][x] == "F" then pipe_down = pipe_down + 1 end end end
            if pipe_down % 2 == 1 then inside_loop = inside_loop + 1 end end end end
            
print(string.format("Part 2: %d", inside_loop))