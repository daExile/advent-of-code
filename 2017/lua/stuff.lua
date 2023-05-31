local stuff = {}

-- general purpose functions
    -- some string to table conversions
function stuff.str2table(str, pattern)
    local t = {}
    for item in string.gmatch(str, pattern) do
        if pattern == "%d+" then table.insert(t, tonumber(item)) else table.insert(t, item) end
    end
    return t end

function stuff.str2strtable(str) return stuff.str2table(str, "%w+") end

function stuff.str2numtable(str) return stuff.str2table(str, "%d+") end

function stuff.str2alnumchartable(str) return stuff.str2table(str, "%w") end

function stuff.str2anychartable(str) return stuff.str2table(str, ".") end

    -- some min/max lookups, very likely need more work
function stuff.tableminmax(t)
    local min, max
    for _, item in ipairs(t) do
        if not min or item < min then min = item end
        if not max or item > max then max = item end
    end
    return {min, max} end

function stuff.tablemaxindex(t)
    local max, k
    for i, item in ipairs(t) do
        if not max or item > max then k, max = i, item end
    end
    return k end

function stuff.tablemax(t)
    local max
    for k, v in pairs(t) do if not max or v > max then max = v end end
    return max end

    -- #table for when indices are whatever
function stuff.tablesize(t)
    local size = 0
    for k, v in pairs(t) do size = size + 1 end
    return size end
    
-- AoC 2017 knot hashing functions w/supplements
    -- init starting string
function stuff.init()
    local s = ""
    for i = 0, size - 1 do s = s..string.char(i) end
    return s end
    
    -- hashing itself
function rotate(s, n)
    n = n % size
    return string.sub(s, n + 1)..string.sub(s, 1, n) end

function reverse_n(s, n) return string.sub(s, 1, n):reverse()..string.sub(s, n + 1) end

function stuff.knothash(s, input, rounds)
    offset, skip = 0, 0
    for r = 1, rounds do
        for i, v in ipairs(input) do
            if v <= size then s = rotate(reverse_n(s, v), v + skip) end
            offset = (offset + skip + v) % size; skip = skip + 1
        end
    end
    s = rotate(s, -offset)
    
    local sparsehash = {}
    for _, v in ipairs(stuff.str2anychartable(s)) do table.insert(sparsehash, string.byte(v)) end
    return sparsehash end

    -- extracting the resulting hash
function bitxor(a, b)
    local r = 0
    for i = 0, 7 do r, a, b = r / 2 + (a + b) % 2 * 128, math.floor(a / 2), math.floor(b / 2) end
    return r end

function bin(n)
    local str = ""
    for i = 0, 7 do str, n = str..n % 2, math.floor(n / 2) end
    return string.reverse(str) end

function hex(n) return string.format("%02x", n) end

function stuff.densehash(sparsehash, f_format)
    local hash = ""
    for i = 0, (#sparsehash / 16 - 1) do
        local n = sparsehash[i * 16 + 1]
        for j = 2, 16 do n = bitxor(n, sparsehash[i * 16 + j]) end
        hash = hash..f_format(n) end
    return hash end

return stuff