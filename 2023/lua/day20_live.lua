local modules, queue = {}, {}
for line in io.lines("../__in/20.txt") do
    local prefix, id, outs = string.match(line, "([&%%]?)([%w]+) %-> ([%w%s,]+)")
    if not modules[id] then modules[id] = {prefix, {}, {}, 0} else modules[id][1] = prefix end
    
    for id_out in string.gmatch(outs, "([%w]+)") do
        table.insert(modules[id][2], id_out)
        
        if not modules[id_out] then modules[id_out] = {"", {}, {}, 0} end
        modules[id_out][3][id] = 0
    end
end

-- part 2 dumb hack, assuming "n conj modules -> 1 conj module -> rx" structure is always true, and it loops nicely
local rx_ins, rx_low = {}, 0
for k, _ in pairs(modules["rx"][3]) do
    for k2, _ in pairs(modules[k][3]) do rx_ins[k2] = 0 end end

local pulses = {[0] = 0, [1] = 0}
local function push_the_button(x)
    local queue = {}
    
    -- button pulse
    pulses[0] = pulses[0] + 1
    for _, id_out in ipairs(modules["broadcaster"][2]) do table.insert(queue, {id_out, "broadcaster", 0}) end
    
    while #queue > 0 do
        local id, id_in, pulse = table.unpack(table.remove(queue, 1))
        pulses[pulse] = pulses[pulse] + 1
        
        if modules[id][1] == "%" and pulse == 0 then
            modules[id][4] = (modules[id][4] + 1) % 2
            for _, id_out in ipairs(modules[id][2]) do table.insert(queue, {id_out, id, modules[id][4]}) end
        elseif modules[id][1] == "&" then
            modules[id][3][id_in] = pulse
            
            local send = 0
            for k, v in pairs(modules[id][3]) do
                if not rx_ins[k] then -- more part2 dumb hack
                    if v == 0 then send = 1 break end
                else
                    if v == 0 then send = 1
                    elseif v == 1 and rx_ins[k] == 0 then rx_ins[k] = x end
                end
            end
            for _, id_out in ipairs(modules[id][2]) do
                table.insert(queue, {id_out, id, send})
            end
        end
    end
    
    rx_low = 1; for k, v in pairs(rx_ins) do rx_low = rx_low * v end -- last bit of part 2 dumb hack
end

local x = 0
repeat
    x = x + 1
    push_the_button(x)
    if x == 1000 then print(string.format("Part 1: %d", pulses[0] * pulses[1])) end
until x >= 1000 and rx_low > 0

print(string.format("Part 2: %.0f", rx_low))