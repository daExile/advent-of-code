# Advent of Code 2024
### 6 :star:
Going for it in Lua 5.1 again, for now.

Links to puzzles and maybe some notes:
## Day 01 - [Historian Hysteria](https://adventofcode.com/2024/day/1)
## Day 02 - [Red-Nosed Reports](https://adventofcode.com/2024/day/2)
Took me some time to come up with and code something that wasn't an outright bruteforce check for each level in bad reports.

Current solution parses a report and counts positive / zero / negative deltas, and collects delta signs + values. Next, it decides what's the overall trend - increasing or decreasing - in the report (simple check of what do we have more of, negatives or positives, for equal count / most zeroes cases it will get the correct answer in the end anyway, so I didn't bother with more logic here :) and then gets a list of indexes of `bad_gaps` that don't fit the trend.

For part 1, only reports with `bad_gaps` length of `0` are considered safe. For part 2, some reports are rechecked: with `1` we check if dropping either left or right side of a bad gap gives us a perfectly safe report, with `2`, we check if bad gaps are adjacent, and whether dropping the middle value passes the test.
## Day 03 - [Mull It Over](https://adventofcode.com/2024/day/3)
Messy regex, because you don't have alternates in Lua. I also forgot to add a check for empty arguments in `do()` / `don't()`, but it worked fine without it, so... let me know if it explodes with some inputs.