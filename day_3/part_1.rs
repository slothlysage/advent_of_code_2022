use std::{
    fs,
    collections::HashSet
};

fn main() {
    let input = fs::read_to_string("puzzle_input")
        .expect("This should be able to read in the file");

    let split = input.split("\n");
    let split: Vec<&str> = split.collect();

    let mut sum = 0;
    for i in &split {
        if *i == "" { continue; }
        let half = i.chars().count() / 2;
        let half_1: HashSet<char> = String::from(&i[..half]).chars().collect();
        let half_2: HashSet<char> = String::from(&i[half..]).chars().collect();
        let intersect: char = *half_1.intersection(&half_2).next().unwrap();
        sum += match intersect {
            'a'..='z' => intersect as u32 - 96,
            'A'..='Z' => intersect as u32 - 38,
            _ => 0,
        }
    }
    println!("{sum}");
}
