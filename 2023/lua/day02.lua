local p1, p2, gameid = 0, 0, 0
for line in io.lines("../__in/02.txt") do
    gameid = gameid + 1
    local count = {["red"] = 0, ["green"] = 0, ["blue"] = 0}
    for n, col in line:gmatch("(%d+) (%w+)") do
        if count[col] < tonumber(n) then count[col] = tonumber(n) end end

    if count["red"] <= 12 and count["green"] <= 13 and count["blue"] <= 14 then p1 = p1 + gameid end
    p2 = p2 + count["red"] * count["green"] * count["blue"]
end

print(string.format("Part 1: %d", p1))
print(string.format("Part 2: %d", p2))