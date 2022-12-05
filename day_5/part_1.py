input = open('puzzle_input', 'r')

puzzle_raw = []
steps = []

for i, line in enumerate(input):
    if i < 8:
        puzzle_raw.append(line.strip('\n'))
    if i > 9:
        step = line.strip().split()
        steps.append((step[1], step[3], step[5]))

puzzle_raw.reverse()
puzzle = [[i] for i in range(1, 10)]

for row in puzzle_raw:
    i = 0
    for r in range(1, 35, 4):
        if row[r].isalnum():
            puzzle[i].append(row[r])
        i += 1

for step in steps:
    for i in range(int(step[0])):
        puzzle[int(step[2]) - 1].append(puzzle[int(step[1]) - 1].pop())

print([i.pop() for i in puzzle])
