input = open('puzzle_input', 'r')

H = (0, 0)
T = (0, 0)
visited = set([T, H])
game = (H, T, visited)

def move_tail(game):
    (H, T, visited) = game
    (hx, hy) = H
    (tx, ty) = T
    if hx == tx + 2:
        if hy == ty + 1:
            T = (tx + 1, ty + 1)
        elif hy == ty - 1:
            T = (tx + 1, ty - 1)
        else:
            T = (tx + 1, ty)
    elif hx == tx - 2:
        if hy == ty + 1:
            T = (tx - 1, ty + 1)
        elif hy == ty - 1:
            T = (tx - 1, ty - 1)
        else:
            T = (tx - 1, ty)
    elif hy == ty + 2:
        if hx == tx + 1:
            T = (tx + 1, ty + 1)
        elif hx == tx - 1:
            T = (tx - 1, ty + 1)
        else:
            T = (tx, ty + 1)
    elif hy == ty - 2:
        if hx == tx + 1:
            T = (tx + 1, ty - 1)
        elif hx == tx - 1:
            T = (tx - 1, ty - 1)
        else:
            T = (tx, ty - 1)
    visited.add(T)
    return (H, T, visited)


def move_head(move, game):
    (H, T, visited) = game
    (dir, len) = move
    for _ in range(len):
        (hx, hy) = H
        if dir == 'R':
            H = (hx + 1, hy)
        if dir == 'U':
            H = (hx, hy + 1)
        if dir == 'L':
            H = (hx - 1, hy)
        if dir == 'D':
            H = (hx, hy - 1)
        H, T, visited = move_tail((H, T, visited))
    return((H, T, visited))

for line in input:
    line = line.split()
    direction = line[0]
    length = int(line[1])
    move = (direction, length)
    game = move_head(move, game)

print(len(visited))
