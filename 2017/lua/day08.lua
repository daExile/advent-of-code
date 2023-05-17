require("stuff")

ops = { ["<"] = function(r, n) return regs[r] < n end,
        [">"] = function(r, n) return regs[r] > n end,
        ["<="] = function(r, n) return regs[r] <= n end,
        [">="] = function(r, n) return regs[r] >= n end,
        ["=="] = function(r, n) return regs[r] == n end,
        ["!="] = function(r, n) return regs[r] ~= n end }

regs, max = {}, 0
for line in io.lines("08.txt") do
    local r1, sign, n1, r2, op, n2 = string.match(line, "(%w+) (%w+) (%-?%d+) if (%w+) ([!<>=]=?) (%-?%d+)")
    if sign == "dec" then n1 = -n1 end
    
    if not regs[r1] then regs[r1] = 0 end
    if not regs[r2] then regs[r2] = 0 end
    if ops[op](r2, tonumber(n2)) then regs[r1] = regs[r1] + n1 end
    if regs[r1] > max then max = regs[r1] end
end

print(string.format("Part 1: %d", stuff.tablemax(regs)))
print(string.format("Part 2: %d", max))