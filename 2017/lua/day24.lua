local bridges, nodes, paths = {}, {}, {[0] = { {bridges = {}, endnode = 0, sum = 0} }}
local maxstr, maxlen = 0, 0

local function getnodes(line)
    local n1, n2 = string.match(line, "([%d]+)/([%d]+)")
    return tonumber(n1), tonumber(n2) end

local function addbridge(path, bridge_id)
    local t, end_new, sum_new = {}
    
    for k, _ in pairs(path.bridges) do t[k] = true end
    t[bridge_id] = true
    
    if path.endnode == bridges[bridge_id].nodes[1] then end_new = bridges[bridge_id].nodes[2]
    else end_new = bridges[bridge_id].nodes[1] end
    sum_new = path.sum + bridges[bridge_id].str; maxstr = math.max(maxstr, sum_new)

    return {bridges = t, endnode = end_new, sum = sum_new} end

for line in io.lines("24.txt") do
    local n1, n2 = getnodes(line)

    table.insert(bridges, {nodes = {n1, n2}, str = (n1 + n2)})
    
    if not nodes[n1] then nodes[n1] = {} end; table.insert(nodes[n1], #bridges)
    if not nodes[n2] then nodes[n2] = {} end; if n1 ~= n2 then table.insert(nodes[n2], #bridges) end
end

repeat
    local step, maxlen_step = #paths + 1, 0
    paths[step] = {}
    
    for _, p in ipairs(paths[step - 1]) do
        for _, n in ipairs(nodes[p.endnode]) do
            if not p.bridges[n] then
                local path_new = addbridge(p, n)
                if path_new and path_new.sum > maxlen_step then maxlen_step = path_new.sum end
                table.insert(paths[step], path_new) end end end
    
    if maxlen_step > 0 then maxlen = maxlen_step end
until #paths[#paths] == 0

print(string.format("Part 1: %d", maxstr))
print(string.format("Part 2: %d", maxlen))