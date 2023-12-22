# Advent of Code 2023
### 44 :star:
Live event being done in Lua 5.1 (which I sort of regret now - I like lightweight Lua on its own, but having to do all the extra work to write library functions kind of shows when you're on timer. Oh well :)

Just some notes and no detailed walkthroughs until later.
## Day 01 - [Trebuchet?!](https://adventofcode.com/2023/day/1)
## Day 02 - [Cube Conundrum](https://adventofcode.com/2023/day/2)
The code honestly parses each roll separately, as I assumed it's gonna be important in part 2, and when it wasn't, I left it as is anyway.
## Day 03 - [Gear Ratios](https://adventofcode.com/2023/day/3)
Current solution uses a silly assumption that parts can't have the same number twice in a row, or something like that. It isn't a big deal to fix but it worked for my input, so I just didn't :P
## Day 04 - [Scratchcards](https://adventofcode.com/2023/day/4)
## Day 05 - [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)
Fair warning, live solution just naively bruteforces part 2 (takes about 17 min w/LuaJIT on my rather old machine). I tried to make faster one while this code was running, and failed twice - the program finished faster, and the idea was bad, as second version added way too much overhead which killed all its potential benefits lol. Yep, I scrapped it and will make a better one with ranges later.
## Day 06 - [Wait For It](https://adventofcode.com/2023/day/6)
This one is also a straight bruteforce. Again, I wanted to solve it with math but kinda got lost in which values exactly I should pass to the quadratic formula :) Also, it solves the puzzle in some milliseconds "as is" (with LuaJIT help, but still).
## Day 07 - [Camel Cards](https://adventofcode.com/2023/day/7)
## Day 08 - [Haunted Wasteland](https://adventofcode.com/2023/day/8)
Not marked with `_live`, because technically it isn't - I cut some corners in part 2, manually putting in some parameters to find loop sizes, test if each starting point may lead to different exits or not, et cetera, and then doing math by hand to get the answer (you can see some remnants of that in the code). The solution that gives answer on its own was only implemented after sending the answer in and getting the shiny :D
## Day 09 - [Mirage Maintenance](https://adventofcode.com/2023/day/9)
## Day 10 - [Pipe Maze](https://adventofcode.com/2023/day/10)
## Day 11 - [Cosmic Expansion](https://adventofcode.com/2023/day/11)
## Day 12 - [Hot Springs](https://adventofcode.com/2023/day/12)
## Day 13 - [Point of Incidence](https://adventofcode.com/2023/day/13)
Part 1 was done at first by comparing strings directly. Then part 2 arrived and asked us to evaluate the degree of difference between "reflections", it was refactored into per-tile comparison. One could optimise it by cutting short all checks that have more than 1 tile difference, but with maps Eric supplied for this puzzle it finishes in milliseconds "as is".
## Day 14 - [Parabolic Reflector Dish](https://adventofcode.com/2023/day/14)
## Day 15 - [Lens Library](https://adventofcode.com/2023/day/15)
## Day 16 - [The Floor Will Be Lava](https://adventofcode.com/2023/day/16)
## Day 17 - [Clumsy Crucible](https://adventofcode.com/2023/day/17)
Alright, this was a bumpy road, and the final result is pretty sketchy, too. Takes about 15 min to solve on my machine and might explode, you are warned. It does, however, give correct answers for my input and main example grid (both parts) and special part 2 example (p2, p1 explodes :), so I called it a day.
## Day 18 - [Lavaduct Lagoon](https://adventofcode.com/2023/day/18)
A tribute to wasted time, haha - I bruteforced part 1 (by making a 2D table of boundaries and flood-filling it) for starters, and then part 2 called for a different approach. And then I wasted more time by trying to come up with some algorithm before doing research. So all I got was a t- ...ext file with part 1 dig plan printout.

Anyway, it now uses a combination of [shoelace](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's](https://en.wikipedia.org/wiki/Pick%27s_theorem) formulae to find area and then extract number of points inside the loop using known area and perimeter. Yay.
## Day 19 - [Aplenty](https://adventofcode.com/2023/day/19)
## Day 20 - [Pulse Propagation](https://adventofcode.com/2023/day/20)
Letting the thing run for part 2, hoping that it will just magically arrive to the answer, was a mistake, as usual. Enter the Haunted Wasteland-like loop size search to save the day half an hour later.
## Day 21 - [Step Counter](https://adventofcode.com/2023/day/21)
Working with some input details again, shortcutting it with the assumption that all inputs have edges of the map and cardinal directions from starting point empty, and that our elf would only ever enter adjacent map tile from the corner or edge center. Plus some sketchy-looking loop math that I certainly did not expect to work on the first try.
## Day 22 - [Sand Slabs](https://adventofcode.com/2023/day/22)