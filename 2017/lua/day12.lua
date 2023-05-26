require("stuff")

function getlinks(name, links)
    links[name] = true; log[name] = true
    for _, v in ipairs(pipes[name]) do
        if not links[v] then getlinks(v, links) end end
    return links end

pipes, groups, log = {}, {}, {}
for line in io.lines("12.txt") do
    local name, data = string.match(line, "(%d+) <%-> (.+)");
    pipes[tonumber(name)] = stuff.str2numtable(data)
end

for name, _ in pairs(pipes) do
    if not log[name] then
        local links = getlinks(name, {})
        table.insert(groups, links)
    end
end

print(string.format("Part 1: %d", stuff.tablesize(groups[1])))
print(string.format("Part 2: %d", #groups))