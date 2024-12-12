local map, trailheads = {}, {}
local dirs = {{r = -1, c = 0}, {r = 0, c = 1}, {r = 1, c = 0}, {r = 0, c = -1}}

local row = 0
for line in io.lines("../__in/10.txt") do
    local map_row, col = {}, 0; row = row + 1
    
    for tile in line:gmatch(".") do
        tile, col = tonumber(tile) or -1, col + 1
        
        table.insert(map_row, tile)
        if tile == 0 then table.insert(trailheads, {r = row, c = col}) end
    end
    
    table.insert(map, map_row)
end

local score1, score2, k = 0, 0, #map[1] + 1
for _, trailhead in ipairs(trailheads) do
    local h, step = 0, {{r = trailhead.r, c = trailhead.c, score = 1}}
    
    while h < 9 do
        local next_step, log = {}, {}; h = h + 1
        
        for _, tile in ipairs(step) do
            for _, d in ipairs(dirs) do
                local r, c = tile.r + d.r, tile.c + d.c
                if map[r] and map[r][c] == h then
                    if log[k * r + c] then log[k * r + c] = log[k * r + c] + tile.score
                    else table.insert(next_step, {r = r, c = c}); log[k * r + c] = tile.score end
                end
            end
        end
                
        for _, tile in ipairs(next_step) do tile.score = log[k * tile.r + tile.c] end        
        step = next_step
    end
    
    score1 = score1 + #step
    for _, tile in ipairs(step) do score2 = score2 + tile.score end
end

print(string.format("Part 1: %d", score1))
print(string.format("Part 2: %d", score2))