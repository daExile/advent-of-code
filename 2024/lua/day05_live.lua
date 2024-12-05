local input = io.open("../__in/05.txt"):lines()
local total_ordered, total_reordered = 0, 0
local pairwise = {} -- {pageA = {pageB1 = (pageA|pageB1), pageB2...}}

local function manual_in_order(manual)
    for i = 1, #manual - 1 do if not pairwise[manual[i]][manual[i + 1]] then return false end end
    return true
end

for line in input do
    if line == "" then break end
    local p1, p2 = line:match("(%d+)|(%d+)"); p1, p2 = tonumber(p1), tonumber(p2)
    
    if not pairwise[p1] then pairwise[p1] = {} end; pairwise[p1][p2] = true
    if not pairwise[p2] then pairwise[p2] = {} end; pairwise[p2][p1] = false
end

for line in input do
    local manual = {}
    for p in line:gmatch("%d+") do table.insert(manual, tonumber(p)) end
    
    if manual_in_order(manual) then
        total_ordered = total_ordered + manual[(#manual + 1) / 2]
    else
        table.sort(manual, function(a, b) return pairwise[a][b] end)
        total_reordered = total_reordered + manual[(#manual + 1) / 2]
    end
end

print(string.format("Part 1: %d", total_ordered))
print(string.format("Part 2: %d", total_reordered))