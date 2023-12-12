local function fuelforfuel(fuel)
    local t = math.floor(fuel / 3) - 2
    if t > 0 then return t + fuelforfuel(t) else return 0 end end

local fuel_p1, fuel_p2 = 0, 0
for line in io.lines("../__in/01.txt") do
    local t = math.floor(tonumber(line) / 3) - 2
    fuel_p1 = fuel_p1 + t
    fuel_p2 = fuel_p2 + t + fuelforfuel(t) end

print(string.format("Part 1: %d", fuel_p1))
print(string.format("Part 2: %d", fuel_p2))