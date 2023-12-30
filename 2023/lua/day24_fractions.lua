-- fraction solver where Lua's integers failed me in the end by a tiny margin,
-- but I liked coding this approach, so I'm keeping it for the record.

local function gcd(x, y)    -- euclidean this time
    x, y = math.abs(x), math.abs(y)
    if y == x then return x
    else
        if y > x then x, y = y, x end
        while y ~= 0 do x, y = y, x % y end
    end
    return x end

Frac = {}

function Frac:new(_a, _b)
    local k = gcd(_a, (_b or 1)); k = _b and _b < 0 and -k or k; newobj = {a = _a / k; b = (_b or 1) / k}
    self.__index = self
    return setmetatable(newobj, self) end

function Frac.__unm(f) return Frac:new(-f.a, f.b) end

function Frac.__add(n1, n2)
    if tonumber(n2) then return Frac:new(n1.a + n2 * n1.b, n1.b)
    else
        local k = gcd(n1.b, n2.b); local k1, k2 = n2.b / k, n1.b / k
        local sum = Frac:new(n1.a * k1 + n2.a * k2, n1.b * k1); return sum end end

function Frac.__sub(n1, n2) return n1 + (-n2) end

function Frac.__mul(n1, n2)
    if tonumber(n2) then return Frac:new(n1.a * n2, n1.b)
    else local prod = Frac:new(n1.a * n2.a, n1.b * n2.b); return prod end end

function Frac.__div(n1, n2)
    if tonumber(n2) then return Frac:new(n1.a, n1.b * n2)
    else local quot = Frac:new(n1.a * n2.b, n1.b * n2.a); return quot end end

local hailstones = {}; local v = {}
for line in io.lines("../__in/24.txt") do
    local t = {}; for item in string.gmatch(line, "([%d-]+)") do table.insert(t, tonumber(item)) end
    table.insert(hailstones, t) end

--local c_min, c_max = 7, 27 -- ranges for example input
local c_min, c_max = 200000000000000, 400000000000000 -- ranges for puzzle input

local Xs = 0
for i = 1, #hailstones - 1 do
    for j = i + 1, #hailstones do
        local a1, a2 = hailstones[i][5] / hailstones[i][4], hailstones[j][5] / hailstones[j][4]
        
        if a1 ~= a2 then
            local b1, b2 = hailstones[i][2] - hailstones[i][1] * a1, hailstones[j][2] - hailstones[j][1] * a2
            local x = (b2 - b1) / (a1 - a2); local y = a1 * x + b1
            local t1, t2 = (x - hailstones[i][1]) / hailstones[i][4], (x - hailstones[j][1]) / hailstones[j][4]

            if x >= c_min and x <= c_max and y >= c_min and y <= c_max and t1 >= 0 and t2 >= 0 then Xs = Xs + 1 end
        end end end

print(string.format("Part 1: %d", Xs))

local function solve_p2()
    local a, b, c = hailstones[1], hailstones[2], hailstones[3]
    local A, B = {}, {}; local o = Frac:new(0)
    
    local t = {}; for i = 1, 6 do table.insert(t, Frac:new(a[i] - b[i])) end
    
    table.insert(A, {o, -t[6], t[5], o, t[3], -t[2]})
    table.insert(A, {t[6], o, -t[4], -t[3], o, t[1]})
    table.insert(A, {-t[5], t[4], o, t[2], -t[1], o})
    
    table.insert(B, Frac:new(-a[2] * a[6] + b[2] * b[6] + a[3] * a[5] - b[3] * b[5]))
    table.insert(B, Frac:new(-a[3] * a[4] + b[3] * b[4] + a[1] * a[6] - b[1] * b[6]))
    table.insert(B, Frac:new(-a[1] * a[5] + b[1] * b[5] + a[2] * a[4] - b[2] * b[4]))
    
    t = {}; for i = 1, 6 do table.insert(t, Frac:new(a[i] - c[i])) end
    
    table.insert(A, {o, -t[6], t[5], o, t[3], -t[2]})
    table.insert(A, {t[6], o, -t[4], -t[3], o, t[1]})
    table.insert(A, {-t[5], t[4], o, t[2], -t[1], o})
    
    table.insert(B, Frac:new(-a[2] * a[6] + c[2] * c[6] + a[3] * a[5] - c[3] * c[5]))
    table.insert(B, Frac:new(-a[3] * a[4] + c[3] * c[4] + a[1] * a[6] - c[1] * c[6]))
    table.insert(B, Frac:new(-a[1] * a[5] + c[1] * c[5] + a[2] * a[4] - c[2] * c[4]))
    
    local Ai = {}; for i = 1, 6 do local row = {o, o, o, o, o, o}; row[i] = Frac:new(1); table.insert(Ai, row) end
    
    -- inverting the matrix by gaussian elimination
    for i = 1, 6 do
        if A[i][i].a == 0 then
            for n = i + 1, 6 do
                if A[n][i].a ~= 0 then
                    for j = 1, 6 do A[i][j] = A[i][j] + A[n][j]; Ai[i][j] = Ai[i][j] + Ai[n][j] end; break
                end
            end
        end
        
        local k = Frac:new(1) / A[i][i]; for j = 1, 6 do A[i][j] = A[i][j] * k; Ai[i][j] = Ai[i][j] * k end
        
        for n = i + 1, 6 do
            if A[n][i].a ~= 0 then
                local k = A[n][i] / A[i][i]
                for j = 1, 6 do A[n][j] = A[n][j] / k - A[i][j]; Ai[n][j] = Ai[n][j] / k - Ai[i][j] end
            end
        end
    end
    
    for i = 6, 2, -1 do
        for n = i - 1, 1, -1 do
            local k = A[n][i] / A[i][i]; A[n][i] = o; for j = 1, 6 do Ai[n][j] = Ai[n][j] - Ai[i][j] * k end
        end
    end
    
    local result = {}
    for i = 1, 6 do local r = Frac:new(0); for j = 1, 6 do r = r + Ai[i][j] * B[j] end; table.insert(result, r) end
    
    return result end

local result = solve_p2()
print(string.format("Part 2: %.0f", result[1].a / result[1].b + result[2].a / result[2].b + result[3].a / result[3].b))