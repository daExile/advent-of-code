local map = {}
for line in io.lines("../__in/23.txt") do
    local row = {}; for tile in string.gmatch(line, ".") do table.insert(row, tile) end
    table.insert(map, row) end

local r_max, c_max, dirs = #map, #map[1], {{0, 1, "<", 3}, {1, 0, "^", 4}, {0, -1, ">", 1}, {-1, 0, "v", 2}}

local graph = {{r = 1, c = 2, nodes = {}}}, {{r = 1, c = 2, nodes = {}}}; local node_set = {[r_max + 2] = 1}
for r = 2, r_max - 1 do
    for c = 2, c_max - 1 do
        if map[r][c] ~= "#" then
            local count = 0
            for _, d in ipairs(dirs) do
                if map[r + d[1]][c + d[2]] ~= "#" then count = count + 1 end end
            if count > 2 then
                table.insert(graph, {r = r, c = c, nodes = {}}); node_set[r * r_max + c] = #graph end end end end
table.insert(graph, {r = r_max, c = c_max - 1, nodes = {}}); node_set[r_max * r_max + c_max - 1] = #graph

local function connect_nodes(slopes)
    for id = 1, #graph - 1 do
        graph[id].nodes = {}
        local t, step, queue = {[graph[id].r] = {[graph[id].c] = 0}}, 0, {{r = graph[id].r, c = graph[id].c}}
        
        while #queue > 0 do
            local queue_next = {}; step = step + 1
            
            for _, x in ipairs(queue) do
                for i_d, d in ipairs(dirs) do
                    local r_new, c_new = x.r + d[1], x.c + d[2]
                    if map[r_new] and map[r_new][c_new] ~= "#" and (map[r_new][c_new] ~= d[3] or not slopes) then
                        if not t[r_new] then t[r_new] = {} end
                        
                        if not t[r_new][c_new] then
                            if node_set[r_new * r_max + c_new] then
                                table.insert(graph[id].nodes, {node_set[r_new * r_max + c_new], step})
                            else
                                t[r_new][c_new] = step
                                table.insert(queue_next, {r = r_new, c = c_new})
                            end end end end end
            queue = queue_next end end end

local function scenic_route(cur, dist, dist_max, visited)
    visited[cur] = true
    
    for _, node in ipairs(graph[cur].nodes) do
        if node[1] == #graph then if dist + node[2] > dist_max then dist_max = dist + node[2] end
        elseif not visited[node[1]] then dist_max = scenic_route(node[1], dist + node[2], dist_max, visited) end
    end
    
    visited[cur] = nil; return dist_max end

connect_nodes(true)
print(string.format("Part 1: %d", scenic_route(1, 0, 0, {})))

connect_nodes(false)
print(string.format("Part 2: %d", scenic_route(1, 0, 0, {})))