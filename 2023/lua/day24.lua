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
    local A, B, t = {}, {}, {}
    
    for i = 1, 6 do table.insert(t, a[i] - b[i]) end
    
    table.insert(A, {0, -t[6], t[5], 0, t[3], -t[2]})
    table.insert(A, {t[6], 0, -t[4], -t[3], 0, t[1]})
    table.insert(A, {-t[5], t[4], 0, t[2], -t[1], 0})
    
    table.insert(B, -a[2] * a[6] + b[2] * b[6] + a[3] * a[5] - b[3] * b[5])
    table.insert(B, -a[3] * a[4] + b[3] * b[4] + a[1] * a[6] - b[1] * b[6])
    table.insert(B, -a[1] * a[5] + b[1] * b[5] + a[2] * a[4] - b[2] * b[4])
    
    t = {}
    for i = 1, 6 do table.insert(t, a[i] - c[i]) end
    
    table.insert(A, {0, -t[6], t[5], 0, t[3], -t[2]})
    table.insert(A, {t[6], 0, -t[4], -t[3], 0, t[1]})
    table.insert(A, {-t[5], t[4], 0, t[2], -t[1], 0})
    
    table.insert(B, -a[2] * a[6] + c[2] * c[6] + a[3] * a[5] - c[3] * c[5])
    table.insert(B, -a[3] * a[4] + c[3] * c[4] + a[1] * a[6] - c[1] * c[6])
    table.insert(B, -a[1] * a[5] + c[1] * c[5] + a[2] * a[4] - c[2] * c[4])
    
    local Ai = {}; for i = 1, 6 do local row = {0, 0, 0, 0, 0, 0}; row[i] = 1; table.insert(Ai, row) end
    
    -- inverting the matrix by gaussian elimination
    for i = 1, 6 do
        if A[i][i] == 0 then
            for n = i + 1, 6 do
                if A[n][i] ~= 0 then
                    for j = 1, 6 do A[i][j] = A[i][j] + A[n][j]; Ai[i][j] = Ai[i][j] + Ai[n][j] end break end
            end
        end
        
        local k = 1 / A[i][i]; for j = 1, 6 do A[i][j] = A[i][j] * k; Ai[i][j] = Ai[i][j] * k end
        
        for n = i + 1, 6 do
            if A[n][i] ~= 0 then
                local k = A[n][i] / A[i][i]
                for j = 1, 6 do A[n][j] = A[n][j] / k - A[i][j]; Ai[n][j] = Ai[n][j] / k - Ai[i][j] end
            end
        end
    end
    
    for i = 6, 2, -1 do
        for n = i - 1, 1, -1 do
            local k = A[n][i] / A[i][i]
            A[n][i] = 0; for j = 1, 6 do Ai[n][j] = Ai[n][j] - Ai[i][j] * k end
        end
    end
    
    local result = {}
    for i = 1, 6 do
        local r = 0; for j = 1, 6 do r = r + Ai[i][j] * B[j] end
        table.insert(result, r)
    end
    
    return result end

local result = solve_p2()
print(string.format("Part 2: %.0f", result[1] + result[2] + result[3])) -- hopefully this rounding works for any input