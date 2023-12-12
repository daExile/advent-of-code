use std::fs::read_to_string;
use std::collections::HashMap;

fn digits(mut n: i32) -> Vec<i32> {
    let mut digits = Vec::<i32>::new();
    while n > 0 {
        let t = n % 10;
        if digits.last().unwrap_or(&9) >= &t {
            digits.push(n % 10); n /= 10;
        } else { return Vec::<i32>::new(); }
    }
    digits.reverse();

    digits
}

fn parse_input(input: String) -> (i32, i32) {
    let t: Vec<i32> = input.trim().split('-').map(|x| x.parse::<i32>().unwrap()).collect();

    (t[0], t[1])
}

fn main() {
    let input = read_to_string("../__in/04.txt").unwrap();
    let (a, b) = parse_input(input);
    let mut count1 = 0;
    let mut count2 = 0;

    for n in a..=b {
        let d = digits(n);
        if !d.is_empty() {
            let mut d_count = HashMap::new();
            for digit in d { d_count.entry(digit).and_modify(|x| *x += 1).or_insert(1); }

            if d_count.iter().any(|(_, &v)| v >= 2) { count1 += 1; }
            if d_count.iter().any(|(_, &v)| v == 2) { count2 += 1; }
        }
    }

    println!("Part 1: {}", count1);
    println!("Part 2: {}", count2);
}