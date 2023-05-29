scanners = {}
for line in io.lines("13.txt") do
    local depth, range = string.match(line, "(%d+): (%d+)");
    table.insert(scanners, {depth = tonumber(depth), range = tonumber(range)})
end

severity = 0
for _, v in ipairs(scanners) do
    if v.depth % (2 * (v.range - 1)) == 0 then severity = severity + v.depth * v.range end
end

delay = 0
repeat
    delay = delay + 1
    gotcha = false
    for _, v in ipairs(scanners) do
        if (v.depth + delay) % (2 * (v.range - 1)) == 0 then gotcha = true break end
    end
until not gotcha

print(string.format("Part 1: %d", severity))
print(string.format("Part 2: %d", delay))