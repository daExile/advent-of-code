local function comp(b1, b2) return b1.z1 < b2.z1 end

local bricks = {}
for line in io.lines("../__in/22.txt") do
    local xyz = {}
    for n in string.gmatch(line, "([%d]+)") do table.insert(xyz, tonumber(n)) end
    
    table.insert(bricks, {x1 = xyz[1], x2 = xyz[4], y1 = xyz[2], y2 = xyz[5], z1 = xyz[3], z2 = xyz[6], sup_by = {}, sups = {}})
end

table.sort(bricks, comp)

local floor = {}
for id, b in ipairs(bricks) do   -- very primitive stacking by checking each tile, performs fine, so be it
    local z_support, supported_by = 0, {}
    for x = b.x1, b.x2 do
        for y = b.y1, b.y2 do
            if not floor[x] then floor[x] = {} end; if not floor[x][y] then floor[x][y] = {} end
            local z = floor[x][y][1]; if z and z > z_support then z_support = z end end end
            
    b.z1, b.z2 = z_support + 1, b.z2 - b.z1 + z_support + 1
    for x = b.x1, b.x2 do
        for y = b.y1, b.y2 do
            if floor[x][y][1] == z_support then supported_by[floor[x][y][2]] = true end
            floor[x][y] = {b.z2, id} end end
    
    for k, _ in pairs(supported_by) do table.insert(bricks[k].sups, id); table.insert(bricks[id].sup_by, k) end
end

local quickened_disintegrate = 0
for _, b in ipairs(bricks) do
    if #b.sups == 0 then quickened_disintegrate = quickened_disintegrate + 1
    else
        local safe = 1
        for _, b_above in ipairs(b.sups) do if #bricks[b_above].sup_by == 1 then safe = 0 end end
        quickened_disintegrate = quickened_disintegrate + safe
    end
end

local maximised_disintegrate = 0
for id = 1, #bricks do
    local goners, goners_set, check = {id}, {[id] = true}, {}
    for _, b_above in ipairs(bricks[id].sups) do table.insert(check, b_above) end
    
    while #check > 0 do
        local recheck = {}
        
        for _, b in ipairs(check) do
            local not_safe = true
            for _, support in ipairs(bricks[b].sup_by) do if not goners_set[support] then not_safe = false end end
            
            if not_safe and not goners_set[b] then  -- check for bricks sent to recheck more than once
                table.insert(goners, b)
                goners_set[b] = true
                
                for _, b_above in ipairs(bricks[b].sups) do table.insert(recheck, b_above) end
            end
        end
        check = recheck
    end
    
    maximised_disintegrate = maximised_disintegrate + (#goners - 1)
end

print(string.format("Part 1: %d", quickened_disintegrate))
print(string.format("Part 2: %d", maximised_disintegrate))