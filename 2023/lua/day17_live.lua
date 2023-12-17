local map = {}
for line in io.lines("../__in/17.txt") do
    local row = {}; for tile in string.gmatch(line, ".") do table.insert(row, tonumber(tile)) end
    table.insert(map, row) end

local r_tgt, c_tgt, dirs = #map, #map[1], {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

local function compare(t1, t2)
    return t1[3] + t1[6] < t2[3] + t2[6] or (t1[3] + t1[6] == t2[3] + t2[6] and t1[6] < t2[6]) end

local current, n, log, path_heat_loss = {{1, 1, 0, 0, 0, 0}}, 0, {}
while not path_heat_loss do
    local t = table.remove(current, 1)
    if t[1] == r_tgt and t[2] == c_tgt then path_heat_loss = t[3]; break end
    local rc_key = t[1] * (r_tgt + 1) + t[2]
    
    if not log[rc_key] then log[rc_key] = {} end
    if not log[rc_key][t[4] % 2] or log[rc_key][t[4] % 2] > t[3] then
        log[rc_key][t[4] % 2] = t[3]
        
        local a, b, c
        if t[4] > 0 then a, b, c = t[4] % 2 + 1, 4, 2 else a, b, c = 1, 2, 1 end
        for i = a, b, c do
            local dir, g_cost = dirs[i], t[3]
            for step = 1, 3 do
                local r_new, c_new = t[1] + dir[1] * step, t[2] + dir[2] * step
                if not map[r_new] or not map[r_new][c_new] then break end
                g_cost = g_cost + map[r_new][c_new]
                local h_cost = r_tgt - r_new + c_tgt - c_new
                    
                local rc_key_new = r_new * (r_tgt + 1) + c_new
                if not log[rc_key_new] or not log[rc_key_new][i % 2] or log[rc_key_new][i % 2] > g_cost then
                    table.insert(current, {r_new, c_new, g_cost, i, step, h_cost}) end
            end
        end

        table.sort(current, compare)
    end
end
print(string.format("Part 1: %d", path_heat_loss))

current, n, log, path_heat_loss = {{1, 1, 0, 0, 0, 0}}, 0, {}
while not path_heat_loss do
    local t = table.remove(current, 1)
    if t[1] == r_tgt and t[2] == c_tgt then path_heat_loss = t[3]; break end
    local rc_key = t[1] * (r_tgt + 1) + t[2]
    
    if not log[rc_key] then log[rc_key] = {} end
    if not log[rc_key][t[4] % 2] or log[rc_key][t[4] % 2] > t[3] then
        log[rc_key][t[4] % 2] = t[3]
        
        local a, b, c
        if t[4] > 0 then a, b, c = t[4] % 2 + 1, 4, 2 else a, b, c = 1, 2, 1 end
        for i = a, b, c do
            local dir, g_cost = dirs[i], t[3]
            for step = 1, 10 do
                local r_new, c_new = t[1] + dir[1] * step, t[2] + dir[2] * step
                if not map[r_new] or not map[r_new][c_new] then break end
                g_cost = g_cost + map[r_new][c_new]
                local h_cost = r_tgt - r_new + c_tgt - c_new
                    
                if step > 3 then
                    local rc_key_new = r_new * (r_tgt + 1) + c_new
                    if not log[rc_key_new] or not log[rc_key_new][i % 2] or log[rc_key_new][i % 2] > g_cost then
                        table.insert(current, {r_new, c_new, g_cost, i, step, h_cost}) end
                end
            end
        end

        table.sort(current, compare)
    end
end
print(string.format("Part 2: %d", path_heat_loss))