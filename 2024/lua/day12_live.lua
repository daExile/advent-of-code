local map, marked = {}, {}
local dirs = {{r = -1, c = 0}, {r = 0, c = 1}, {r = 1, c = 0}, {r = 0, c = -1}}

local total, total_bulk_discount = 0, 0

for line in io.lines("../__in/12.txt") do
    local map_row = {}
    
    for tile in line:gmatch(".") do table.insert(map_row, tile) end
    table.insert(map, map_row); table.insert(marked, {})
end

local function count_sides(fence)
    local sides = 0
    
    for dir_id = 1, 4 do
        for _, segments in pairs(fence[dir_id]) do
            table.sort(segments); local lane_sides = 1
            
            for i = 2, #segments do if segments[i] - segments[i - 1] > 1 then lane_sides = lane_sides + 1 end end
            sides = sides + lane_sides
        end
    end
    
    return sides
end

for r = 1, #map do
    for c = 1, #map[1] do
        if not marked[r][c] then
            local plant, step = map[r][c], {{r = r, c = c}}
            local area, perimeter = 0, 0
            local fence = {{}, {}, {}, {}}
            
            while #step > 0 do
                local next_step = {}
                
                for _, tile in ipairs(step) do
                    if not marked[tile.r][tile.c] then
                        marked[tile.r][tile.c], area = plant, area + 1
                        
                        for dir_id, d in ipairs(dirs) do
                            if map[tile.r + d.r] and map[tile.r + d.r][tile.c + d.c] == plant then
                                table.insert(next_step, {r = tile.r + d.r, c = tile.c + d.c})
                            else
                                perimeter = perimeter + 1
                                
                                local lane, segment
                                if dir_id % 2 == 0 then lane, segment = tile.c, tile.r else lane, segment = tile.r, tile.c end
                                
                                if not fence[dir_id][lane] then fence[dir_id][lane] = {} end
                                table.insert(fence[dir_id][lane], segment)
                            end
                        end
                    end
                end
                
                step = next_step
            end
            
            total = total + area * perimeter
            total_bulk_discount = total_bulk_discount + area * count_sides(fence)
        end
    end
end

print(string.format("Part 1: %d", total))
print(string.format("Part 2: %d", total_bulk_discount))