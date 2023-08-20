local stuff = require("stuff")

local function sign(n, null) if n > 0 then return 1 elseif n < 0 then return -1 end return null end

local function intersect(t1, t2)
    local out = {}
    for _, v1 in ipairs(t1) do for _, v2 in ipairs(t2) do if v1 == v2 then table.insert(out, v1) end end end
    return out end

local sqrts, max = {[0] = 0}, 0
local function intsqrt(n)
    if n > max then
        local t, tsq = sqrts[max]
        repeat t = t + 1; tsq = t * t; sqrts[tsq] = t until tsq >= n
        max = tsq end
    return sqrts[n] end

local function collide(p1, p2)
    local t, x
    for i = 1, 3 do
        local a = p1[6 + i] - p2[6 + i]
        local b = (p1[3 + i] - p2[3 + i]) * 2 + a
        local c = (p1[i] - p2[i]) * 2
        
        if a ~= 0 then
            local d = intsqrt(b * b - 4 * a * c); if not d then return nil end
            
            local roots = {}
            if (-b - d) % (2 * a) == 0 then x = (-b - d) / (2 * a); if x >= 0 then table.insert(roots, x) end end
            if (-b + d) % (2 * a) == 0 then x = (-b + d) / (2 * a); if x >= 0 then table.insert(roots, x) end end

            if #roots == 0 then return nil
            else if not t then t = roots else t = intersect(t, roots); if #t == 0 then return nil end end end
            
        elseif b ~= 0 then
            if c % b == 0 then x = -c / b end
            
            if not x or x < 0 then return nil
            else if not t then t = {x} else t = intersect(t, {x}); if #t == 0 then return nil end end end
            
        elseif c ~= 0 then return nil end
    end
    table.sort(t); return t[1] or 0 end
    
local particles = {}
for line in io.lines("20.txt") do table.insert(particles, stuff.str2numtable(line)) end

local a_cl, v_cl, p_cl, id_closest
for id, data in ipairs(particles) do
    local p, v, a, s = 0, 0, 0
    for i = 1, 3 do
        s = sign(data[6 + i]) or sign(data[3 + i]) or sign(data[i], 0)
        a = a + data[6 + i] * s; v = v + data[3 + i] * s; p = p + data[i] * s
    end

    if not a_cl or a < a_cl or (a == a_cl and (v < v_cl or (v == v_cl and p <= p_cl)))
        then a_cl = a; v_cl = v; p_cl = p; id_closest = id end
end

local n, boom = #particles, {}
for i = 1, n - 1 do
    if not boom[i] then for j = i + 1, n do
        if not boom[j] and collide(particles[i], particles[j]) then boom[i] = true; boom[j] = true end
    end end
end

print(string.format("Part 1: %d", id_closest - 1))
print(string.format("Part 2: %d", n - stuff.tablesize(boom)))