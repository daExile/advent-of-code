local code, mem = {}, {}

local function get(ptr) return mem[ptr] or code[ptr] end

local function run()
    local ptr = 0
    while get(ptr) ~= 99 do
        if get(ptr) == 1 then mem[get(ptr + 3)] = get(get(ptr + 1)) + get(get(ptr + 2))
        elseif get(ptr) == 2 then mem[get(ptr + 3)] = get(get(ptr + 1)) * get(get(ptr + 2)) end
        ptr = ptr + 4
    end
end

local function nvsearch(target)
    for noun = 0, 99 do
        for verb = 0, 99 do
            mem = {noun, verb}; run()
            
            if get(0) == target then return 100 * noun + verb end
        end end end

local n = 0
for item in string.gmatch(io.open("../__in/02.txt", "r"):read(), "[%d%-]+") do code[n] = tonumber(item); n = n + 1 end

mem = {12, 2}; run()
print(string.format("Part 1: %d", get(0)))
print(string.format("Part 2: %d", nvsearch(19690720)))