input = open('puzzle_input', 'r')
sum = 0

for line in input:
    line = line.strip()
    length = int(len(line) / 2)
    half_1 = line[:length]
    half_2 = line[length:]
    similar = list(set(half_1).intersection(set(half_2)))[0]
    if similar.islower():
        sum += ord(similar) - 96
    elif similar.isupper():
        sum += ord(similar) - 38

print(sum)
