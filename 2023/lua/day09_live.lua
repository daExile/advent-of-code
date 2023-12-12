local function extend(hist)
    local t, level, zeroed = {hist}, 1
    
    while not zeroed do
        t[level + 1], zeroed = {}, true
        for i = 1, #t[level] - 1 do
            local valnext = t[level][i + 1] - t[level][i]
            if valnext ~= 0 then zeroed = false end
            table.insert(t[level + 1], valnext) end
        level = level + 1 end
    
    while level > 1 do
        level = level - 1; local last = #t[level]
        t[level][last + 1] = t[level][last] + (t[level + 1][last] or 0)
        t[level][0] = t[level][1] - (t[level + 1][0] or 0) end
end
    
local ext_left_total, ext_right_total = 0, 0
for line in io.lines("../__in/09.txt") do
    local hist = {}
    for n in string.gmatch(line, "([%d-]+)") do table.insert(hist, tonumber(n)) end
    extend(hist)
    ext_left_total, ext_right_total = ext_left_total + hist[0], ext_right_total + hist[#hist]
end

print(string.format("Part 1: %d", ext_right_total))
print(string.format("Part 2: %d", ext_left_total))