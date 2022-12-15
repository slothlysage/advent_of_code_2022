# first attempt
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

# one liner
print(sum(sorted([sum(list(map(int, i.split('\n')))) for i in open('puzzle_input', 'r').read().strip('\n').split("\n\n")])[-3:]))
