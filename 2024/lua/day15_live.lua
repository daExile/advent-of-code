local input = io.lines("../__in/15.txt")
local map1, robot1, map2, robot2 = {}, {}, {}, {}
local dirs = {["^"] = {r = -1, c = 0}, [">"] = {r = 0, c = 1}, ["v"] = {r = 1, c = 0}, ["<"] = {r = 0, c = -1}}

local gps_sum1, gps_sum2 = 0, 0

local r = 0
for line in input do
    if #line == 0 then break end
    
    r = r + 1; local c, map1_row, map2_row = 0, {}, {}
    for tile in line:gmatch(".") do
        c = c + 1
        
        -- part 1
        if tile == "@" then robot1 = {r = r, c = c}; table.insert(map1_row, ".")
        else table.insert(map1_row, tile) end
        
        -- part 2
        if tile == "@" then robot2 = {r = r, c = 2 * c - 1}; table.insert(map2_row, "."); table.insert(map2_row, ".")
        elseif tile == "O" then table.insert(map2_row, "["); table.insert(map2_row, "]")
        else table.insert(map2_row, tile); table.insert(map2_row, tile) end
    end
    
    table.insert(map1, map1_row); table.insert(map2, map2_row)
end

local moves = ""
for line in input do moves = moves .. line end

for m in moves:gmatch(".") do
    local d = dirs[m]
    
    -- part 1
    local next_tile = map1[robot1.r + d.r][robot1.c + d.c]
    
    if next_tile == "." then
        robot1.r, robot1.c = robot1.r + d.r, robot1.c + d.c
    elseif next_tile == "O" then
        local t = {r = robot1.r + d.r, c = robot1.c + d.c}
        
        while map1[t.r][t.c] == "O" do t.r, t.c = t.r + d.r, t.c + d.c end
        
        if map1[t.r][t.c] == "." then
            map1[robot1.r + d.r][robot1.c + d.c], map1[t.r][t.c] = ".", "O"
            robot1.r, robot1.c = robot1.r + d.r, robot1.c + d.c
        end
    end
    
    -- part 2
    next_tile = map2[robot2.r + d.r][robot2.c + d.c]
    
    if next_tile == "." then
        robot2.r, robot2.c = robot2.r + d.r, robot2.c + d.c
    elseif next_tile ~= "#" then
        if d.r == 0 then
            local t = {r = robot2.r, c = robot2.c + d.c}
            
            while map2[t.r][t.c] ~= "." and map2[t.r][t.c] ~= "#" do t.c = t.c + d.c end
            
            if map2[t.r][t.c] == "." then
                for c = t.c, robot2.c + d.c, -d.c do map2[t.r][c] = map2[t.r][c - d.c] end
                map2[robot2.r][robot2.c], robot2 = ".", {r = robot2.r, c = robot2.c + d.c}
            end
        else
            -- i hope you like terrible junk for code
            local push, ptr, push_log = {{r = robot2.r, c = robot2.c}}, 1, {}
            
            while push[ptr] do
                local t = push[ptr]
                
                if map2[t.r + d.r][t.c] == "#" then
                    push = {} break
                elseif map2[t.r + d.r][t.c] == "[" then
                    if not push_log[(t.r + d.r) * 100 + t.c] then
                        table.insert(push, {r = t.r + d.r, c = t.c}); push_log[(t.r + d.r) * 100 + t.c] = true end
                    if not push_log[(t.r + d.r) * 100 + t.c + 1] then
                        table.insert(push, {r = t.r + d.r, c = t.c + 1}); push_log[(t.r + d.r) * 100 + t.c + 1] = true end
                elseif map2[t.r + d.r][t.c] == "]" then
                    if not push_log[(t.r + d.r) * 100 + t.c - 1] then
                        table.insert(push, {r = t.r + d.r, c = t.c - 1}); push_log[(t.r + d.r) * 100 + t.c - 1] = true end
                    if not push_log[(t.r + d.r) * 100 + t.c] then
                        table.insert(push, {r = t.r + d.r, c = t.c}); push_log[(t.r + d.r) * 100 + t.c] = true end
                end
                
                ptr = ptr + 1
            end
            
            for i = #push, 2, -1 do
                local t = push[i]; map2[t.r + d.r][t.c], map2[t.r][t.c] = map2[t.r][t.c], "."
            end
            
            if #push > 0 then robot2 = {r = robot2.r + d.r, c = robot2.c} end
        end
    end
end

for r, row in ipairs(map1) do
    for c, tile in ipairs(row) do gps_sum1 = gps_sum1 + (tile == "O" and ((r - 1) * 100 + (c - 1)) or 0) end
end
print(string.format("Part 1: %d", gps_sum1))

for r, row in ipairs(map2) do
    for c, tile in ipairs(row) do gps_sum2 = gps_sum2 + (tile == "[" and ((r - 1) * 100 + (c - 1)) or 0) end
end
print(string.format("Part 2: %d", gps_sum2))