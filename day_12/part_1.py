from collections import deque

input = open('puzzle_input', 'r')

map, seen, start, end = {}, set(), None, None

direction_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i, line in enumerate(input):
    for j, char in enumerate(line.strip()):
        if char == "S":
            start = (i, j)
            map[(i, j)] = 'a'
            continue
        if char == "E":
            end = (i, j)
            map[(i, j)] = 'z'
            continue
        map[(i, j)] = char

def bfs(map, seen, location):
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

print(bfs(map, seen, start))
