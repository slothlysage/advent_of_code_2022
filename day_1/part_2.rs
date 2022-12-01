use std::fs;

fn main() {
    let input = fs::read_to_string("puzzle_input")
        .expect("This should be able to read in the file");

    let split = input.split("\n");
    let split: Vec<&str> = split.collect();

    let mut elves: Vec<i32> = Vec::new();
    let mut elf: i32 = 0;
    for i in &split {
        let line: &str = i;
        match line.parse::<i32>() {
            Ok(n) => elf += n,
            Err(_e) => {
                if elf != 0 {
                    elves.push(elf);
                    elf = 0;
                }
            }
        }
    }

    elves.sort();
    let max_three = elves.split_off(elves.len() - 3);
    let sum: i32 = max_three.iter().sum();
    println!("{sum}");
}
