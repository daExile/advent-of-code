local map, antennas = {}, {}

local row = 0
for line in io.lines("../__in/08.txt") do
    local map_row, col = {}, 0; row = row + 1
    
    for tile in line:gmatch(".") do
        col = col + 1
        
        if tile ~= "." then
            if not antennas[tile] then antennas[tile] = {} end
            table.insert(antennas[tile], {r = row, c = col})
        end
        table.insert(map_row, tile)
    end
    
    table.insert(map, map_row)
end

-- part 1
local antinodes = 0
for f, a_list in pairs(antennas) do
    for i = 1, #a_list - 1 do
        for j = i + 1, #a_list do
            local dr, dc = a_list[j].r - a_list[i].r, a_list[j].c - a_list[i].c
            local a1, a2 = {r = a_list[i].r - dr, c = a_list[i].c - dc}, {r = a_list[j].r + dr, c = a_list[j].c + dc}
            
            if map[a1.r] and map[a1.r][a1.c] and map[a1.r][a1.c] ~= "#" then map[a1.r][a1.c] = "#"; antinodes = antinodes + 1 end
            if map[a2.r] and map[a2.r][a2.c] and map[a2.r][a2.c] ~= "#" then map[a2.r][a2.c] = "#"; antinodes = antinodes + 1 end
        end
    end
end

-- part 2 - all (dr, dc) pairs seem to be co-prime, so no code for GCD check and adding intermediate nodes
local antinodes_resonance = antinodes
for f, a_list in pairs(antennas) do
    for i = 1, #a_list - 1 do
        for j = i + 1, #a_list do
            local dr, dc = a_list[j].r - a_list[i].r, a_list[j].c - a_list[i].c
            
            local a_t = {r = a_list[i].r, c = a_list[i].c}
            while map[a_t.r] and map[a_t.r][a_t.c] do
                if map[a_t.r][a_t.c] ~= "#" then map[a_t.r][a_t.c] = "#"; antinodes_resonance = antinodes_resonance + 1 end
                a_t = {r = a_t.r - dr, c = a_t.c - dc}
            end
            
            a_t = {r = a_list[j].r, c = a_list[j].c}
            while map[a_t.r] and map[a_t.r][a_t.c] do
                if map[a_t.r][a_t.c] ~= "#" then map[a_t.r][a_t.c] = "#"; antinodes_resonance = antinodes_resonance + 1 end
                a_t = {r = a_t.r + dr, c = a_t.c + dc}
            end
        end
    end
end

print(string.format("Part 1: %d", antinodes))
print(string.format("Part 2: %d", antinodes_resonance))