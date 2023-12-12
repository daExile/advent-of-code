use std::fs::read_to_string;

fn read_lines(file: &str) -> Vec<i32> {
    let mut result = Vec::new();

    for line in read_to_string(file).unwrap().lines() {
        let n: i32 = line.trim().parse().unwrap();
        result.push(n)
    }
    
    result
}

fn get_fuel_fuel(fuel: i32) -> i32 {
    let extra_fuel = fuel / 3 - 2;

    if extra_fuel <= 0 { 0 } else { extra_fuel + get_fuel_fuel(extra_fuel) }
}

fn main() {
    let mut fuel_modules: i32 = 0;
    let mut fuel_total: i32 = 0;

    for n in read_lines("../__in/01.txt") {
        let fuel = n / 3 - 2;
        fuel_modules += fuel;
        fuel_total += fuel + get_fuel_fuel(fuel);
    }
    println!("Part 1: {}", fuel_modules);
    println!("Part 2: {}", fuel_total);
}