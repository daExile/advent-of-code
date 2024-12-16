local robots = {}
local size_x, size_y = 101, 103 -- 11, 7 -- for test example
local room = {}


for line in io.lines("../__in/14.txt") do
    local x, y, vx, vy = line:match("p=([%-%d]+),([%-%d]+) v=([%-%d]+),([%-%d]+)")
    table.insert(robots, {x = tonumber(x), y = tonumber(y), vx = tonumber(vx), vy = tonumber(vy)})
end

local safety, best_x, best_y = {[0] = 0, 0, 0, 0}
for i = 1, 103 do
    local scores_x, scores_y = {}, {}
    
    for _, r in ipairs(robots) do
        r.x, r.y = (r.x + r.vx) % size_x, (r.y + r.vy) % size_y
        scores_x[r.x], scores_y[r.y] = (scores_x[r.x] or 0) + 1, (scores_y[r.y] or 0) + 1
        
        if i == 100 and r.x ~= (size_x - 1) / 2 and r.y ~= (size_y - 1) / 2 then
            local q = (r.x > (size_x - 1) / 2 and 1 or 0) + (r.y > (size_y - 1) / 2 and 2 or 0)
            safety[q] = safety[q] + 1
        end
    end
    
    local sum_x2, sum_y2 = 0, 0
    
    for _, v in pairs(scores_x) do sum_x2 = sum_x2 + v ^ 2 end
    if not best_x or sum_x2 > best_x.score then best_x = {score = sum_x2, i = i} end
        
    for _, v in pairs(scores_y) do sum_y2 = sum_y2 + v ^ 2 end    
    if not best_y or sum_y2 > best_y.score then best_y = {score = sum_y2, i = i} end
end

print(string.format("Part 1: %d", safety[0] * safety[1] * safety[2] * safety[3]))

local t = best_x.i; while t % size_y ~= best_y.i do t = t + size_x end
print(string.format("Part 2: %d", t))