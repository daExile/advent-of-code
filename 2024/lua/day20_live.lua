local map, notes, s, e = {}, {}
local dirs = {[0] = {r = -1, c = 0}, {r = 0, c = 1}, {r = 1, c = 0}, {r = 0, c = -1}}

local r = 0
for line in io.lines("../__in/20.txt") do
    local map_row, c = {}, 0; r = r + 1
    
    for tile in line:gmatch(".") do
        c = c + 1
        
        if tile == "S" then s = {r = r, c = c}; table.insert(map_row, 0)
        elseif tile == "E" then e = {r = r, c = c}; table.insert(map_row, ".")
        else table.insert(map_row, tile) end
    end
    
    table.insert(map, map_row)
end

local curr, step = {r = s.r, c = s.c}, 0
local d; for i = 0, 3 do if map[s.r + dirs[i].r] and map[s.r + dirs[i].r][s.c + dirs[i].c] == "." then d = i break end end

while not (curr.r == e.r and curr.c == e.c) do
    if map[curr.r + dirs[d].r][curr.c + dirs[d].c] == "#" then
        d = (map[curr.r + dirs[(d + 1) % 4].r][curr.c + dirs[(d + 1) % 4].c] ~= "#") and ((d + 1) % 4) or ((d - 1) % 4)
    end
    
    notes[step] = d; step = step + 1
    curr.r, curr.c = curr.r + dirs[d].r, curr.c + dirs[d].c
    map[curr.r][curr.c] = step
end
local r_max, c_max = #map, #map[1]
local count1, count2 = 0, 0; curr = {r = s.r, c = s.c}
for step = 0, #notes do
    for dr = -20, 20 do
        for dc = -20 + math.abs(dr), 20 - math.abs(dr) do
            if map[curr.r + dr] and tonumber(map[curr.r + dr][curr.c + dc]) then
                local distance = math.abs(dr) + math.abs(dc)
                local diff = map[curr.r + dr][curr.c + dc] - map[curr.r][curr.c] - distance
                
                if diff >= 100 then count1, count2 = count1 + (distance == 2 and 1 or 0), count2 + 1 end
            end
        end
    end
    
    curr.r, curr.c = curr.r + dirs[notes[step]].r, curr.c + dirs[notes[step]].c
end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %d", count2))