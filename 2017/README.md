# Advent of Code 2017 
### 14:star:
Being done in Lua and Kotlin in parallel, learning the former from scratch and learning more of / practicing the latter. Plus, they have a nice contrast in amount of built-in features.
## Thoughts on...
### Day 01
- **Kotlin:**
  - Simply parsing the input into a list of Int, and then comparing them by given rules. For fun I wanted to create custom List variant that would loop on its own, without doing `% list.size`, but seems like I don't have the knowledge for it yet.
- **Lua:**
  - For a very first Lua code, as straightforward as it gets - read the input, compare its digits in pairs, get answers. No built-in string indexing, so I made a silly function for that, also indexing from 1 does seem like a cool idea to me, but here it needed a bit of workaround to avoid getting 0 at the end. Oh well.
  - Reckoned the function that gets one symbol as a substring of input might not be optimal. Replacing that with input converted to a char table and dealing with it by indices turned out to be about 10x faster. Other stuff (parsing only half of input for part 2 separately or with extra `if i <= len / 2`) yielded no improvement so far, though. 
### ...
### Day 07
- **Kotlin:**
  - Part 1 comes down to parsing input into some structure and then finding the only entry in it that doesn't have an underlying "program". Part 2, well, slightly more complicated, I kept adding "features" to the data structure and wroking with them in what seems to be a really clumsy way. But it worked, onwards to Lua, hoping to coming up with much better ideas there.