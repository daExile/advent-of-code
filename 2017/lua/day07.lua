stuff = require("stuff")

function towercheck(name)
    local total, held = weights[name], {}
    for _, item in ipairs(holds[name]) do
        local t = towercheck(item)
        if done then break end
        
        if not held[t] then held[t] = {item} else table.insert(held[t], item) end
        total = total + t
    end

    if stuff.tablesize(held) <= 1 then return total end
    
    local good, bad
    for k, v in pairs(held) do if #v == 1 then bad = k; unbalanced = v[1] else good = k end end
    delta, done = (good - bad), true
    return total end

weights, holds, heldby = {}, {}, {}
for line in io.lines("07.txt") do
    name, wgt = string.match(line, "(%w+)%s%((%d+)%)")
    weights[name] = tonumber(wgt)
    if not heldby[name] then heldby[name] = "" end
    
    local tmp = {}
    for item in string.gmatch(line, "%s(%w+)") do table.insert(tmp, item); heldby[item] = name end
    holds[name] = tmp
end

-- part 1
for k, v in pairs(heldby) do if v == "" then root = k; break end end
-- part 2
done, unbalanced, delta = false
towercheck(root)

print(string.format("Part 1: %s", root))
print(string.format("Part 2: %s should have a weight of %d", unbalanced, weights[unbalanced] + delta))