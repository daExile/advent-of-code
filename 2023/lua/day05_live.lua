local almanac = io.open("../__in/05.txt", "r"):lines()

local function map(table, id)
    for _, rule in ipairs(table) do
        if id >= rule[1] and id <= rule[2] then return id + rule[3] end end
    return id end

local seeds = {}
for line in almanac do
    if line == "" then break end
    for item in string.gmatch(line, "([%d]+)") do table.insert(seeds, tonumber(item)) end end

local soil = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(soil, {from, to, shift}) end end

local fert = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(fert, {from, to, shift}) end end

local water = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(water, {from, to, shift}) end end

local light = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(light, {from, to, shift}) end end

local temp = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(temp, {from, to, shift}) end end

local humid = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(humid, {from, to, shift}) end end

local loc = {}
for line in almanac do
    if line == "" then break end
    for _target, _id, _range in string.gmatch(line, "([%d]+) ([%d]+) ([%d]+)") do
        local from, to, shift = tonumber(_id), tonumber(_id) + tonumber(_range) - 1, tonumber(_target) - tonumber(_id)
        table.insert(loc, {from, to, shift}) end end

local loc_p1, loc_p2
for _, id in ipairs(seeds) do
    t = map(loc, map(humid, map(temp, map(light, map(water, map(fert, map(soil, id)))))))
    if not loc_p1 or t < loc_p1 then loc_p1 = t end end

print(string.format("Part 1: %d", loc_p1))

for i = 1, #seeds, 2 do
    print(seeds[i], seeds[i + 1])
    for id = seeds[i], seeds[i] + seeds[i + 1] - 1 do
        t = map(loc, map(humid, map(temp, map(light, map(water, map(fert, map(soil, id)))))))
        if not loc_p2 or t < loc_p2 then loc_p2 = t end end end

print(string.format("Part 2: %d", loc_p2))