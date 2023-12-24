local hailstones = {}
for line in io.lines("../__in/24.txt") do
    local t = {}; for item in string.gmatch(line, "([%d-]+)") do table.insert(t, tonumber(item)) end
    table.insert(hailstones, {x = t[1], y = t[2], z = t[3], dx = t[4], dy = t[5], dz = t[6]}) end

--local c_min, c_max = 7, 27
local c_min, c_max = 200000000000000, 400000000000000

local Xs = 0
for i = 1, #hailstones - 1 do
    for j = i + 1, #hailstones do
        local a1, a2 = hailstones[i].dy / hailstones[i].dx, hailstones[j].dy / hailstones[j].dx
        
        if a1 ~= a2 then
            local b1, b2 = hailstones[i].y - hailstones[i].x * a1, hailstones[j].y - hailstones[j].x * a2
            local x = (b2 - b1) / (a1 - a2); local y = a1 * x + b1
            local t1, t2 = (x - hailstones[i].x) / hailstones[i].dx, (x - hailstones[j].x) / hailstones[j].dx

            if x >= c_min and x <= c_max and y >= c_min and y <= c_max and t1 >= 0 and t2 >= 0 then Xs = Xs + 1 end
        end end end

print(string.format("Part 1: %d", Xs))
--print(string.format("Part 2: %d", nope_not_yet))