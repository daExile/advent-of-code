# Advent of Code 2017 
### 30:star:
Being done in Lua and Kotlin in parallel, learning the former from scratch and learning more of / practicing the latter. Plus, they have a nice contrast in amount of built-in features.
## Thoughts on...
```
TODO( write [more of] something mildly interesting on days 01-10 )
```
## Day 01 - [Inverse Captcha](https://adventofcode.com/2017/day/1)
- **Kotlin**
  - Simply parsing the input into a list of Int, and then comparing them by given rules. For fun I wanted to create custom List variant that would loop on its own, without doing `% list.size`, but seems like I don't have the knowledge for it yet.
- **Lua**
  - For a very first Lua code, as straightforward as it gets - read the input, compare its digits in pairs, get answers. No built-in string indexing, so I made a silly function for that, also indexing from 1 does seem like a cool idea to me, but here it needed a bit of workaround to avoid getting 0 at the end. Oh well.
  - Reckoned the function that gets one symbol as a substring of input might not be optimal. Replacing that with input converted to a char table and dealing with it by indices turned out to be about 10x faster. Other stuff (parsing only half of input for part 2 separately or with extra `if i <= len / 2`) yielded no improvement so far, though. 

### ...

## Day 07 - [Recursive Circus](https://adventofcode.com/2017/day/7)
- **Kotlin**
  - Part 1 comes down to parsing input into some structure and then finding the only entry in it that doesn't have an underlying "program". Part 2, well, slightly more complicated, I kept adding "features" to the data structure and working with them in what seems to be a really clumsy way. But it worked, onwards to Lua, hoping to coming up with much better ideas there.
- **Lua**
  - Same idea but somewhat cleaner (at least it looks like that, to me). Go up from the root of program tree, checking if every branch joint has equal weights, pass down its total weight if true, find the outlier, save its name + weight delta, and fall out of recursion if false.
- **Kotlin**
  - Ported Lua code for unbalanced "floor" search, pretty much, looks somewhat better to me now.

## Day 08 - [I Heard You Like Registers](https://adventofcode.com/2017/day/8)
Assembly puzzle :heart: This time it's rather simple processing, no loops involved, so we can go through it line by line and keep track of registers, only needs capturing all the args in a convenient way, and some sort of a switch for conditional checks.

**Lua**: I opted for using a table of functions for makeshift switch here. I did try a six-store `if-then-elseif` construction instead, out of curiosity, the performance was very similar.

## Day 09 - [Stream Processing](https://adventofcode.com/2017/day/9)
Regular expression day, brings back memories of doing stuff like this manually in Python for the first time :)

Anyway, we're tasked with cleaning input stream of some garbage in two stages. First, getting rid of already cancelled symbols marked with `!`, then, garbage sequences enclosed in `<>`. While Kotlin uses just regular regex (doubly regular heh), Lua does its own take on patterns, but they turned out to be exact same for both.
- `"!."` for searching for cancelled symbols, replacing the matches with empty strings.
- `"<[^>]*>"` for garbage sequences, again, replacing with nothing.

To calculate the answer (sum of individual group scores that match their level of "containment" in other groups), input cleanup result is iterated over its length. Since we know that all groups "are nicely formed", no need to check if anything's closed correctly, etc. Just two variables, one to keep track of group embed level (+1 on encountering `{`, -1 on `}`), other to accumulate group score (+group level on `{`).
**Lua**: converting the input string into a table for parsing.

Part 2 asks to find out how much garbage was dumped out at the second cleanup stage... without its marker `<>` brackets. So, gotta go back and adjust the second filter to keep those intact (replace sequences with `"<>"` instead of empty strings), and find the diff in input size before and after this step.

...But this is again linear stuff, should give parsing the stream manually a try, too, and compare performance.
## Day 10 - [Knot Hash](https://adventofcode.com/2017/day/10)
The task this time is to take a list of numbers from 0 to 255 and transform it repeatedly - namely, reverse lengthy parts of it, according to input data. The list also wraps around.

**Lua**: I went with simply copying the needed part into a proxy table and putting it back in reverse. Since it's done one by one element, wrapping around the table is easily done with `index % size` (with some extras for indexing from 1). Guess it could be done in another way (using some sort of a linked list structure?), but outright table manipulation was easier to code, and in this case works fast enough.

...Woah, part 2 brings plenty of new things to do. Treating input string as char sequence instead of parsing it for numbers, rearranging the code to turn part 1 solution into a function to call it repeatedly for 64 rounds, finally, making the hash calculations. What makes it a bit more difficult, methinks, is the fact that you can only check it against given test cases when it's all done.

