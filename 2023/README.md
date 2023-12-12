# Advent of Code 2023
### 24 :star:
Live event being done in Lua 5.1 (which I sort of regret now - I like lightweight Lua on its own, but having to do all the extra work to write library functions kind of shows when you're on timer. Oh well :)

Just some notes and no detailed walkthroughs until later.
## Day 01 - [Trebuchet?!](https://adventofcode.com/2023/day/1)
## Day 02 - [Cube Conundrum](https://adventofcode.com/2023/day/2)
## Day 03 - [Gear Ratios](https://adventofcode.com/2023/day/3)
Current solution uses a silly assumption that parts can't have the same number twice in a row, or something like that. It isn't a big deal to fix but it worked for my input, so I just didn't :P
## Day 04 - [Scratchcards](https://adventofcode.com/2023/day/4)
## Day 05 - [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)
Fair warning, live solution just naively bruteforces part 2 (takes about 17 min w/LuaJIT on my rather old machine). I tried to make faster one while this code was running, and failed twice - the program finished faster, and the idea was bad, as second version added way too much overhead which killed all its potential benefits lol. Yep, I scrapped it and will make a better one with ranges later.
## Day 06 - [Wait For It](https://adventofcode.com/2023/day/6)
This one is also a straight bruteforce. Again, I wanted to solve it with math but kinda got lost in which values exactly I should pass to the quadratic formula :) Also, it solves the puzzle in some milliseconds "as is" (with LuaJIT help, but still).
## Day 07 - [Camel Cards](https://adventofcode.com/2023/day/7)
## Day 08 - [Haunted Wasteland](https://adventofcode.com/2023/day/8)
Not marked as "live", because I cut some corners in part 2, manually putting in some parameters to find lood sizes, test if each starting point may lead to different exits or not, et cetera, and then doing math by hand to get the answer (you can see some remnants of that in the code). The solution that gives answer on its own was only implemented after sending the answer in and getting the shiny :D
## Day 09 - [Mirage Maintenance](https://adventofcode.com/2023/day/9)
## Day 10 - [Pipe Maze](https://adventofcode.com/2023/day/10)
## Day 11 - [Cosmic Expansion](https://adventofcode.com/2023/day/11)
## Day 12 - [Hot Springs](https://adventofcode.com/2023/day/12)