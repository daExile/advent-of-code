# Advent of Code 2024
### 24 :star:
Going for it in Lua 5.1 again, for now.

Links to puzzles and maybe some notes:
## Day 01 - [Historian Hysteria](https://adventofcode.com/2024/day/1)
## Day 02 - [Red-Nosed Reports](https://adventofcode.com/2024/day/2)
Took me some time to come up with and code something that wasn't an outright bruteforce check for each level in bad reports.

Current solution parses a report and counts positive / zero / negative deltas, and collects delta signs + values. Next, it decides what's the overall trend - increasing or decreasing - in the report (simple check of what do we have more of, negatives or positives, for equal count / most zeroes cases it will get the correct answer in the end anyway, so I didn't bother with more logic here :) and then gets a list of indexes of `bad_gaps` that don't fit the trend.

For part 1, only reports with `bad_gaps` length of `0` are considered safe. For part 2, some reports are rechecked: with `1` we check if dropping either left or right side of a bad gap gives us a perfectly safe report, with `2`, we check if bad gaps are adjacent, and whether dropping the middle value passes the test.
## Day 03 - [Mull It Over](https://adventofcode.com/2024/day/3)
Messy regex, because you don't have alternates in Lua. I also forgot to add a check for empty arguments in `do()` / `don't()`, but it worked fine without it, so... let me know if it explodes with some inputs.
## Day 04 - [Ceres Search](https://adventofcode.com/2024/day/4)
## Day 05 - [Print Queue](https://adventofcode.com/2024/day/5)
Only the pairwise ordering lookup table due to loops lurking in the rules. On the bright side, we're provided with complete pair ordering data, so no deductions were required.
## Day 06 - [Guard Gallivant](https://adventofcode.com/2024/day/6)
Current code is sort of a naive bruteforce for part 2, just tries to put obstacle on each tile of the traced in part 1 path and checks if it loops. A fallback from another, supposedly faster approach, that I've put on hold due to a lot of false positives and debugging difficulties without a working solution to compare to. Though the naive one isn't terribly slow, either, ~2.7s on my ancient machine.
## Day 07 - [Bridge Repair](https://adventofcode.com/2024/day/7)
## Day 08 - [Resonant Collinearity](https://adventofcode.com/2024/day/8)
## Day 09 - [Disk Fragmenter](https://adventofcode.com/2024/day/9)
## Day 10 - [Hoof It](https://adventofcode.com/2024/day/10)
## Day 11 - [Plutonian Pebbles](https://adventofcode.com/2024/day/11)
## Day 12 - [Garden Groups](https://adventofcode.com/2024/day/12)
Part 1 is a map walk: start on an unvisited yet tile and check its neighbours, adding `1` to `area` for each adjacent tile with the same plant and marking it as visited, too; adding `1` to `perimeter` where adjacent tile is different (or doesn't exist = map edge), until a region is charted. Repeat until entire map is done.

For part 2, fence segments data was collected into a table, grouping by `direction` first and `lane` second (row or column, depending on direction), making a list of fence segment positions on a given lane (the other coordinate). Lists are then sorted and `sides` counted as `1 + number of continuity breaks`.