**Lua**: And that's where things got silly. There's no built-in xor, so it needed to be done from scratch (or imported from somewhere, I guess). So I made it, except I got the result assembly wrong in the first version.
```lua
function bitxor(a, b)
    local r = 0
    for i = 0, 7 do r, a, b = r + (a + b) % 2 * (2 ^ i), math.floor(a / 2), math.floor(b / 2) end
    -- for some reason I though this would be ok
    --          ... r, a, b = 2 * r + (a + b) % 2 ...
    return r end
```
Wouldn't be a difficult to spot problem, normally, but the check was done using the given example of `65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64`, for first two numbers and the whole thing, once the hashing function was also put in place. Just so happens that reverse bit order gives correct result for both of these inputs. Do more checks, will ya :)

**Kotlin**: Now for something completely different, here we can use all built-in good stuff - init lists with a constructor; rotate the list to new starting point then flip its first N elements to avoid dealing with wrapping around entirely, while tracking current offset to rotate the list back to what should be 0 as starting index, once knot-hashing is done); and so on. `denseHash()` could use more scope function magic, but it's a bit too tricky for now.
## Day 11 - [Hex Ed](https://adventofcode.com/2017/day/11)
This is a hex grid traversal puzzle, which calls for some coordinate system setup. I chose a relatively lazy approach for the first language (it was **Kotlin** today), to represent it as a skewed square grid with an extra degree of freedom, moving along one of diagonals is allowed, too. The choice of direction for x/y axis is arbitrary, for traversal itself it won't matter anyway. 
```
            Y
         \  ¦  /
          +-¦-+  
   \     /  ¦  \     /
    +---+  0,1  +---+   X
   /     \  ¦  /     .'
 -+ -1,1  +-¦-+  1,0  +-
   \     /  ¦  .'    /
    +---+  0,0  +---+
   /     \     /     \
 -+ -1,0  +---+  1,-1 +-
   \     /     \     /
    +---+  0,-1 +---+
   /     \     /     \
          +---+
         /     \
```
The next step is to map each step direction to its corresponding coordinate change:
```kotlin
val move = mapOf(
    "n" to Pair(0, 1),
    "ne" to Pair(1, 0),
    "se" to Pair(1, -1),
    "s" to Pair(0, -1),
    "sw" to Pair(-1, 0),
    "nw" to Pair(-1, 1)
)
```
And we're ready to start at `(0, 0)` and iterate over our input, adding deltas for each step to get the final tile coordinates.

Now all that's left is to find the Manhattan distance to it on a hex grid...
```
                +---+
               / 0,2 \
          +---+   o   +---+
         -1,2  \  ¦  / 1,1 \
    +---+   o   +-¦-+   o   +---+
   /     \    `.  ¦  \  ¦  / 2,0 \
 -2,2 o   +---+  `¦   +-¦-+   o   +
   \    `.        ¦     ¦  .'    /
    +---+  `.   +-¦-+   .'  +---+
   /     \    `.  ¦  .'     
 -2,1 o   +   +  `@'  +   +
   \    `.     .'    /
    +---+  `.'  +---+
   /     .'  
 -2,0 o'  +   +
   \     /
    +---+
```
As you can see here, the twist is that in "quadrants" that don't match the allowed diagonal movement, the distance is the usual sum of coordinates' absolute values. Where it is allowed, we only need the maximum of the two. So, all needed here is a conditional check, whether the signs of two coordinates are same or n-nope.
```kotlin
fun hexManhattanDist(pos: Pair<Int, Int>): Int {
    return if (pos.first.sign == pos.second.sign) {
        abs(pos.first) + abs(pos.second)
    } else max(abs(pos.first), abs(pos.second))
}
```
Part 2 asks for a distance to the farthest from origin visited tile. No problem, all that's needed is to call the distance function for each step and keep track of its maximum.

For the second language (**Lua**), I decided to do something that treats hex grid as, well, hex grid.
```
            A
         \  ¦  /
          +-¦-+  
   \     /  ¦  \     /
    +---+ 1,0,0 +---+
   /     \  ¦  /     \
 -+       +-¦-+    <----- this is a 1,1,0 tile. Or 0,0,-1 :)
   \     /  ¦  \     /
    +---+ 0,0,0 +---+
   /     .'   `.     \
 -+ 0,0,1 +---+ 0,1,0 +-
   .'    /     \    `.
C'  +---+       +---+  `B
   /     \     /     \
          +---+
         /     \
```
```lua
move = {n = {1, 0, 0},
        ne = {0, 0, -1},
        se = {0, 1, 0},
        s = {-1, 0, 0},
        sw = {0, 0, 1},
        nw = {0, -1, 0}}
```
Strictly speaking, that wouldn't be a proper coordinate system, as each tile is not uniquely defined by a certain set of numbers. But sets of numbers are still unique to the tiles, and bringing the coordinates to `(n1 >= 0, n2 = 0, n3 <= 0)` form allows for easy Manhattan distance calculation.
```lua
function reduce(t)
    local tmp = {}; for i = 1, 3 do table.insert(tmp, t[i]) end
    table.sort(tmp); local delta = tmp[2]
    
    for i = 1, 3 do tmp[i] = t[i] - delta end
    return tmp end

