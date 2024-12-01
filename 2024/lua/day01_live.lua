local total1, total2 = 0, 0
local left, right, right_counts = {}, {}, {}

for line in io.lines("../__in/01.txt") do
    local l, r = line:match("(%d+)%s+(%d+)")
    l, r = tonumber(l), tonumber(r)
    
    table.insert(left, l)
    table.insert(right, r)
    right_counts[r] = (right_counts[r] or 0) + 1
end

table.sort(left); table.sort(right)

for i = 1, #left do
    total1 = total1 + ((left[i] > right[i]) and (left[i] - right[i]) or (right[i] - left[i]))
    total2 = total2 + left[i] * (right_counts[left[i]] or 0)
end

print(string.format("Part 1: %d", total1))
print(string.format("Part 2: %d", total2))