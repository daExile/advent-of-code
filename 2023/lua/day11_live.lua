local function sort_by_col(g1, g2) return g1[2] < g2[2] or (g1[2] == g2[2] and g1[1] < g2[1]) end

local gmap1, gmap2, r1, r2, k = {}, {}, 1, 1, 1000000
for line in io.lines("../__in/11.txt") do
    local c, count = 1, 0
    for tile in string.gmatch(line, ".") do
        if tile == "#" then table.insert(gmap1, {r1, c}); table.insert(gmap2, {r2, c}); count = count + 1 end
        c = c + 1 end
    if count == 0 then r1 = r1 + 2; r2 = r2 + k else r1 = r1 + 1; r2 = r2 + 1 end end

table.sort(gmap1, sort_by_col); table.sort(gmap2, sort_by_col)
local t_new, delta, c_prev = {}, 0
for _, g in ipairs(gmap1) do
    if c_prev and g[2] - c_prev > 1 then delta = delta + (g[2] - c_prev - 1) end
    c_prev = g[2]
    table.insert(t_new, {g[1], g[2] + delta}) end
gmap1 = t_new

local paths_total_p1 = 0
for i = 1, #gmap1 - 1 do
    for j = i + 1, #gmap1 do
        paths_total_p1 = paths_total_p1 + math.abs(gmap1[j][1] - gmap1[i][1]) + math.abs(gmap1[j][2] - gmap1[i][2])
    end
end

print(string.format("Part 1: %d", paths_total_p1))

t_new, delta, c_prev = {}, 0, nil
for _, g in ipairs(gmap2) do
    if c_prev and g[2] - c_prev > 1 then empty = g[2] - c_prev - 1; delta = delta + empty * (k - 1) end
    c_prev = g[2]
    table.insert(t_new, {g[1], g[2] + delta}) end
gmap2 = t_new

local paths_total_p2 = 0
for i = 1, #gmap2 - 1 do
    for j = i + 1, #gmap2 do
        paths_total_p2 = paths_total_p2 + math.abs(gmap2[j][1] - gmap2[i][1]) + math.abs(gmap2[j][2] - gmap2[i][2])
    end
end

print(string.format("Part 2: %.0f", paths_total_p2))