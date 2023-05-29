local aoc17 = {}

function bin(n)
    local str = ""
    for i = 0, 7 do str, n = str..n % 2, math.floor(n / 2) end
    return string.reverse(str) end

function hex(n) return string.format("%02x", n) end

function rotate(s, n)
    n = n % size
    return string.sub(s, n + 1)..string.sub(s, 1, n) end

function reverse_n(s, n) return string.sub(s, 1, n):reverse()..string.sub(s, n + 1) end

function aoc17.init()
    local s = ""
    for i = 0, size - 1 do s = s..string.char(i) end
    return s end

function aoc17.knothash(s, input, rounds)
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

function aoc17.bitxor(a, b)
    local r = 0
    for i = 0, 7 do r, a, b = r / 2 + (a + b) % 2 * 128, math.floor(a / 2), math.floor(b / 2) end
    return r end

function aoc17.densehash(sparsehash, f_format)
    local hash = ""
    for i = 0, (#sparsehash / 16 - 1) do
        local n = sparsehash[i * 16 + 1]
        for j = 2, 16 do n = aoc17.bitxor(n, sparsehash[i * 16 + j]) end
        hash = hash..f_format(n) end
    return hash end
    
return aoc17