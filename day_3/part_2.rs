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
    let mut elf_1: HashSet<char> = HashSet::new();
    let mut elf_2: HashSet<char> = HashSet::new();

    for i in &split {
        if *i == "" { continue; }
        if elf_1.is_empty() {
            elf_1 = String::from(*i).chars().collect();
        } else if elf_2.is_empty() {
            elf_2 = String::from(*i).chars().collect();
        } else {
            let elf_3 = String::from(*i).chars().collect();
            let intersect: char = *elf_1.intersection(&(elf_2.intersection(&elf_3).copied().collect())).next().unwrap();
            sum += match intersect {
                'a'..='z' => intersect as u32 - 96,
                'A'..='Z' => intersect as u32 - 38,
                _ => 0,
            };
            elf_1.clear();
            elf_2.clear();
        }
    }
    println!("{sum}");
}
