input = open('puzzle_input', 'r')
sum = 0

for line in input:
    line = line.strip().split(',')
    pair_1 = line[0].split('-')
    pair_2 = line[1].split('-')
    range_1 = set(range(int(pair_1[0]), int(pair_1[1]) + 1))
    range_2 = set(range(int(pair_2[0]), int(pair_2[1]) + 1))
    intersection = range_1 & range_2
    if (intersection == range_1) or (intersection == range_2):
        sum += 1

print(sum)
