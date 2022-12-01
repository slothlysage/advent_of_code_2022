input = open('puzzle_input', 'r')
elves = []
elf = 0

for line in input:
    if line == '\n':
        if elf != 0:
            elves.append(elf)
        elf = 0
    else:
        elf += int(line)

elves.sort(reverse=True)
print(sum(elves[:3]))
