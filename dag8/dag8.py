import math

with open("input.txt", "r") as f:
    read = f.read()
    data = [line.strip() for line in read.splitlines() if line]  # gets lines from file
    startNodes = [line.strip() for line in read.split() if line and line.endswith("A")]  # nodes ending with A
# parsing


def parse_to_map(data):
    mapping = {}
    for e in data:
        content = e.replace(" ", "").split("=")
        key = content[0]
        val = tuple(map(str.strip, content[1][1:-1].split(',')))
        mapping[key] = val

    return mapping


# doesn't work but should be the same
def traverse_rec(map_data, pos, steps, dirs):
    if pos == "ZZZ":
        return steps

    direction = dirs[steps % len(dirs)]
    dir_indx = 0 if direction == "L" else 1

    to = map_data[pos][dir_indx]
    return traverse_rec(map_data, to, steps + 1, dirs)


# traverses iteratively, works
def traverse_it(map_data, pos, steps, directions):
    while pos != "ZZZ":
        direction = directions[steps % len(directions)]
        pos = map_data[pos][0] if direction == "L" else map_data[pos][1]
        steps += 1
    return steps


# traverses from nodes ending with Z to nodes ending with Z (can be multiple)
def traverse_mult(map_data, starts, directions):
    path_steps = [0] * len(starts)
    dir_length = len(directions)

    # gathers steps for each start-node
    for i, node in enumerate(starts):
        while not node.endswith("Z"):
            direction = directions[path_steps[i] % dir_length]
            node = map_data[node][0] if direction == "L" else map_data[node][1]
            path_steps[i] += 1

    return math.lcm(*path_steps) # calculates the LCM of steps in the list


directions = [x for x in data.pop(0)]
map_data = parse_to_map(data)
steps = traverse_it(map_data, "AAA", 0, directions)
mult_steps = traverse_mult(map_data, startNodes, directions)

print(f'Steps from AAA nodes to ZZZ nodes: {steps}')
print(f'Steps ending with A to ending with Z: {mult_steps}')
