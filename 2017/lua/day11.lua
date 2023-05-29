stuff = require("stuff")

--[[    a       a.         _        let's invent hexagonal wheel for fun!
        |       |  `b =   .c    <-- axis are set such as (1, 0, 0) + (0, 1, 0) = (0, 0, -1), and so on
       .o.      o      o'           also any triplet is reducible to (+n1, -n2, 0) or set with more zeroes,
    c'     `b                       and reduced form gives the Manhattan distance just like Carthesian (x, y). ]]

move = {n = {1, 0, 0}, ne = {0, 0, -1}, se = {0, 1, 0}, s = {-1, 0, 0}, sw = {0, 0, 1}, nw = {0, -1, 0}}

function step(pos, dir)
    for i = 1, 3 do pos[i] = pos[i] + move[dir][i] end
    return pos end

function reduce(t)
    local tmp = {}; for i = 1, 3 do table.insert(tmp, t[i]) end
    table.sort(tmp); local delta = tmp[2]
    
    for i = 1, 3 do tmp[i] = t[i] - delta end
    return tmp end

function hexmd(t) return math.abs(t[1] - t[2] - t[3]) end

input = stuff.str2strtable(io.open("11.txt", "r"):read())

pos, max = {0, 0, 0}, 0
for _, v in ipairs(input) do
    pos = reduce(step(pos, v))
    local d = hexmd(pos); if max < d then max = d end
end

print(string.format("Part 1: %d", hexmd(pos)))
print(string.format("Part 2: %d", max))