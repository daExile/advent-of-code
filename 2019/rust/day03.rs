use std::fs::read_to_string;
use std::collections::HashMap;

fn read_lines(file: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(file).unwrap().lines() {
        result.push(line.to_string())
    }
    
    result
}

fn parse_wire_data(input: &String) -> Vec<(char, i32)> {
    input.trim().split(',').map(|x| (x.chars().next().unwrap(), x[1..].parse::<i32>().unwrap())).collect()
}

fn get_delta(c: char) -> (i32, i32) {
    match c {
        'U' => (0, 1),
        'D' => (0, -1),
        'L' => (-1, 0),
        'R' => (1, 0),
        _ => (0, 0),
    }
}

fn main() {
    let input = read_lines("../__in/03.txt");
    let wire1: Vec<(char, i32)> = parse_wire_data(&input[0]);
    let wire2: Vec<(char, i32)> = parse_wire_data(&input[1]);

    let mut wire_data = HashMap::<(i32, i32), (i32, i32)>::new();

    // parse wire1
    let mut xy: (i32, i32) = (0, 0);
    let mut step = 0;
    for segment in wire1 {
        let delta = get_delta(segment.0);
        for _n in 1..=segment.1 {
            xy = (xy.0 + delta.0, xy.1 + delta.1);
            step += 1;
            if !wire_data.contains_key(&xy) { wire_data.insert(xy, (step, 0)); }
        }
    }

    // parse wire2
    xy = (0, 0);
    step = 0;
    for segment in wire2 {
        let delta = get_delta(segment.0);
        for _n in 1..=segment.1 {
            xy = (xy.0 + delta.0, xy.1 + delta.1);
            step += 1;
            if wire_data.contains_key(&xy) {
                let t = wire_data.get(&xy).unwrap();
                if t.1 == 0 { wire_data.insert(xy, (t.0, step)); }
            }
        }
    }

    wire_data.retain(|_, val| val.0 != 0 && val.1 != 0);

    let mut x_closest_score = i32::MAX;
    let mut x_shortest_score = i32::MAX;
    for (key, val) in wire_data.iter() {
        if key.0.abs() + key.1.abs() < x_closest_score { x_closest_score = key.0.abs() + key.1.abs(); }
        if val.0 + val.1 < x_shortest_score { x_shortest_score = val.0 + val.1; }
    }
    println!("Part 1: {}", x_closest_score);
    println!("Part 2: {}", x_shortest_score);
}