# Advent of Code 2017 
### 20:star:
Being done in Lua and Kotlin in parallel, learning the former from scratch and learning more of / practicing the latter. Plus, they have a nice contrast in amount of built-in features.
## Thoughts on...
### Day 01 - Inverse Captcha
- **Kotlin**
  - Simply parsing the input into a list of Int, and then comparing them by given rules. For fun I wanted to create custom List variant that would loop on its own, without doing `% list.size`, but seems like I don't have the knowledge for it yet.
- **Lua**
  - For a very first Lua code, as straightforward as it gets - read the input, compare its digits in pairs, get answers. No built-in string indexing, so I made a silly function for that, also indexing from 1 does seem like a cool idea to me, but here it needed a bit of workaround to avoid getting 0 at the end. Oh well.
  - Reckoned the function that gets one symbol as a substring of input might not be optimal. Replacing that with input converted to a char table and dealing with it by indices turned out to be about 10x faster. Other stuff (parsing only half of input for part 2 separately or with extra `if i <= len / 2`) yielded no improvement so far, though. 

### ...

### Day 07 - Recursive Circus
- **Kotlin**
  - Part 1 comes down to parsing input into some structure and then finding the only entry in it that doesn't have an underlying "program". Part 2, well, slightly more complicated, I kept adding "features" to the data structure and working with them in what seems to be a really clumsy way. But it worked, onwards to Lua, hoping to coming up with much better ideas there.
- **Lua**
  - Same idea but somewhat cleaner (at least it looks like that, to me). Go up from the root of program tree, checking if every branch joint has equal weights, pass down its total weight if true, find the outlier, save its name + weight delta, and fall out of recursion if false.
- **Kotlin**
  - Ported Lua code for unbalanced "floor" search, pretty much, looks somewhat better to me now.

### Day 08 - I Heard You Like Registers
Assembly puzzle :heart: This time it's rather simple processing, no loops involved, so we can go through it line by line and keep track of registers, only needs capturing all the args in a convenient way, and some sort of a switch for conditional checks.

**Lua**: I opted for using a table of functions for makeshift switch here. I did try a six-store `if-then-elseif` construction instead, out of curiosity, the performance was very similar.

### Day 09 - Stream Processing
Regular expression day, brings back memories of doing stuff like this manually in Python for the first time :)

Anyway, we're tasked with cleaning input stream of some garbage in two stages. First, getting rid of already cancelled symbols marked with `!`, then, garbage sequences enclosed in `<>`. While Kotlin uses just regular regex (doubly regular heh), Lua does its own take on patterns, but they turned out to be exact same for both.
- `"!."` for searching for cancelled symbols, replacing the matches with empty strings.
- `"<[^>]*>"` for garbage sequences, again, replacing with nothing.

To calculate the answer (sum of individual group scores that match their level of "containment" in other groups), input cleanup result is iterated over its length. Since we know that all groups "are nicely formed", no need to check if anything's closed correctly, etc. Just two variables, one to keep track of group embed level (+1 on encountering `{`, -1 on `}`), other to accumulate group score (+group level on `{`).
**Lua**: converting the input string into a table for parsing.

Part 2 asks to find out how much garbage was dumped out at the second cleanup stage... without its marker `<>` brackets. So, gotta go back and adjust the second filter to keep those intact (replace sequences with `"<>"` instead of empty strings), and find the diff in input size before and after this step.

...But this is again linear stuff, should give parsing the stream manually a try, too, and compare performance.
### Day 10 - Knot Hash
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