local function subst(c, p2)
    if c == "A" then return 14
    elseif c == "K" then return 13
    elseif c == "Q" then return 12
    elseif c == "J" then
        if p2 then return 1 else return 11 end
    elseif c == "T" then return 10 end
    return tonumber(c) end

local function eval(cards, p2)
    local count_cards, count_combos, val, j = {}, {0, 0, 0, 0, 0}, 0
    for card in string.gmatch(cards, "[%w%d]") do
        count_cards[card] = (count_cards[card] or 0) + 1
        val = val * 15; val = val + subst(card, p2) end
    
    for k, v in pairs(count_cards) do count_combos[v] = count_combos[v] + 1 end
    
    if p2 then j = count_cards["J"] end
    if j and j < 5 then
        local n = 6 - j
        count_combos[j] = count_combos[j] - 1
        repeat n = n - 1 until count_combos[n] > 0
        count_combos[n] = count_combos[n] - 1
        count_combos[n + j] = count_combos[n + j] + 1 end
    
    if count_combos[5] == 1 then return 7, val  -- crappy makeshift enum lol
    elseif count_combos[4] == 1 then return 6, val
    elseif count_combos[3] == 1 and count_combos[2] == 1 then return 5, val
    elseif count_combos[3] == 1 then return 4, val
    else return count_combos[2] + 1, val end end    

local function compare_hands(h1, h2)
    local type1, val1 = eval(h1[1]); local type2, val2 = eval(h2[1])
    return type1 < type2 or (type1 == type2 and val1 < val2) end

local function compare_hands_p2(h1, h2)
    local type1, val1 = eval(h1[1], true); local type2, val2 = eval(h2[1], true)
    return type1 < type2 or (type1 == type2 and val1 < val2) end

local hands = {}
for line in io.lines("../__in/07.txt") do
    local cards, bid = string.match(line, "([%w%d]+) (%d+)")
    table.insert(hands, {cards, tonumber(bid)})
end

table.sort(hands, compare_hands)
local score = 0; for i, v in ipairs(hands) do score = score + i * v[2] end
print(string.format("Part 1: %s", score))

table.sort(hands, compare_hands_p2)
score = 0; for i, v in ipairs(hands) do score = score + i * v[2] end
print(string.format("Part 2: %d", score))