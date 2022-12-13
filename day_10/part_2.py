input = open('puzzle_input', 'r')

cycles = []
crt = []
prev = 1

for line in input:
    line = line.split(" ")
    cycles.append(prev)
    if line[0] == "addx":
        cycles.append(prev)
        prev = prev + int(line[1])

for i, cycle in enumerate(cycles):
    symbol = "."
    if (i % 40 == cycle - 1) or (i % 40 == cycle) or (i % 40== cycle + 1):
        symbol = "#"
    print(symbol, end=" ")
    if (i + 1) % 40 == 0:
        print(" ")
