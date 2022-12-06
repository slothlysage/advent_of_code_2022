input = open('puzzle_input', 'r').read()

window = []
index = 0

for i, char in enumerate(input):
    if i >= 3:
        window = input[i - 3:i]
        if char not in window and len(set(window)) == 3:
            index = i + 1
            break

print(index)
