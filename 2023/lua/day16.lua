local map, dirs = {}, {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
for line in io.lines("../__in/16.txt") do
    local row = {}; for tile in string.gmatch(line, ".") do table.insert(row, tile) end
    table.insert(map, row) end

local r_max, c_max = #map, #map[1]

local function simulate(rays)
    local energy = {}
    local function ray_check(r)
        if map[r[1]] and map[r[1]][r[2]] then
            if not energy[r[1]] or not energy[r[1]][r[2]] or not energy[r[1]][r[2]][r[3]] then return true end end
        return false end
    
    while #rays > 0 do
        local rays_new = {}
        for _, ray in ipairs(rays) do
            if ray_check(ray) then
                if not energy[ray[1]] then energy[ray[1]] = {} end
                if not energy[ray[1]][ray[2]] then energy[ray[1]][ray[2]] = {} end
                
                local t = energy[ray[1]][ray[2]]
            
                local tile = map[ray[1]][ray[2]]
                if tile == "." then
                    if ray[3] % 2 == 0 then energy[ray[1]][ray[2]] = {t[1], true, t[3], true}
                    else energy[ray[1]][ray[2]] = {true, t[2], true, t[4]} end
                    
                    table.insert(rays_new, {ray[1] + dirs[ray[3]][1], ray[2] + dirs[ray[3]][2], ray[3]})   
                elseif tile == "|" then
                    energy[ray[1]][ray[2]] = {true, true, true, true}
                    
                    if ray[3] % 2 == 1 then table.insert(rays_new, {ray[1] + dirs[ray[3]][1], ray[2] + dirs[ray[3]][2], ray[3]})
                    else
                        table.insert(rays_new, {ray[1] + 1, ray[2], 1})
                        table.insert(rays_new, {ray[1] - 1, ray[2], 3}) end
                elseif tile == "-" then
                    energy[ray[1]][ray[2]] = {true, true, true, true}
                    
                    if ray[3] % 2 == 0 then table.insert(rays_new, {ray[1] + dirs[ray[3]][1], ray[2] + dirs[ray[3]][2], ray[3]})
                    else
                        table.insert(rays_new, {ray[1], ray[2] + 1, 2})
                        table.insert(rays_new, {ray[1], ray[2] - 1, 4}) end
                elseif tile == "/" then
                    if ray[3] == 1 or ray[3] == 2 then energy[ray[1]][ray[2]] = {true, true, t[3], t[4]}
                    else energy[ray[1]][ray[2]] = {t[1], t[2], true, true} end
                    
                    local dir_new = 5 - ray[3]
                    local dr, dc = dirs[dir_new][1], dirs[dir_new][2]
                    table.insert(rays_new, {ray[1] + dr, ray[2] + dc, dir_new})
                elseif tile == "\\" then
                    if ray[3] == 1 or ray[3] == 4 then energy[ray[1]][ray[2]] = {true, t[2], t[3], true}
                    else energy[ray[1]][ray[2]] = {t[1], true, true, t[4]} end
                
                    local dir_new = ray[3] + (ray[3] % 2 == 0 and -1 or 1)
                    local dr, dc = dirs[dir_new][1], dirs[dir_new][2]
                    table.insert(rays_new, {ray[1] + dr, ray[2] + dc, dir_new}) end
            end
        end
        rays = rays_new end

    local count = 0
    for r = 1, r_max do
        if energy[r] then
            for c = 1, c_max do if energy[r][c] then count = count + 1 end end end end
            
    return count end

local count_max = 0
-- loops in dumb manual way to save time on coding it :)
for i = 1, r_max do
    local x = simulate({{i, 1, 2}})
    if i == 1 then print(string.format("Part 1: %d", x)) end
    if x > count_max then count_max = x end end
for i = 1, r_max do local x = simulate({{i, c_max, 4}}); if x > count_max then count_max = x end end
for i = 1, c_max do local x = simulate({{1, i, 1}}); if x > count_max then count_max = x end end
for i = 1, r_max do local x = simulate({{r_max, i, 3}}); if x > count_max then count_max = x end end

print(string.format("Part 2: %d", count_max))