local map = {}
for line in io.lines("../__in/16.txt") do
    local row = {}; for tile in string.gmatch(line, ".") do table.insert(row, tile) end
    table.insert(map, row) end

local r_max, c_max = #map, #map[1]

local function simulate(rays)
    local energy = {}
    local function ray_check(ray)
        if map[ray[1]] and map[ray[1]][ray[2]] then
            if not energy[ray[1]] or not energy[ray[1]][ray[2]] then return true
            elseif energy[ray[1]][ray[2]][ray[3] + 2 * ray[4]] then return false end
            return true end
        return false end
    
    while #rays > 0 do
        local rays_new = {}
        for _, ray in ipairs(rays) do
            if ray_check(ray) then
                if not energy[ray[1]] then energy[ray[1]] = {} end
                if not energy[ray[1]][ray[2]] then energy[ray[1]][ray[2]] = {} end
                energy[ray[1]][ray[2]][ray[3] + 2 * ray[4]] = true
            
                local tile = map[ray[1]][ray[2]]
                if tile == "." then table.insert(rays_new, {ray[1] + ray[3], ray[2] + ray[4], ray[3], ray[4]})
                elseif tile == "|" then
                    if ray[4] == 0 then table.insert(rays_new, {ray[1] + ray[3], ray[2] + ray[4], ray[3], ray[4]})
                    else
                        table.insert(rays_new, {ray[1] + 1, ray[2], 1, 0})
                        table.insert(rays_new, {ray[1] - 1, ray[2], -1, 0}) end
                elseif tile == "-" then
                    if ray[3] == 0 then table.insert(rays_new, {ray[1] + ray[3], ray[2] + ray[4], ray[3], ray[4]})
                    else
                        table.insert(rays_new, {ray[1], ray[2] + 1, 0, 1})
                        table.insert(rays_new, {ray[1], ray[2] - 1, 0, -1}) end
                elseif tile == "/" then 
                    local dr, dc = -ray[4], -ray[3]
                    table.insert(rays_new, {ray[1] + dr, ray[2] + dc, dr, dc})
                elseif tile == "\\" then
                    local dr, dc = ray[4], ray[3]
                    table.insert(rays_new, {ray[1] + dr, ray[2] + dc, dr, dc}) end
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
    local x = simulate({{i, 1, 0, 1}})
    if i == 1 then print(string.format("Part 1: %d", x)) end
    if x > count_max then count_max = x end end
for i = 1, r_max do local x = simulate({{i, c_max, 0, -1}}); if x > count_max then count_max = x end end
for i = 1, c_max do local x = simulate({{1, i, 1, 0}}); if x > count_max then count_max = x end end
for i = 1, r_max do local x = simulate({{r_max, i, -1, 0}}); if x > count_max then count_max = x end end

print(string.format("Part 2: %d", count_max))