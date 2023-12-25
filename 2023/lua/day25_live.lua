local nodes, edges, nodes_count, n, id0 = {}, {}, 0, 0
for line in io.lines("../__in/25.txt") do
    local this_id, connections = string.match(line, "([%w]+): (.*)"); if not id0 then id0 = this_id end
    
    if not nodes[this_id] then nodes[this_id] = {}; nodes_count = nodes_count + 1 end
    
    for other_id in string.gmatch(connections, "([%w]+)") do
        n = n + 1; table.insert(nodes[this_id], {other_id, n})
        if not nodes[other_id] then nodes[other_id] = {}; nodes_count = nodes_count + 1 end
        table.insert(nodes[other_id], {this_id, n}); table.insert(edges, {this_id, other_id, 0})
    end
end

-- looking for "edge replacement costs", how long is the path between two nodes if the edge is removed
local cost_db, costs = {}, {}
for e_id, edge in ipairs(edges) do
    local queue, target, log, dist = {edge[1]}, edge[2], {}, 0
    
    while edge[3] == 0 do
        local queue_next = {}
        
        for _, node in ipairs(queue) do
            if node == target then edge[3] = dist; break end
            if not log[node] then
                log[node] = true
                for _, connection in ipairs(nodes[node]) do
                    if connection[2] ~= e_id then table.insert(queue_next, connection[1]) end end
            end
        end
        
        queue = queue_next; dist = dist + 1
    end
    if not cost_db[edge[3]] then cost_db[edge[3]] = {}; table.insert(costs, edge[3]) end
    table.insert(cost_db[edge[3]], e_id)
end

table.sort(costs, function(n1, n2) return n1 > n2 end)

local i, removables = 1, {}
repeat for _, e_id in ipairs(cost_db[costs[i]]) do table.insert(removables, e_id) end; i = i + 1 until #removables >= 3

local answer
for i = 1, #removables - 2 do
    for j = i + 1, #removables - 1 do
        for k = j + 1, #removables do
            local set, queue, count = {[id0] = true}, {}, 1
            local edge1, edge2, edge3 = removables[i], removables[j], removables[k] 
            
            for _, wire in ipairs(nodes[id0]) do
                if not set[wire[1]] and wire[2] ~= edge1 and wire[2] ~= edge2 and wire[2] ~= edge3 then
                    table.insert(queue, wire[1]) end
            end
            
            while #queue > 0 do
                local queue_next = {}
                
                for _, node in ipairs(queue) do
                    if not set[node] then
                        set[node] = true; count = count + 1
                    
                        for _, wire in ipairs(nodes[node]) do
                            if not set[wire[1]] and wire[2] ~= edge1 and wire[2] ~= edge2 and wire[2] ~= edge3 then
                                table.insert(queue_next, wire[1]) end end
                    end
                end
                queue = queue_next
            end
            
            if count < nodes_count then answer = count * (nodes_count - count) end
        end; if answer then break end
    end; if answer then break end
end

print(string.format("Answer: %d", answer))