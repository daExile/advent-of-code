local map, bytes = {}, {}
local dirs = {{r = -1, c = 0}, {r = 0, c = 1}, {r = 1, c = 0}, {r = 0, c = -1}}
local p1_cutoff = 1024

local r_max, c_max, i = 0, 0, 0
for line in io.lines("../__in/18.txt") do
    i = i + 1
    local c, r = line:match("(%d+),(%d+)"); r, c = tonumber(r), tonumber(c)
    if r > r_max then r_max = r end; if c > c_max then c_max = c end
    
    if not map[r] then map[r] = {} end
    table.insert(bytes, {c = c, r = r})
end

for i = 1, p1_cutoff do map[bytes[i].r][bytes[i].c] = "#" end

local function check_path(map)
    local queue, step, path = {{r = 0, c = 0}}, 0, {}
    
    while #queue > 0 and not (path[r_max] and path[r_max][c_max]) do
        step = step + 1
        local next_queue = {}
    
        for _, tile in ipairs(queue) do
            if not path[tile.r] then path[tile.r] = {} end; path[tile.r][tile.c] = step
        
            for _, d in ipairs(dirs) do
                local t = {r = tile.r + d.r, c = tile.c + d.c}
                if t.r >= 0 and t.r <= r_max and t.c >= 0 and t.c <= c_max and map[t.r][t.c] ~= "#" then
                    if not path[t.r] then path[t.r] = {} end
                    if not path[t.r][t.c] then table.insert(next_queue, {r = t.r, c = t.c}); path[t.r][t.c] = step end
                end
            end
        end
    
        queue = next_queue
    end
    
    return (path[r_max] and path[r_max][c_max])
end

print(string.format("Part 1: %d", check_path(map)))

-- stupid bruteforce lol
local i = p1_cutoff
repeat
    i = i + 1
    map[bytes[i].r][bytes[i].c] = "#"
until not check_path(map)

print("Part 2: " .. bytes[i].c .. "," .. bytes[i].r) -- .. " (byte #" .. i .. ")")