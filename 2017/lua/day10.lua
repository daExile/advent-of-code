require("stuff")

function bitxor(a, b)
    local r = 0
    for i = 0, 7 do r, a, b = r + (a + b) % 2 * (2 ^ i), math.floor(a / 2), math.floor(b / 2) end
    return r end

function init()
    local t = {}
    for i = 0, size - 1 do table.insert(t, i) end
    return t end
    
function knot(t, len)
    local tmp = {}
    
    for i = start, start + len - 1 do
        if i > size then table.insert(tmp, t[i - size]) else table.insert(tmp, t[i]) end end
    for i, v in ipairs(tmp) do
        local j = start + len - i
        if j > size then t[j - size] = tmp[i] else t[j] = tmp[i] end end
    return t end

function knothash(t, input, rounds)
    for r = 1, rounds do
        for i, v in ipairs(input) do
            t = knot(t, v)
            start = (start + skip + v - 1) % size + 1; skip = skip + 1
        end
    end
    return t end

function getdensehash(sparsehash)
    local hash = ""
    for i = 0, (#sparsehash / 16 - 1) do
        local n = sparsehash[i * 16 + 1]
        for j = 2, 16 do n = bitxor(n, sparsehash[i * 16 + j]) end
        hash = hash..string.format("%02x", n) end
    return hash end

input = io.input("10.txt"):read(); io.close()

p1data = stuff.str2numtable(input)
p2data = {}
for _, v in ipairs(stuff.str2anychartable(input)) do table.insert(p2data, string.byte(v)) end
for _, v in ipairs({17, 31, 73, 47, 23}) do table.insert(p2data, v) end -- add standard ending

size = 256

start, skip = 1, 0 -- part 1
t = knothash(init(), p1data, 1)
print(string.format("Part 1: %d", t[1] * t[2]))

start, skip = 1, 0 -- part 2
t = knothash(init(), p2data, 64)
print(string.format("Part 2: %s", getdensehash(t)))