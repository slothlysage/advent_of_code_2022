input = open('puzzle_input', 'r')
sum = 0
elf_1 = elf_2 = elf_3 = ""

for line in input:
    line = line.strip()
    if elf_1 == "":
        elf_1 = line
    elif elf_2 == "":
        elf_2 = line
    elif elf_3 == "":
        elf_3 = line
        similar = list(set(elf_1).intersection(set(elf_2), set(elf_3)))[0]
        if similar.islower():
            sum += ord(similar) - 96
        elif similar.isupper():
            sum += ord(similar) - 38
        elf_1 = elf_2 = elf_3 = ""

print(sum)
