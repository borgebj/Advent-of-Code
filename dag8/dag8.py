with open("input.txt", "r") as f:
    data = [line.strip() for line in f if line.strip()]


def parse_to_map(data):
    mapping = {}
    for e in data:
        content = e.replace(" ", "").split("=")
        key = content[0]
        val = tuple(map(str.strip, content[1][1:-1].split(',')))

        mapping[key] = val

    return mapping


def traverse(map_data, instructions):
    original_instructions = instructions.copy()
    start = list(map_data.keys())[0]
    end = "ZZZ"

    steps = 0
    while start != end:
        if start not in map_data: raise ValueError(f"'{start}' is not a valid key in map_data")
        if not instructions:
            instructions = original_instructions.copy()

        instruction = instructions.pop(0)

        dir_index = 0 if instruction == "L" else 1
        to = map_data[start][dir_index]

        start = to
        steps += 1

    return steps


def traverse_2(map_data, pos, steps, ins, orig):

    if pos == "ZZZ":
        return steps

    if not ins:
        ins = orig.copy()
        print(ins)
        print(orig)

    direction = 0 if ins.pop(0) == "L" else 1
    to = map_data[pos][direction]
    return traverse_2(map_data, to, steps+1, ins, orig)


instructions = [x for x in data.pop(0)]
map_data = parse_to_map(data)
steps = traverse_2(map_data, list(map_data.keys())[0], 0, instructions.copy(), instructions.copy())
print(f'Steps or whatever {steps}')
