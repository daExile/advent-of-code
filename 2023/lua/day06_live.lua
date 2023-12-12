local input = {}
for line in io.lines("../__in/06.txt") do
    local t = {}
    for item in string.gmatch(line, "([%d]+)") do table.insert(t, tonumber(item)) end
    table.insert(input, t) end

local data = {}
for i = 1, #input[1] do table.insert(data, {input[1][i], input[2][i]}) end

local p1, p2time, p2dist = 1, "", ""
for _, race in ipairs(data) do
    p2time, p2dist = p2time .. race[1], p2dist .. race[2]
    
    local t = 0
    while (t * race[1] - t * t <= race[2]) do t = t + 1 end
    p1 = p1 * (race[1] + 1 - 2 * t) end

print(string.format("Part 1: %d", p1))

p2time = tonumber(p2time); p2dist = tonumber(p2dist)
local t = 0; while (t * p2time - t * t <= p2dist) do t = t + 1 end

print(string.format("Part 2: %d", p2time + 1 - 2 * t))