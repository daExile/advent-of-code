local papers_hehe = io.open("../__in/08.txt", "r"):lines()

local function replace(r_or_l) if r_or_l == "L" then return 1 end return 2 end

local dirs = {}
for line in papers_hehe do
    if line == "" then break end
    for item in string.gmatch(line, "([RL])") do table.insert(dirs, replace(item)) end end

local maps, d_len = {}, #dirs
for line in papers_hehe do
    local node, left, right = string.match(line, "([%w]+) = %(([%w]+), ([%w]+)%)")
    maps[node] = {left, right} end

local function move(node, step) return maps[node][dirs[step % d_len + 1]] end

local function is_finished(node, target)
    if not string.match(node, target or "%w%wZ") then return false end
    return true end

local function factorise(n)
    local factors = {}
    repeat
        local old_n, lim = n, math.ceil(math.sqrt(n))
        for i = 2, lim do if n % i == 0 then factors[i] = (factors[i] or 0) + 1; n = n / i; break end end
        
        if old_n == n then factors[n] = (factors[n] or 0) + 1; n = 1 end
    until n == 1
    return factors end

local function lcm(numbers)
    local prime_factors, lcm = {}, 1
    
    for _, n in ipairs(numbers) do
        for k, v in pairs(factorise(n)) do prime_factors[k] = math.max(v, prime_factors[k] or 0) end end
    for k, v in pairs(prime_factors) do lcm = lcm * math.pow(k, v) end
    return lcm end

local starting_nodes, loop_sizes = {}, {}
for k, _ in pairs(maps) do if string.match(k, "%w%wA") then table.insert(starting_nodes, k) end end
for i, node in ipairs(starting_nodes) do
    local steps = 0
    repeat node = move(node, steps); steps = steps + 1 until is_finished(node)  
    
    if starting_nodes[i] == "AAA" then print(string.format("Part 1: %d", steps)) end
    table.insert(loop_sizes, steps)
end

print(string.format("Part 2: %s", tostring(lcm(loop_sizes)))) -- oops, %d can only do i32 it seems