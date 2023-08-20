local progs = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"}
local do_things; do_things = {
    p = function(p1, p2)
            local swap = {}
            for i, v in pairs(progs) do if v == p1 or v == p2 then table.insert(swap, i) end end
            do_things.x(swap[1], swap[2]) end,
    s = function(n)
            for i = 1, 16 - n do progs[i + 16] = progs[i] end
            for i = 1, 16 do progs[i] = progs[i + 16 - n] end
        end,
    x = function(n1, n2) progs[n1], progs[n2] = progs[n2], progs[n1] end
    }

local dance = {}
for s in string.gmatch(io.input("16.txt"):read(), ",?([%w/]+),?") do
    local move = {}
    table.insert(move, string.match(s, "^%w"))
    for arg in string.gmatch(s, "[psx/]([0-9a-p]+)") do
        if move[1] == "x" then table.insert(move, arg + 1) else table.insert(move, arg) end end
    
    table.insert(dance, move) end

local log, round = {}, 0
repeat
    local list = table.concat(progs, "", 1, 16); log[list] = round; log[round] = list
    round = round + 1
    for _, move in ipairs(dance) do do_things[move[1]](move[2], move[3]) end
until log[table.concat(progs, "", 1, 16)]

local target = 1000000000 % round
print(string.format("Part 1: %s", log[1]))
print(string.format("Part 2: %s", log[target]))