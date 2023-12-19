local function picks_shoelace_huehue(poly)
    local a, p = 0, 0
    for i = 1, #poly - 1 do
        a = a + poly[i][1] * poly[i + 1][2] - poly[i + 1][1] * poly[i][2]
        p = p + math.abs(poly[i + 1][1] - poly[i][1] + poly[i + 1][2] - poly[i][2])
    end
    
    return math.abs(a) / 2 + p / 2 + 1 end
    
local poly1, poly2 = {{0, 0}}, {{0, 0}}
local dirs = {[0] = {0, 1}, [1] = {1, 0}, [2] = {0, -1}, [3] = {-1, 0}}
local p1_conv = {["R"] = 0, ["D"] = 1, ["L"] = 2, ["U"] = 3}
for line in io.lines("../__in/18.txt") do
    local p1, p2, p3 = string.match(line, "([UDLR]) ([%d]+) %(#([%da-f]+)%)")
    
    local x1, d1 = tonumber(p2), p1_conv[p1]
    table.insert(poly1, {poly1[#poly1][1] + x1 * dirs[d1][1], poly1[#poly1][2] + x1 * dirs[d1][2]})
    
    local p3_1, p3_2 = string.match(p3, "([%da-f]+)([%da-f])")
    local x2, d2 = tonumber(p3_1, 16), tonumber(p3_2)
    table.insert(poly2, {poly2[#poly2][1] + x2 * dirs[d2][1], poly2[#poly2][2] + x2 * dirs[d2][2]})
end

print(string.format("Part 1: %d", picks_shoelace_huehue(poly1)))
print(string.format("Part 2: %.0f", picks_shoelace_huehue(poly2)))