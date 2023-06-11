Prog = {}               -- "class" for single program, part 1

function Prog:new()
    newobj = {regs = {}, ptr = 1}
    self.__index = self
    return setmetatable(newobj, self) end

function Prog:get(x) return self.regs[x] or x end

function Prog:snd(x) self.regs["snd"] = self:get(x) end
function Prog:rcv(x) if self:get(x) ~= 0 then self.regs["rcv"] = self.regs["snd"] end end
function Prog:set(r, x) self.regs[r] = self:get(x) end
function Prog:add(r, x) self.regs[r] = (self.regs[r] or 0) + self:get(x) end
function Prog:mul(r, x) self.regs[r] = (self.regs[r] or 0) * self:get(x) end
function Prog:mod(r, x) self.regs[r] = (self.regs[r] or 0) % self:get(x) end
function Prog:jgz(x, y) if self:get(x) > 0 then self.ptr = self.ptr + self:get(y) - 1 end end
                                        -- workaround for pointer++ in main loop ---^
ProgThread = Prog:new() -- "class" for thread, for multithreaded part 2

function ProgThread:new(id, t_id)
  newobj = {regs = {["p"] = id}, queue = {}, target = t_id, wait = false}
  self.__index = self
  return setmetatable(newobj, self)
end

function ProgThread:snd(x, pr)
    table.insert(pr[self.target].queue, 1, self:get(x))
    self.regs["snd"] = (self.regs["snd"] or 0) + 1 end
function ProgThread:rcv(x)
    if #self.queue > 0 then self.regs[x] = table.remove(self.queue); self.wait = false
    else self.wait = true end end

ops = { ["snd"] = function(pr, id, x) pr[id]:snd(x, pr) end,
        ["rcv"] = function(pr, id, x) pr[id]:rcv(x) end,
        ["set"] = function(pr, id, r, x) pr[id]:set(r, x) end,
        ["add"] = function(pr, id, r, x) pr[id]:add(r, x) end,
        ["mul"] = function(pr, id, r, x) pr[id]:mul(r, x) end,
        ["mod"] = function(pr, id, r, x) pr[id]:mod(r, x) end,
        ["jgz"] = function(pr, id, x, y) pr[id]:jgz(x, y) end }

input = {}
for line in io.lines("18.txt") do
    local t = {}
    for item in string.gmatch(line, "([%w-]+)") do table.insert(t, tonumber(item) or item) end
    table.insert(input, t)
end

p1 = {Prog:new()}                                             -- running part 1
while input[p1[1].ptr] do
    local t = input[p1[1].ptr]
    ops[t[1]](p1, 1, t[2], t[3])
    
    if p1[1].regs["rcv"] then break end
    p1[1].ptr = p1[1].ptr + 1 end

p2 = {[0] = ProgThread:new(0, 1), [1] = ProgThread:new(1, 0)} -- running part 2
repeat
    live = 0
    for n = 0, 1 do
        if input[p2[n].ptr] then
            local t = input[p2[n].ptr]
            ops[t[1]](p2, n, t[2], t[3])
        
            if not p2[n].wait then live = live + 1; p2[n].ptr = p2[n].ptr + 1 end
        end
    end
until live == 0

print(string.format("Part 1: %d", p1[1].regs["rcv"]))
print(string.format("Part 2: %d", p2[1].regs["snd"]))