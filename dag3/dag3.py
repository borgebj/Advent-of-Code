# borgebj
# part of Advent of code 2023 day 3
# https://adventofcode.com/2023/day/3


def get_neighbors(arr, row, col):
    neighbors = []
    rows, cols = len(arr), len(arr[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if i != row or j != col:
                neighbors.append(arr[i][j])

    return neighbors


def retrieve_valid(num, lines, i):
    global valid
    for index in num.keys():
        adjacent = get_neighbors(lines, i, index)
        valid = not all(x.isdigit() or x == "." or x == "\n" for x in adjacent)

        if valid: break

    if valid: return int(''.join(map(str, num.values())))
    else: return 0


def part_one(inp_file):
    """
    param:
        input (string): name of input-file
    return:
        int: Sum of all part numbers from input
    """
    with open(inp_file) as file:
        lines = [x.replace("\n", "") for x in file.readlines()]
        tot_sum = 0

        for i, row in enumerate(lines):
            num = {}

            for j, digit in enumerate(row):

                # constructs a number
                if lines[i][j].isdigit():
                    num[j] = lines[i][j]

                # number is constructed, searches for valid part-numbers
                elif len(num) > 0:
                    valid_number = retrieve_valid(num, lines, i)
                    tot_sum += valid_number
                    num = {}

            # handles end-of-life numbers
            if len(num) > 0:
                valid_number = retrieve_valid(num, lines, i)
                tot_sum += valid_number

    return tot_sum


part_sum = part_one("input.txt")
print("part one:", part_sum)


def part_two(inp_file):
    """
    param:
        input (string): name of input-file
    return:
        int: Sum of all part gear-ratios from input
    """
    with open(inp_file) as file:
        lines = [x.replace("\n", "") for x in file.readlines()]

        for i, row in enumerate(lines):
            cogs = {}

            for j, digit in enumerate(row):
                if lines[i][j] == "*":
                    cogs[j] = lines[i][j]

            print(cogs)

    return "a"


ratio_sum = part_two("input.txt")
print("part two:", ratio_sum)
