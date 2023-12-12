Prog = {}               -- "class" for single thread, part 1

function Prog:new()
    newobj = {regs = {}, ptr = 1}
    self.__index = self
    return setmetatable(newobj, self) end

function Prog:get(x) return self.regs[x] or tonumber(x) or 0 end

function Prog:snd(x) self.regs["snd"] = self:get(x) end
function Prog:rcv(x) if self:get(x) ~= 0 then self.regs["rcv"] = self.regs["snd"]; self.ptr = -1 end end
function Prog:set(r, x) self.regs[r] = self:get(x) end  -- stop thread by setting pointer ----^ out of input
function Prog:add(r, x) self.regs[r] = (self.regs[r] or 0) + self:get(x) end
function Prog:mul(r, x) self.regs[r] = (self.regs[r] or 0) * self:get(x) end
function Prog:mod(r, x) self.regs[r] = (self.regs[r] or 0) % self:get(x) end
function Prog:jgz(x, y) if self:get(x) > 0 then self.ptr = self.ptr + self:get(y) - 1 end end
                                        -- workaround for pointer++ in main loop ---^
ProgThread = Prog:new() -- "class" with extras for multithreaded part 2

function ProgThread:new(p, q_out, q_in) -- i couldn't resist starting doing 0ut / 1n here, sorry, Lua
    newobj = {regs = {["p"] = p}, qs = {[0] = q_out, [1] = q_in}, wait = false}
    self.__index = self
    return setmetatable(newobj, self) end

function ProgThread:snd(x)
    table.insert(self.qs[0], 1, self:get(x))
    self.regs["snd"] = (self.regs["snd"] or 0) + 1 end
function ProgThread:rcv(x)
    if #self.qs[1] > 0 then self.regs[x] = table.remove(self.qs[1]); self.wait = false
    else self.wait = true end end

ops = { ["snd"] = function(prog, x) prog:snd(x) end,
        ["rcv"] = function(prog, x) prog:rcv(x) end,
        ["set"] = function(prog, r, x) prog:set(r, x) end,
        ["add"] = function(prog, r, x) prog:add(r, x) end,
        ["mul"] = function(prog, r, x) prog:mul(r, x) end,
        ["mod"] = function(prog, r, x) prog:mod(r, x) end,
        ["jgz"] = function(prog, x, y) prog:jgz(x, y) end }

local input = {}
for line in io.lines("../__in/18.txt") do
    local t = {}
    for item in string.gmatch(line, "([%w-]+)") do table.insert(t, item) end
    table.insert(input, t)
end

local qs = {{}, {}}       -- setting up runner for both parts, part 1: [1], part 2: [2, 3]
local progs, live = {Prog:new(), ProgThread:new(0, qs[1], qs[2]), ProgThread:new(1, qs[2], qs[1])}
repeat
    live = 0
    for n = 1, 3 do
        if input[progs[n].ptr] then
            local t = input[progs[n].ptr]
            ops[t[1]](progs[n], t[2], t[3])
        
            if not progs[n].wait then live = live + 1; progs[n].ptr = progs[n].ptr + 1 end
        end
    end
until live == 0

print(string.format("Part 1: %d", progs[1].regs["rcv"]))
print(string.format("Part 2: %d", progs[3].regs["snd"]))