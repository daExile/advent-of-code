module("stuff", package.seeall)

function stuff.str2table(str, pattern)
    local t = {}
    for item in string.gmatch(str, pattern) do
        if pattern == "%d+" then table.insert(t, tonumber(item)) else table.insert(t, item) end
    end
    return t end

function stuff.str2strtable(str) return stuff.str2table(str, "%w+") end

function stuff.str2numtable(str) return stuff.str2table(str, "%d+") end

function stuff.str2chartable(str) return stuff.str2table(str, "%w") end

function stuff.tableminmax(t)
    local min, max
    for _, item in ipairs(t) do
        if not min or item < min then min = item end
        if not max or item > max then max = item end
    end
    return {min, max} end

function stuff.tablemaxindex(t)
    local max, k
    for i, item in ipairs(t) do
        if not max or item > max then k, max = i, item end
    end
    return k end

function stuff.tablemax(t)
    local max
    for k, v in pairs(t) do if not max or v > max then max = v end end
    return max end

function stuff.tablesize(t)
    local size = 0
    for k, v in pairs(t) do size = size + 1 end
    return size end