input = open('puzzle_input', 'r')

cycles = [1]
prev = cycles[-1]

for line in input:
    line = line.split(" ")
    cycles.append(prev)
    if line[0] == "addx":
        cycles.append(prev)
        prev = prev + int(line[1])

sum_six = 0
for i in range(6):
    sum_six += cycles[20 + (i * 40)] * (20 + (i * 40))

print(sum_six)
