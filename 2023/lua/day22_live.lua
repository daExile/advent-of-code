local bricks = {}

local function comp(b1, b2) return b1[5] < b2[5] end
for line in io.lines("../__in/22.txt") do
    local coords = {}
    for n in string.gmatch(line, "([%d]+)") do table.insert(coords, tonumber(n)) end
                        -- {x1, x2, y1, y2, z1, z2, supported by, supports}
    table.insert(bricks, {coords[1], coords[4], coords[2], coords[5], coords[3], coords[6], {}, {}})
end

table.sort(bricks, comp)

local floor = {}
for id, b in ipairs(bricks) do   -- very primitive stacking by checking each tile, performs fine, so be it
    local z_support, supported_by = 0, {}
    for x = b[1], b[2] do
        for y = b[3], b[4] do
            if not floor[x] then floor[x] = {} end; if not floor[x][y] then floor[x][y] = {} end
            local z = floor[x][y][1]; if z and z > z_support then z_support = z end end end
            
    b[5], b[6] = z_support + 1, b[6] - b[5] + z_support + 1
    for x = b[1], b[2] do
        for y = b[3], b[4] do
            if floor[x][y][1] == z_support then supported_by[floor[x][y][2]] = true end
            floor[x][y] = {b[6], id} end end
    
    for k, _ in pairs(supported_by) do table.insert(bricks[k][8], id); table.insert(bricks[id][7], k) end
end

local quickened_disintegrate = 0
for _, b in ipairs(bricks) do
    if #b[8] == 0 then quickened_disintegrate = quickened_disintegrate + 1
    else
        local safe = 1
        for _, b_sup in ipairs(b[8]) do if #bricks[b_sup][7] == 1 then safe = 0 end end
        quickened_disintegrate = quickened_disintegrate + safe
    end
end

print(string.format("Part 1: %d", quickened_disintegrate))

local maximised_disintegrate = 0
for id = 1, #bricks do
    local goners, goners_set, check = {id}, {[id] = true}, {}
    for _, b_next in ipairs(bricks[id][8]) do table.insert(check, b_next) end
    
    while #check > 0 do
        local recheck = {}
        
        for _, b in ipairs(check) do
            local not_safe = true
            for _, support in ipairs(bricks[b][7]) do if not goners_set[support] then not_safe = false end end
            
            if not_safe and not goners_set[b] then  -- check for bricks sent to recheck more than once
                table.insert(goners, b)
                goners_set[b] = true
                
                for _, b_next in ipairs(bricks[b][8]) do table.insert(recheck, b_next) end
            end
        end
        check = recheck
    end
    
    maximised_disintegrate = maximised_disintegrate + (#goners - 1)
end

print(string.format("Part 2: %d", maximised_disintegrate))