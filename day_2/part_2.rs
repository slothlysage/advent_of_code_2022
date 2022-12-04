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
    let outcome = match right {
        'X' => Some(Outcome::Lose),
        'Y' => Some(Outcome::Draw),
        'Z' => Some(Outcome::Win),
        _ => None,
    };
    let player = match (&opponent, &outcome) {
        (Some(Throw::Rock), Some(Outcome::Win)) => Throw::Paper,
        (Some(Throw::Rock), Some(Outcome::Lose)) => Throw::Scissors,
        (Some(Throw::Paper), Some(Outcome::Win)) => Throw::Scissors,
        (Some(Throw::Paper), Some(Outcome::Lose)) => Throw::Rock,
        (Some(Throw::Scissors), Some(Outcome::Win)) => Throw::Rock,
        (Some(Throw::Scissors), Some(Outcome::Lose)) => Throw::Paper,
        (_, _) => opponent.unwrap(),
    };
    score += match &player {
        Throw::Rock => 1,
        Throw::Paper => 2,
        Throw::Scissors => 3,
    };
    score += match &outcome.unwrap() {
        Outcome::Win => 6,
        Outcome::Draw => 3,
        Outcome::Lose => 0,
    };
    score
}
