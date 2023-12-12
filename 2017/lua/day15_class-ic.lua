-- alright, let's try Lua's class-like tables
Generator = {}

function Generator:new(f)
    newobj = {factor = f; value = 0}
    self.__index = self
    return setmetatable(newobj, self) end

function Generator:set(n) self.value = n end

function Generator:nextvalue()
    self.value = (self.value * self.factor) % 2147483647
    return self.value end
    
function Generator:nextmultiple(m)
    repeat self:nextvalue() until self.value % m == 0
    return self.value end

A = Generator:new(16807)
B = Generator:new(48271)

starters = {}
for line in io.lines("../__in/15.txt") do table.insert(starters, tonumber(string.match(line, "(%d+)"))) end

count1, count2 = 0, 0

A:set(starters[1]); B:set(starters[2])
for a = 1, 40000000 do if (A:nextvalue() - B:nextvalue()) % 65536 == 0 then count1 = count1 + 1 end end
print(string.format("Part 1: %d", count1))

A:set(starters[1]); B:set(starters[2])
for a = 1, 5000000 do if (A:nextmultiple(4) - B:nextmultiple(8)) % 65536 == 0 then count2 = count2 + 1 end end
print(string.format("Part 2: %d", count2))