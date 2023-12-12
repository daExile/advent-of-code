# Advent of Code 2019
### 8:star:
Launguages used for the playthrough this time:
- **Lua**: 5.1, as something "known well enough"
- **C++**: 2020 edition, absolutely arbitrary choice for a trip down memory lane (don't expect much, haha, my prior experience dates back to pre-modern builds, I might not even use any C++20 features in the end :)
- **Rust**: 1.72 for now, as a "new and tasty" alternative.
## Day 01 - [The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1)
The warm-up puzzle for AoC2019 is a pretty straightforward math problem, in part 1 at least - a list or integers (spaceship module weights) that we need to calculate matching amounts of fuel for (apply the `n / 3 - 2` formula to), and get the total. Nothing tricky here, aside of **Lua** not having integer division in 5.1 and needing `math.floor()` applied to the result (but the example will be of **Rust** instead):
```rust
fn main() {
    let mut fuel_modules: i32 = 0;

    for n in input_list_as_vec_i32 {
        let fuel = n / 3 - 2;
        fuel_modules += fuel;
    }
    println!("Part 1: {}", fuel_modules);
}
```
Turns out, all this fuel, too, won't fly on *wishing really hard*, and part 2 asks to find the grand total of fuel needed for modules and fuel to lift them off, then all the fuel for this new amount, and so on until our formula gives `0` for it (where negative results are treated as zeroes). I chose using recursive function to deal with it:
```rust
fn get_fuel_fuel(fuel: i32) -> i32 {
    let extra_fuel = fuel / 3 - 2;

    if extra_fuel <= 0 { 0 } else { extra_fuel + get_fuel_fuel(extra_fuel) }
}

fn main() {
    // ...
    let mut fuel_total: i32 = 0;

    for n in input_list_as_vec_i32 {
        let fuel = n / 3 - 2;
        // ...
        fuel_total += fuel + get_fuel_fuel(fuel);
    }
    // ...
    println!("Part 2: {}", fuel_total);
}
```
## Day 02 - [1202 Program Alarm](https://adventofcode.com/2019/day/2)
A-ha, the fun part of AoC 2019 begins here, the Intcode series. As it usually is like in AoC, we're building our own interpreter for a made-up assembly, but this time it spans across the entirety of the event

The Intcode uses only integers for both its opcodes and data (which allows modifying the program on the go, as one of provided examples shows).

An Intcode program is a list of integers that represent initial memory state, starting from address `0` (which is also the starting point of the program). The integer at the pointer is an opcode, and all its parameters immediately follow it in the memory. After operation is finished, pointer is moved to the address immediately after last parameter, and so on until the program terminates.

For starters we get three opcodes:
- `1` (takes 3 parameters): addition, reads two values stored in memory by addresses in first two parameters, and saves their sum by the address in the third.
- `2` (takes 3 parameters): multiplication, same as above but the result is the product of two values.
- `99` marks the end of a program.

Ok, first we parse input into some suitable collection. In Lua, we only have tables, so a table it is :) Also, I'm making sure that resulting table starts from index `0` for convenience.
```lua
local code, n = {}, 0
for item in string.gmatch(io.open("02.txt", "r"):read(), "[%d%-]+") do code[n] = tonumber(item); n = n + 1 end
```
Also, as running an Intcode program modifies memory contents, some way to keep the original sequence or to provide copies for each run is needed. Lua doesn't make copying tables easy, so I decided to create another, "RAM" table to store runtime values, instead of manually making a copy of original Intcode every time. And a getter that checks if there's a modified value for a given address, before reading it from unchanged program sequence:
```lua
local mem = {}
local function get(ptr) return mem[ptr] or code[ptr] end
```
Now, the runner itself with opcodes we are given.
```lua
local function run()
    local ptr = 0
    while get(ptr) ~= 99 do
        if get(ptr) == 1 then mem[get(ptr + 3)] = get(get(ptr + 1)) + get(get(ptr + 2))
        elseif get(ptr) == 2 then mem[get(ptr + 3)] = get(get(ptr + 1)) * get(get(ptr + 2)) end
        ptr = ptr + 4
    end
end
```
Reading opcode, and then reading values from two addresses and putting the result by third, until we hit opcode `99`.

Alright. Now, to solve the puzzle itself. Part 1 asks to load a pair of specific values into memory by addresses `1` and `2`, run the program, and read the resulting value from `0`. So, we can initialise the `mem` table with required values and do the thing:
```lua
mem = {12, 2}; run()
print(get(0))
```
Part 2 is very similar, just requires more work - we need to find a similar pair of values (dubbed `noun` and `verb`), that, when loaded into memory, lead to a desired value in the output after executing the code.
```lua
local function nvsearch(target)
    for noun = 0, 99 do
        for verb = 0, 99 do
            mem = {noun, verb}; run()
            
            if get(0) == target then return 100 * noun + verb end
        end end end
```
Nothing fancy this time, iterating over given ranges until we get the result, and extracting these newfound starting values in the requested `100 * noun + verb` format.

## Day 03 - [Crossed Wires](https://adventofcode.com/2019/day/3)
Solved, write-ups later, as it's AoC2023 time now.
## Day 04 - [Secure Container](https://adventofcode.com/2019/day/4)
Same as above :)