input = open('puzzle_input', 'r')

knots_length = 10
knots = {}
for i in range(knots_length):
    knot = f"knot_{i}"
    knots[knot] = (0, 0)

visited = set(knots.values())

game = (knots, visited)

def print_knots():
    print(knots)
    height_max = max([y for (_, y) in knots.values()])
    width_max = max([x for (x, _) in knots.values()])
    height_max = 10 if height_max < 10 else height_max
    width_max = 10 if width_max < 10 else width_max
    height_min = min([y for (_, y) in knots.values()])
    width_min = min([x for (x, _) in knots.values()])
    height_min = -10 if height_min > -10 else height_min
    width_min = -10 if width_min > -10 else width_min
    height = height_max - height_min
    width = width_max - width_min
    board = [[0] * width for _ in range(height)]
    for i in reversed(range(knots_length)):
        knot_name = f"knot_{i}"
        (kx, ky) = knots[knot_name]
        board[ky + abs(height_min) - 1][kx + abs(width_min) - 1] = i if i > 0 else "H"
    for row in board:
        for item in row:
            print(item, end=" ")
        print("")

def print_visited(visited):
    height_max = max([y for (_, y) in visited])
    width_max = max([x for (x, _) in visited])
    height_max = 10 if height_max < 10 else height_max
    width_max = 10 if width_max < 10 else width_max
    height_min = min([y for (_, y) in visited])
    width_min = min([x for (x, _) in visited])
    height_min = -10 if height_min > -10 else height_min
    width_min = -10 if width_min > -10 else width_min
    height = height_max - height_min
    width = width_max - width_min
    board = [[0] * width for _ in range(height)]
    for i in visited:
        (kx, ky) = i
        board[ky + abs(height_min) - 1][kx + abs(width_min) - 1] = "#"
    for row in board:
        for item in row:
            to_print = item if item == "#" else " "
            print(to_print, end=" ")
        print("")


def move_tail(knots, visited):
    (knots, visited) = game
    for i in range(knots_length - 1):
        knot_h = f"knot_{i}"
        knot_t = f"knot_{i + 1}"
        (hx, hy) = knots[knot_h]
        (tx, ty) = knots[knot_t]
        dx = hx - tx
        dy = hy - ty
        if 2 <= abs(dx) or 2 <= abs(dy):
            knots[knot_t] = (tx if dx == 0 else tx + int(dx / abs(dx)), ty if dy == 0 else ty + int(dy / abs(dy)))
    visited.add(knots["knot_9"])
    return (knots, visited)


def move_head(move, game):
    (knots, visited) = game
    (dir, len) = move
    for _ in range(len):
        (hx, hy) = knots["knot_0"]
        if dir == 'R':
            H = (hx + 1, hy)
        if dir == 'U':
            H = (hx, hy + 1)
        if dir == 'L':
            H = (hx - 1, hy)
        if dir == 'D':
            H = (hx, hy - 1)
        knots["knot_0"] = H
        game = move_tail(knots, visited)
    return(knots, visited)

for line in input:
    line = line.split()
    direction = line[0]
    length = int(line[1])
    move = (direction, length)
    knots, visted = move_head(move, game)

print(len(visited))
