Prog = {}

function Prog:new()
    newobj = {regs = {}, ptr = 1}
    self.__index = self
    return setmetatable(newobj, self) end

function Prog:get(x) return self.regs[x] or tonumber(x) or 0 end

function Prog:set(r, x) self.regs[r] = self:get(x) end
function Prog:sub(r, x) self.regs[r] = (self.regs[r] or 0) - self:get(x) end
function Prog:mul(r, x)
    self.regs[r] = (self.regs[r] or 0) * self:get(x)
    self.regs["mul"] = (self.regs["mul"] or 0) + 1 end
function Prog:jnz(x, y) if self:get(x) ~= 0 then self.ptr = self.ptr + self:get(y) - 1 end end

local ops = { ["set"] = function(prog, r, x) prog:set(r, x) end,
        ["sub"] = function(prog, r, x) prog:sub(r, x) end,
        ["mul"] = function(prog, r, x) prog:mul(r, x) end,
        ["jnz"] = function(prog, x, y) prog:jnz(x, y) end }

local input = {}
for line in io.lines("../__in/23.txt") do
    local t = {}
    for item in string.gmatch(line, "([%w-]+)") do table.insert(t, item) end
    table.insert(input, t)
end

-- part 1
local proc = Prog:new()
repeat
    local t = input[proc.ptr]
    ops[t[1]](proc, t[2], t[3])
        
    if not proc.wait then proc.ptr = proc.ptr + 1 end
until not input[proc.ptr]

-- translated into Lua and (somewhat) optimised part 2
local b = input[1][3] * input[5][3] - input[6][3] -- taking loop start, end, step size from puzzle input
local c = b - input[8][3]                         -- looks like only starting value of 'b' differs in inputs
local step = -input[#input - 1][3]                -- and the rest could've been hardcoded but a-a-a-anyway...

local count = 0
for i = b, c, step do
    for d = 2, math.sqrt(i) do if i % d == 0 then count = count + 1; break end end
end

print(string.format("Part 1: %d", proc.regs["mul"]))
print(string.format("Part 2: %d", count))