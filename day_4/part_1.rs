use std::fs;

fn main() {
    let input = fs::read_to_string("puzzle_input")
        .expect("This should be able to read in the file");

    let mut sum = 0;
    for i in input.split("\n") {
        if i == "" { continue; }
        let mut ranges = i.split(",");
        let mut range_1 = ranges.next().unwrap().split("-").map(|x| x.parse::<i32>().unwrap());
        let mut range_2 = ranges.next().unwrap().split("-").map(|x| x.parse::<i32>().unwrap());
        let range_1_low = range_1.next().unwrap();
        let range_1_high = range_1.next().unwrap();
        let range_2_low = range_2.next().unwrap();
        let range_2_high = range_2.next().unwrap();
        if (range_1_low <= range_2_low && range_1_high >= range_2_high) || (range_1_low >= range_2_low && range_1_high <= range_2_high) {
            sum += 1
        }
    }
    println!("{sum}");
}
