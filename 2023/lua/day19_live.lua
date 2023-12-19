local input = io.open("../__in/19.txt", "r"):lines()
local works = {}

local function process(part)
    local work = "in"
    while work ~= "R" do
        local dest
        for _, step in ipairs(works[work]) do
            if not step[1] then dest = step[4]; break
            else
                local check
                if step[2] == ">" then check = part[step[1]] > step[3] else check = part[step[1]] < step[3] end
                if check then dest = step[4]; break end
            end
        end
        
        if dest == "A" then return(part["x"] + part["m"] + part["a"] + part["s"])
        else work = dest end
    end
    return 0 end

for line in input do
    if line == "" then break end
    local id, contents = string.match(line, "([%w]+){(.*)}")
    
    local flow = {}
    for item in string.gmatch(contents, "([^,]+)") do
        local crit, op, val, dest
        if string.match(item, ":") then crit, op, val, dest = string.match(item, "([xmas])([><])([%d]+):([%w]+)")
        else dest = item end
    
        table.insert(flow, {crit, op, tonumber(val), dest}) end
        
    works[id] = flow
end

local sum1 = 0
for line in input do
    local part = {}
    for category, rating in string.gmatch(line, "([xmas])=([%d]+)") do part[category] = tonumber(rating) end
    sum1 = sum1 + process(part)
end

print(string.format("Part 1: %d", sum1))

local function split(range, more_than)
    if range[2] <= more_than then return range, nil
    elseif range[1] > more_than then return nil, range end

    return {range[1], more_than}, {more_than + 1, range[2]} end

local function get_size(ranges)
    local p = 1
    for _, range in pairs(ranges) do p = p * (range[2] - range[1] + 1) end
    return p end

local sum2 = 0

local function process_ranges(ranges, work)
    if not work then work = "in" end
    
    if work == "A" then sum2 = sum2 + get_size(ranges)
    elseif work ~= "R" then
        for _, step in ipairs(works[work]) do
            if not ranges["x"] or not ranges["m"] or not ranges["a"] or not ranges["s"] then break end
            if step[1] then
                local ranges_copy = {["x"] = ranges["x"], ["m"] = ranges["m"], ["a"] = ranges["a"], ["s"] = ranges["s"]}
            
                local cut = step[2] == ">" and step[3] or step[3] - 1
                local sub_low, sub_hi = split(ranges[step[1]], cut)

                if step[2] == ">" then
                    ranges_copy[step[1]] = sub_hi; process_ranges(ranges_copy, step[4])
                    ranges[step[1]] = sub_low
                else
                    ranges_copy[step[1]] = sub_low; process_ranges(ranges_copy, step[4])
                    ranges[step[1]] = sub_hi
                end
            else process_ranges(ranges, step[4]) end end end end

process_ranges({["x"] = {1, 4000}, ["m"] = {1, 4000}, ["a"] = {1, 4000}, ["s"] = {1, 4000}})
print(string.format("Part 2: %d", sum2))