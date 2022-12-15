from datetime import datetime

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

input = open('puzzle_input', 'r')

map = {}

for i, line in enumerate(input):
    for j, char in enumerate(line.strip()):
        map[(i, j)] = char

# print(map)

# try direction, check if solved, if not recurse, add solution to array, keep going until done
# breadth first
start = [i for i in map if map[i] == "S"][0]
solutions = []
# print(map[start])
map[start] = 'a'
# print(start)

highest_char = 'a'
steps = {0}
count = 0

def solve_map(map, char, location):
    # print(location)
    # print(steps)
    # print(char)
    global highest_char
    global steps
    global solutions
    global count
    count += 1
    if count % 1000000 == 0:
        print(int(count / 1000000))
    if ord(char) > ord(highest_char):
        highest_char = char
        print(highest_char)
    if len(steps) > 400:
        #print(f"length greater than 300: {char}")
        return False
    if location not in map:
        #print("Failed location: {char}")
        return False
    if location in steps:
        return False
    # if location in steps:
    #     #print("Failed step: {char}")
    #     return False
    if char == 'z' and map[location] == "E":
        print("Solution found!!!")
        print(solutions)
        solutions.append(len(steps) - 1)
        return True
    if (ord(map[location]) > ord(char) + 1):
        #print(f"{map[location]} is not greater or equal to {char}")
        return False
    steps.add(location)
    (x, y) = location
    #print(char)
    solve_map(map, map[location], (x + 1, y))
    solve_map(map, map[location], (x - 1, y))
    solve_map(map, map[location], (x, y + 1))
    solve_map(map, map[location], (x, y - 1))
    steps.remove(location)
    return False

solve_map(map, "a", start)

print(solutions)
print(min(solutions))

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
