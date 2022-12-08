input = open('puzzle_input', 'r').read().split()

trees = [[int(j) for j in i] for i in input]
visible = [[0 for _ in i] for i in trees]

edge_num = len(input) * 4 - 4

print(edge_num)

def check_left(i, j):
    tree = trees[i][j]
    for k in range(0, j):
        if trees[i][k] >= tree:
            return(False)
    return(True)

def check_top(i, j):
    tree = trees[i][j]
    for k in range(0, i):
        if trees[k][j] >= tree:
            return(False)
    return(True)

def check_right(i, j):
    tree = trees[i][j]
    for k in reversed(range(j + 1, len(trees))):
        if trees[i][k] >= tree:
            return(False)
    return(True)

def check_bottom(i, j):
    tree = trees[i][j]
    for k in reversed(range(i + 1, len(trees))):
        if trees[k][j] >= tree:
            return(False)
    return(True)

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees) - 1):
        if check_left(i, j) or check_top(i, j) or check_right(i, j) or check_bottom(i, j):
            visible[i][j] = 1

print(sum([sum(i) for i in visible]) + edge_num)
