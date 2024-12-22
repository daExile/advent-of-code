local input = io.open("../__in/17.txt", "r"):read("*a")
local input_pattern = ".-A: (%d+).-B: (%d+).-C: (%d+).-Program: ([%d,]+)"

local function bitxor(a, b)
    local place_val, r = 1, 0
    
    repeat
        r, a, b, place_val = r + ((a % 2 + b % 2) % 2) * place_val, math.floor(a / 2), math.floor(b / 2), place_val * 2
    until a == 0 and b == 0
    
    return r
end

local function run(regs, program)
    local ptr, combo, out = 1, {[4] = "a", [5] = "b", [6] = "c"}, {}
    
    local op = {
        [0] = function(x) regs.a = math.floor(regs.a / (2 ^ (regs[combo[x]] or x)));    ptr = ptr + 2 end,
        [1] = function(x) regs.b = bitxor(regs.b, x);                                   ptr = ptr + 2 end,
        [2] = function(x) regs.b = (regs[combo[x]] or x) % 8;                           ptr = ptr + 2 end,
        [3] = function(x) ptr = (regs.a ~= 0 and x + 1) or (ptr + 2) end;
        [4] = function(x) regs.b = bitxor(regs.b, regs.c);                              ptr = ptr + 2 end,
        [5] = function(x) table.insert(out, (regs[combo[x]] or x) % 8)                  ptr = ptr + 2 end,
        [6] = function(x) regs.b = math.floor(regs.a / (2 ^ (regs[combo[x]] or x)));    ptr = ptr + 2 end,
        [7] = function(x) regs.c = math.floor(regs.a / (2 ^ (regs[combo[x]] or x)));    ptr = ptr + 2 end
    }
    
    while program[ptr] do op[program[ptr]](program[ptr + 1]) end
    return out
end

local function match_search(regs, program, step, k)
    step, k = step or #program, k or 0
    
    for i = (step == #program and 1 or 0), 7 do
        if (run({a = i + k, b = regs.b, c = regs.c}, program))[1] == program[step] then
            if step > 1 then
                local m = match_search(regs, program, step - 1, (k + i) * 8)
                if m then return m end
            else
                return k + i
            end
        end
    end
    
    return nil
end

local a, b, c, program_str = input:match(input_pattern); a, b, c = tonumber(a), tonumber(b), tonumber(c)

local program = {}
for n in program_str:gmatch("%d+") do table.insert(program, tonumber(n)) end

print(string.format("Part 1: %s", table.concat(run({a = a, b = b, c = c}, program), ",")))

local match = match_search({a = a, b = b, c = c}, program)
print(string.format("Part 2: " .. (string.format("%.0f", match) or "solution not found")))                                            