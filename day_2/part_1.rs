use std::fs;

fn main() {
    let input = fs::read_to_string("puzzle_input")
        .expect("This should be able to read in the file");

    let split = input.split("\n");
    let split: Vec<&str> = split.collect();

    let mut sum: i32 = 0;
    for i in &split {
        sum += match *i {
            "" => 0,
            _ => game(&i.chars().nth(0).unwrap(), &i.chars().nth(2).unwrap()),
        }
    }
    println!("{sum}");
}

enum Throw {
    Rock,
    Paper,
    Scissors,
}

enum Outcome {
    Lose,
    Draw,
    Win,
}

fn game(left: &char, right: &char) -> i32 {
    let mut score: i32 = 0;
    let opponent = match left {
        'A' => Some(Throw::Rock),
        'B' => Some(Throw::Paper),
        'C' => Some(Throw::Scissors),
        _ => None,
    };
    let player = match right {
        'X' => Some(Throw::Rock),
        'Y' => Some(Throw::Paper),
        'Z' => Some(Throw::Scissors),
        _ => None,
    };
    let outcome = match (&opponent, &player) {
        (Some(Throw::Rock), Some(Throw::Paper)) => Outcome::Win,
        (Some(Throw::Rock), Some(Throw::Scissors)) => Outcome::Lose,
        (Some(Throw::Paper), Some(Throw::Scissors)) => Outcome::Win,
        (Some(Throw::Paper), Some(Throw::Rock)) => Outcome::Lose,
        (Some(Throw::Scissors), Some(Throw::Rock)) => Outcome::Win,
        (Some(Throw::Scissors), Some(Throw::Paper)) => Outcome::Lose,
        _ => Outcome::Draw,
    };
    score += match &player {
        Some(Throw::Rock) => 1,
        Some(Throw::Paper) => 2,
        Some(Throw::Scissors) => 3,
        _ => 0,
    };
    score += match &outcome {
        Outcome::Win => 6,
        Outcome::Draw => 3,
        Outcome::Lose => 0,
    };
    score
}