function hexmd(t) return math.abs(t[1] - t[2] - t[3]) end
```
The rest of the code does pretty much the same as before - routinely adds each step's coordinate change and checks distance to origin.
## Day 12 - [Digital Plumber](https://adventofcode.com/2017/day/12)
A graphs problem, where we're given a list of nodes and their links, and need to find the number of nodes in a subgraph containing node `0`. So far, however, it looks like implementing a graph structure isn't required.

**Lua**: I'm using two global tables, `pipes` to store input data, and `links` as a set of nodes that are already accounted for. We're doing depth-first search for connected nodes using a recursive function, that reads linked IDs from `pipes[ID]` and calls itself to read their links, skips those already in the list and adds those that aren't:
```lua
function getlinks(name)
    if not links[name] then
        links[name] = true
        for _, v in ipairs(pipes[name]) do getlinks(v) end
    end
end
```
After it's done its job, all we need is resulting `links` size.

Now, part 2 is asking to find the number of isolated subgraphs in the whole thing. I went for collecting all subgraphs' data into `groups` table which will store `links` tables from each search, and added another table to track all IDs seen in searches. Now we can do the group search over the whole input data, skipping IDs that we already discovered a group for:
```lua
for name, _ in pairs(pipes) do
    if not log[name] then
        local links = getlinks(name, {})
        table.insert(groups, links)
    end
end
```
`getlinks()` function was also modified, to start new search with an empty group, add found IDs to new global `log` as well, and return the result.
```lua
function getlinks(name, links)
    links[name] = true; log[name] = true
    for _, v in ipairs(pipes[name]) do
        if not links[v] then getlinks(v, links) end end
    return links end
```
And the answer is the size of `groups`. Could do a simple count, instead, but with all group data, part 1 solution is incorporated in it, too, we simply print the size of first group in `groups` as its search starts with node `0`.

For **Kotlin** I made some pretty lazy Graph class implementation, for now only with things required to solve this day (and a BFS search instead, for a change). I totally expect it to be useful (and needing updates / enhancements) at some point later on, for a route-searching puzzle. We'll see. Nothing to write home about, otherwise.
## Day 13 - [Packet Scanners](https://adventofcode.com/2017/day/13)
Here we have a firewall setup for an input, a list of `depths` (a distance to each scanner in the structure) and matching `ranges` (a scanner's route length). The scanners all start at position `0` and move one step at a time until the end of their routes, then go back in the same manner, while we're moving at the same pace across the "firewall" at level `0`. Parsing this into some structure...
```kotlin
class SecurityScanner(val depth: Int, val range: Int)
```
```kotlin
val firewall = File("13.txt").readLines()
    .map { line -> line.split(": ").map { it.toInt() } }
    .map { SecurityScanner(it[0], it[1]) }
```
I added this after getting the answers for the first time, though, because parsing input in a loop turned out to be bad idea, surprise, surprise. Anyway! Part 1, basically, asks to find which scanners would spot us if we'd move out immediately, and answer with sum of those scanners' `depth * range`. As scanners take `period = 2 * (range - 1)` steps to do a full rotation, we can take `depth mod period` and compare to `0` to see if we'll be spotted.
```kotlin
var severity = 0
for (layer in firewall) {
    severity += if (layer.depth % (2 * (layer.range - 1)) == 0) layer.depth * layer.range else 0
}
```
Second part of the puzzle is the search for such a starting delay that would allow us to cross the firewall without being caught at all. Normally this would call for using math to cut corners, but I didn't see any clear cut to it. Other [similarly](https://adventofcode.com/2016/day/15) [looking](https://adventofcode.com/2020/day/13) puzzles in AoC asked us to do the opposite, the equivalent of getting caught by every single scanner, but that approach won't work here (there is number of scanners with matching ranges, but placed at distances not matching their period, see `4` and `6` in provided example), and even if it would, no way to tell if the solution was optimal (and quite likely it wasn't).

So I opted for an outright iteration this time (it gets the answer pretty fast anyway, after optimising the code a little bit). At first I reused the severity score function for the search, but the result was too low - ri-ight, first firewall layer has a score of `0` regardless of getting caught or not. The second attempt uses a boolean instead:
```kotlin
var delay = 0
do {
    var caught = false
    delay++
    for (layer in firewall) {
        caught = (delay + layer.depth) % (2 * (layer.range - 1)) == 0
        if (caught) break
    }
} while (caught)
```
Skipping to next value as soon as we're caught is one obvious shortcut, another was stopping being silly and making some data structure to store input data instead of parsing it every round (yup, at first it was like that, and about 20x slower). For this particular solution, I reckon there are ways to make it faster and / or shorter with more Kotlin-ising, saving period value as another property, grouping scanners by their period and reducing maximum number of checks per delay. Gonna try that later if I don't come up with some better algorithm altogether.
## Day 14 - [Disk Defragmentation](https://adventofcode.com/2017/day/14)
Knot hashing from day 10 is back! We're using its part 2 algorithm to build a 128x128 bitmap, for which a couple new things are needed. One is simple, to provide keys for hashing in form of `input string + '-' + row number`, and do it for 128 rows.
```lua
map = {}
for i = 0, 127 do
    local key = {}
    for _, v in ipairs(stuff.str2anychartable(input.."-"..i)) do table.insert(key, string.byte(v)) end
    for _, v in ipairs({17, 31, 73, 47, 23}) do table.insert(key, v) end
    
    table.insert(map, stuff.str2anychartable(stuff.densehash(stuff.knothash(stuff.init(), key, 64), bin)))
