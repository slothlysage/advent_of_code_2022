input = open('puzzle_input', 'r')

ops = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

monkeys = {}

monkey = {}

for line in input:
    line = line.split(":")
    if line[0][0] == 'M':
        monkey = {}
        monkey["name"] = line[0]
    elif line[0].strip() == "Starting items":
        monkey["items"] = list(map(int, line[1].split(",")))
    elif line[0].strip() == "Operation":
        op = line[1].split()
        monkey["op"] = (op[3] , op[4])
    elif line[0].strip() == "Test":
        monkey["test"] = int(line[1].split()[2])
    elif line[0].strip() == "If true":
        monkey["true"] = line[1].split()[3]
    elif line[0].strip() == "If false":
        monkey["false"] = line[1].split()[3]
    elif len(line) == 1:
        monkey["count"] = 0
        monkeys[monkey["name"]] = monkey
monkey["count"] = 0
monkeys[monkey["name"]] = monkey

for _ in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[f"Monkey {i}"]
        for i in range(len(monkey["items"])):
            item = monkey["items"][i]
            (sym, val) = monkey["op"]
            val = item if val == "old" else int(val)
            new_item = int(ops[sym](item, val) / 3)
            if new_item % monkey["test"] == 0:
                monkeys[f"Monkey {monkey['true']}"]["items"].append(new_item)
            else:
                monkeys[f"Monkey {monkey['false']}"]["items"].append(new_item)
            monkey["count"] += 1
        monkey["items"] = []

vals = sorted([monkey["count"] for monkey in monkeys.values()])
print(vals[-1] * vals[-2])
