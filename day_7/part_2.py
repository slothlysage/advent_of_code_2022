input = open('puzzle_input', 'r')

paths = {}
path = "/"
files = {}

def add_val_to_path(p, v):
    if p not in paths:
        paths[p] = v
    else:
        paths[p] += v

for line in input:
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                continue
            if line[2] == "..":
                split_path = path.split("/")
                split_path.remove(split_path[-2])
                path = "/".join(split_path[:len(split_path)])
            else:
                path = f"{path}{line[2]}/"
    elif line[0] != "dir":
        file = f"{path}{line[1]}"
        if file in files:
            continue
        files[file] = line[0]
        mini_p = "/"
        add_val_to_path(mini_p, int(line[0]))
        add_val_to_path(path, int(line[0]))
        split_path = path.split("/")
        for i in range(2, len(split_path) - 1):
            mini_p = f"/{'/'.join(split_path[1:i])}/"
            add_val_to_path(mini_p, int(line[0]))

space_needed = 30000000 - (70000000 - paths["/"])
candidates = [v for v in paths.values() if v >= space_needed]

print(min(candidates))