end
```
```kotlin
val map = List(128) {
    i -> denseHash(knotHash(List(256) { j -> j }, ("$input-$i").map { it.code } + listOf(17, 31, 73, 47, 23), 64), ::toBinaryString)
}
```
**Lua** and **Kotlin** ways. Second, to get a bitmap, we need a binary representation of the result instead of hex... yeah, **Lua** doesn't seem to have it so I had to invent some mediocre function for it:
```lua
function bin(n)
    local str = ""
    for i = 0, 7 do str, n = str..n % 2, math.floor(n / 2) end
    return string.reverse(str) end
```
Room for improvement, but again, it was fast enough for the purpose. In **Kotlin** I made a function for it, too, could have put it directly into the `denseHash()` call but it was getting crowded already :)
```kotlin
fun toBinaryString(n: Int) = n.toString(2).padStart(8, '0')
```
If we need more decimal to binary conversions further down the road, I'll likely update both to handle numbers of bits different from 8.

Part 1 asks to count the total of `1`s in the final map. For **Kotlin**, I added `.also { count1s += it.count { it == '1' } }` to `denseHash()` call, for **Lua** I used pattern matching to get each row's length with all `0`s removed:
```lua
for _, row in ipairs(map) do count = count + #string.gsub(table.concat(row), "0", "") end
```
The task for part 2 is to count regions the `1`s form on our generated map. For this, I repurposed some chunks of day 12 code, changing it from just reading the data for all connected nodes to neighbours check. Both solutions are using the same approach they did in day 12. Recursive function called for each not encountered yet `1` on a map for **Lua**...
```lua
neighbour_deltas = {{x = 1, y = 0}, {x = 0, y = 1}, {x = -1, y = 0}, {x = 0, y = -1}}
function markregion(i, j)
    checked[i.." "..j] = true
    for _, n in ipairs(neighbour_deltas) do
        if map[i + n.x] and map[i + n.x][j + n.y] == "1" and not checked[i + n.x.." "..j + n.y] then
            markregion(i + n.x, j + n.y)
        end
    end
end

checked, count = {}, 0
for i, row in ipairs(map) do
    for j, tile in ipairs(row) do
        if not checked[i.." "..j] and tile == "1" then
            count = count + 1
            markregion(i, j)
        end
    end
end
```
**Kotlin** in turn got its BFS approach, but honestly I'm not happy enough with it to put it here in [this](https://github.com/daExile/advent-of-code/blob/main/2017/kotlin/day14.kt) clunky state. It works, though.
### Background
As this marks the first time one day refers to solution of another, I moved those code chunks to "helper libraries". **Kotlin** happily picks contents from any file in the project as is, I moved all hashing functions for clarity anyway, and the little `Pair<Int, Int>`-adding convenience bit, too.
```kotlin
operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>) = Pair(this.first + other.first, this.second + other.second)
```
...and added a format parameter to the `denseHash()`.

In **Lua**, old table manipulation approach was taking almost a whole second to find day 14 solution (after all, we're doing 128 times the work of day 10), which felt too slow. I decided to try something else - well, namely use **Kotlin** solution ideas but with strings instead of lists / tables, as Lua 5.1 doesn't yet have `table.move()`, and the result turned out to be about twice as fast. Seems that however fast working with tables is, the sheer number of operations outweighs it here.

All the new functions are in [stuff.lua](https://github.com/daExile/advent-of-code/blob/main/2017/lua/stuff.lua), old code is in [day10's history](https://github.com/daExile/advent-of-code/blob/f86fcd49a1054f1e16f67b64723ac888f1e6b891/2017/lua/day10.lua) because I had to make an indecisive mess while moving functions around.
## Day 15 - [Dueling Generators](https://adventofcode.com/2017/day/15)
...proper writeup attempt later, just the code for now.