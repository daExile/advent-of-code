local stones = {}

local function count(stones)
    local total = 0; for stone, n in pairs(stones) do total = total + n end
    return total
end

local function blink(stones)
    local stones_new = {}
    
    for stone, n in pairs(stones) do
        if stone == 0 then
            stones_new[1] = (stones_new[1] or 0) + n
        else
            l = math.ceil(math.log10(stone + 1))
            if l % 2 == 0 then
                local k = 10 ^ (l / 2); local b = stone % k; local a = (stone - b) / k
                
                stones_new[a] = (stones_new[a] or 0) + n
                stones_new[b] = (stones_new[b] or 0) + n
            else
                stones_new[stone * 2024] = (stones_new[stone * 2024] or 0) + n
            end
        end
    end
    
    return stones_new
end

for n in io.open("../__in/11.txt"):read():gmatch("(%d+)") do stone = tonumber(n); stones[stone] = (stones[stone] or 0) + 1 end

for blinks = 1, 25 do stones = blink(stones) end
print(string.format("Part 1: %d", count(stones)))

for blinks = 26, 75 do stones = blink(stones) end
print(string.format("Part 2: %.0f", count(stones)))