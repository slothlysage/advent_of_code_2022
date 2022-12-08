input = open('puzzle_input', 'r').read().split()

trees = [[int(j) for j in i] for i in input]
visible = [[1 for _ in i] for i in trees]

def look_left(i, j):
    tree = trees[i][j]
    vision = 0
    for k in reversed(range(0, j)):
        if trees[i][k] < tree:
            vision += 1
        else:
            break
    return(vision if vision else 1)

def look_top(i, j):
    tree = trees[i][j]
    vision = 0
    for k in reversed(range(0, i)):
        if trees[k][j] < tree:
            vision += 1
        else:
            break
    return(vision if vision else 1)

def look_right(i, j):
    tree = trees[i][j]
    vision = 0
    for k in range(j + 1, len(trees)):
        if trees[i][k] < tree:
            vision += 1
        else:
            break
    return(vision if vision else 1)

def look_bottom(i, j):
    tree = trees[i][j]
    vision = 1
    for k in range(i + 1, len(trees)):
        if trees[k][j] < tree:
            vision += 1
        else:
            break
    return(vision)

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees) - 1):
        visible[i][j] *= look_left(i, j)
        visible[i][j] *= look_top(i, j)
        visible[i][j] *= look_right(i, j)
        visible[i][j] *= look_bottom(i, j)

print(max([max(i) for i in visible]))
