use std::fs::read_to_string;

fn intcode_run(mut code: Vec<i32>, noun: i32, verb: i32) -> i32 {
    let mut ptr: usize = 0;
    code[1] = noun;
    code[2] = verb;

    while code[ptr] != 99 {
        let dest = code[ptr + 3] as usize;
        match code[ptr] {
            1 => code[dest] = code[code[ptr + 1] as usize] + code[code[ptr + 2] as usize],
            2 => code[dest] = code[code[ptr + 1] as usize] * code[code[ptr + 2] as usize],
            _ => continue,
        }
        ptr += 4;
    }

    code[0]
}

fn noun_verb_search(code: Vec<i32>, target: i32) -> i32 {
    for noun in 0..100 {
        for verb in 0..100 {
            if intcode_run(code.to_vec(), noun, verb) == target { return noun * 100 + verb }
        }
    }
    
    0
}

fn main() {
    let input = read_to_string("../__in/02.txt").unwrap();
    let code: Vec<i32> = input
        .trim()
        .split(',')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    println!("Part 1: {}", intcode_run(code.to_vec(), 12, 2));
    println!("Part 2: {}", noun_verb_search(code, 19690720));
}