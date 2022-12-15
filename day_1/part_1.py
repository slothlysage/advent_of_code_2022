# first solution
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

print(max(elves))

# one liner
print(max([sum(list(map(int, i.split('\n')))) for i in open('puzzle_input', 'r').read().strip('\n').split("\n\n")]))
