from collections import deque

input = open('puzzle_input', 'r')

map, starts, end = {}, [], None

direction_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i, line in enumerate(input):
    for j, char in enumerate(line.strip()):
        if char == "S" or char == "a":
            starts.append((i, j))
            map[(i, j)] = 'a'
            continue
        if char == "E":
            end = (i, j)
            map[(i, j)] = 'z'
            continue
        map[(i, j)] = char

def bfs(map, location):
    seen = set()
    d = deque()
    d.append((0, location))
    while (len(d) > 0):
        (distance, (x, y)) = d.popleft()
        if (x, y) == end:
            return distance
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for (dx, dy) in direction_vectors:
            step = ( x + dx, y + dy)
            if step in map and (ord(map[step]) < ord(map[(x, y)]) + 2) :
                d.append((distance + 1, step))
    return -1

solutions = {bfs(map, start) for start in starts}
solutions.remove(-1)
print(solutions)
print(min(list(solutions)))
