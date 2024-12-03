local total1, total2, enabled = 0, 0, true

for op, args in io.open("../__in/03.txt"):read("*a"):gmatch("([md][ulon't]+)(%([%d,]*%))") do
    if op == "do" then enabled = true           -- args check seems to be needed for mul only
    elseif op == "don't" then enabled = false   -- hopefully it won't explode for you :)
    elseif op == "mul" and args:match("%(%d%d?%d?%,%d%d?%d?%)") then
        local n1, n2 = args:match("(%d+),(%d+)")
        total1, total2 = total1 + n1 * n2, total2 + (enabled and (n1 * n2) or 0)
    end
end

print(string.format("Part 1: %d", total1))
print(string.format("Part 2: %d", total2))