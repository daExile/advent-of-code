local visited, obstacle_spots = 0, 0
local map, path = {}, {}

local function in_lab(map, r, c) return map[r] and map[r][c] end

local function turn_right(dr, dc) return dc, -dr end

local row, guard = 0
for line in io.lines("../__in/06.txt") do
    local map_row, col = {}, 0; row = row + 1
    
    for tile in line:gmatch(".") do
        col = col + 1
        
        if guard or tile ~= "^" then
            table.insert(map_row, tile)
        else
            table.insert(map_row, "."); guard = {r = row, c = col}
        end
    end
    
    table.insert(map, map_row)
end

local r, c, dr, dc, dir = guard.r, guard.c, -1, 0, 0
local dir_map = {}
while in_lab(map, r, c) do
    if not dir_map[r] then dir_map[r] = {} end
    if not dir_map[r][c] then
        dir_map[r][c] = dir
        visited = visited + 1
        if not (r == guard.r and c == guard.c) then table.insert(path, {r = r, c = c}) end
    end
    
    while map[r + dr] and map[r + dr][c + dc] == "#" do
        dr, dc = turn_right(dr, dc); dir = (dir + 1) % 4
    end
        
    r, c = r + dr, c + dc
end

print(string.format("Part 1: %d", visited))

for _, spot in ipairs(path) do
    local r, c, dr, dc, dir = guard.r, guard.c, -1, 0, 0
    local dir_map = {}
    local loops = false
    
    map[spot.r][spot.c] = "#"
    
    while in_lab(map, r, c) do
        if not dir_map[r] then dir_map[r] = {} end
        if not dir_map[r][c] then dir_map[r][c] = dir elseif dir_map[r][c] == dir then loops = true; break end
        
        while map[r + dr] and map[r + dr][c + dc] == "#" do dr, dc = turn_right(dr, dc); dir = (dir + 1) % 4 end
    
        r, c = r + dr, c + dc
    end
    
    map[spot.r][spot.c] = "."
    obstacle_spots = obstacle_spots + (loops and 1 or 0)
end
    
print(string.format("Part 2: %d", obstacle_spots))