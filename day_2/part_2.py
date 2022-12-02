rock = A = X = 1
paper = B = Y = 2
scissors = C = Z = 3

lost = 0
draw = 3
win = 6

input = open('puzzle_input', 'r')
score = 0

for line in input:
    op, me = line.split()
    if op == "A":
        if me == "X":
            score += lost
            score += scissors
        elif me == "Y":
            score += draw
            score += rock
        elif me == "Z":
            score += win
            score += paper
    elif op == "B":
        if me == "X":
            score += lost
            score += rock
        elif me == "Y":
            score += draw
            score += paper
        elif me == "Z":
            score += win
            score += scissors
    elif op == "C":
        if me == "X":
            score += lost
            score += paper
        elif me == "Y":
            score += draw
            score += scissors
        elif me == "Z":
            score += win
            score += rock

print(score)
