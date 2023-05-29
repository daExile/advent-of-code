stuff = require("stuff")

neighbour_deltas = {{x = 1, y = 0}, {x = 0, y = 1}, {x = -1, y = 0}, {x = 0, y = -1}}
function markregion(i, j)
    checked[i.." "..j] = true
    for _, n in ipairs(neighbour_deltas) do
        if map[i + n.x] and map[i + n.x][j + n.y] == "1" and not checked[i + n.x.." "..j + n.y] then
            markregion(i + n.x, j + n.y)
        end
    end
end

input = io.input("14.txt"):read(); io.close() 

map, size = {}, 256
for i = 0, 127 do
    local key = {}
    for _, v in ipairs(stuff.str2anychartable(input.."-"..i)) do table.insert(key, string.byte(v)) end
    for _, v in ipairs({17, 31, 73, 47, 23}) do table.insert(key, v) end -- add standard ending
    
    start, skip = 1, 0
    table.insert(map, stuff.str2anychartable(stuff.densehash(stuff.knothash(stuff.init(), key, 64), bin)))
end

count = 0
for _, row in ipairs(map) do count = count + #string.gsub(table.concat(row), "0", "") end
print(string.format("Part 1: %d", count))

checked, count = {}, 0
for i, row in ipairs(map) do
    for j, tile in ipairs(row) do
        if not checked[i.." "..j] and tile == "1" then
            count = count + 1
            markregion(i, j)
        end
    end
end
print(string.format("Part 2: %d", count))