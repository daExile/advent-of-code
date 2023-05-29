stuff = require("stuff")

input = io.input("10.txt"):read(); io.close()

p1data = stuff.str2numtable(input)
p2data = {}
for _, v in ipairs(stuff.str2anychartable(input)) do table.insert(p2data, string.byte(v)) end
for _, v in ipairs({17, 31, 73, 47, 23}) do table.insert(p2data, v) end -- add standard ending

size = 256

-- part 1
t = stuff.knothash(stuff.init(), p1data, 1)
print(string.format("Part 1: %d", t[1] * t[2]))

-- part 2
t = stuff.knothash(stuff.init(), p2data, 64)
print(string.format("Part 2: %s", stuff.densehash(t, hex)))